# src/models/llm_factory.py
from langchain_openai import ChatOpenAI
from config.settings import settings

def get_llm():
    return ChatOpenAI(
        model=settings.deepseek_model,
        openai_api_key=settings.deepseek_api_key,
        openai_api_base=settings.deepseek_api_base,
        temperature=settings.temperature,
        max_tokens=settings.max_tokens
    )