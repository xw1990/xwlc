# src/memory/manager.py
from langchain.memory import ConversationBufferMemory

_memory_store = {}

def get_memory(user_id: str, session_id: str = "default") -> ConversationBufferMemory:
    """获取或创建用户记忆实例"""
    key = f"{user_id}:{session_id}"
    if key not in _memory_store:
        _memory_store[key] = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
    return _memory_store[key]

def clear_memory(user_id: str, session_id: str = "default"):
    """清理指定会话的记忆"""
    key = f"{user_id}:{session_id}"
    if key in _memory_store:
        del _memory_store[key]