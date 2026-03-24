# src/agents/customer_service.py
from langchain.agents import create_react_agent, AgentExecutor
from src.models.llm_factory import get_llm
from src.tools import get_order_status, search_knowledge_base
from src.prompts import load_customer_service_prompt
from config.settings import settings

def create_customer_service_agent(memory):
    """创建客服代理执行器"""
    llm = get_llm()
    tools = [get_order_status, search_knowledge_base]
    prompt = load_customer_service_prompt()
    
    agent = create_react_agent(llm, tools, prompt)
    
    executor = AgentExecutor(
        agent=agent,
        tools=tools,
        memory=memory,
        verbose=settings.agent_verbose,
        handle_parsing_errors=True,
        max_iterations=settings.agent_max_iterations,
        early_stopping_method=settings.agent_early_stopping,
        return_intermediate_steps=True
    )
    return executor