# src/main.py
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

from config.settings import settings
from src.agents.customer_service import create_customer_service_agent
from src.memory.manager import get_memory
from src.vector_store.knowledge_base import init_vector_store

# 初始化知识库（启动时加载）
init_vector_store()

app = FastAPI(title="智能客服 API (重构版)", version="1.0.0")

class ChatRequest(BaseModel):
    message: str
    user_id: str
    session_id: Optional[str] = None

class ChatResponse(BaseModel):
    reply: str
    thinking: Optional[str] = None
    user_id: str
    session_id: str

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        # 获取用户记忆
        memory = get_memory(request.user_id, request.session_id or "default")
        
        # 创建代理执行器（每个请求新建，但复用记忆）
        agent_executor = create_customer_service_agent(memory)
        
        # 执行
        result = await agent_executor.ainvoke({"input": request.message})
        response = result["output"]
        intermediate_steps = result.get("intermediate_steps", [])
        
        # 格式化思考过程
        thinking_lines = []
        for action, observation in intermediate_steps:
            if hasattr(action, 'log') and action.log:
                thinking_lines.append(action.log.strip())
            thinking_lines.append(f"Observation: {observation}")
        thinking = "\n\n".join(thinking_lines) if thinking_lines else None
        
        return ChatResponse(
            reply=response,
            thinking=thinking,
            user_id=request.user_id,
            session_id=request.session_id or "default"
        )
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def root():
    return {"message": "智能客服 API 已启动", "docs": "/docs"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.host, port=settings.port)