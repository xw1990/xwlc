# config/settings.py

# 管理所有配置，从.env加载
from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional

class Settings(BaseSettings):
    # DeepSeek 配置
    deepseek_api_key: str = Field(..., env="DEEPSEEK_API_KEY")
    deepseek_api_base: str = "https://api.deepseek.com/v1"
    deepseek_model: str = "deepseek-chat"
    
    # 模型参数
    temperature: float = 0.0
    max_tokens: int = 1024
    
    # 知识库配置
    knowledge_base_dir: str = "data/knowledge_base"
    chroma_persist_dir: str = "data/chroma_db"
    chunk_size: int = 500
    chunk_overlap: int = 50
    retrieval_k: int = 3
    
    # 代理配置
    agent_max_iterations: int = 3
    agent_early_stopping: str = "force"
    agent_verbose: bool = True
    
    # 服务配置
    host: str = "0.0.0.0"
    port: int = 8000
    
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()