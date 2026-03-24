# src/tools/knowledge_tool.py
from langchain.tools import tool
from src.vector_store.knowledge_base import get_retriever

@tool
def search_knowledge_base(query: str) -> str:
    """当用户询问关于退货政策、联系客服、发货时间等常见问题时，使用此工具查询知识库。"""
    retriever = get_retriever()
    docs = retriever.get_relevant_documents(query)
    if not docs:
        return "未找到相关信息。"
    return "\n\n".join([doc.page_content for doc in docs])