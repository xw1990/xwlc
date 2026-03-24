# src/vector_store/knowledge_base.py
import os
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from config.settings import settings

_retriever = None  # 单例模式

def init_vector_store():
    """初始化向量库（通常在服务启动时调用）"""
    global _retriever
    if _retriever is not None:
        return _retriever
    
    # 加载文档
    docs = []
    kb_dir = settings.knowledge_base_dir
    if not os.path.exists(kb_dir):
        os.makedirs(kb_dir)
        print(f"请将知识库文档放入 {kb_dir} 文件夹")
        return None
    
    for file in os.listdir(kb_dir):
        if file.endswith(".txt"):
            loader = TextLoader(os.path.join(kb_dir, file))
            docs.extend(loader.load())
    
    if not docs:
        print("⚠️ 知识库文件夹为空")
        return None
    
    # 切分
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.chunk_size,
        chunk_overlap=settings.chunk_overlap
    )
    splits = text_splitter.split_documents(docs)
    
    # 创建 embedding 和向量库
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma.from_documents(
        documents=splits,
        embedding=embeddings,
        persist_directory=settings.chroma_persist_dir
    )
    _retriever = vectorstore.as_retriever(search_kwargs={"k": settings.retrieval_k})
    return _retriever

def get_retriever():
    """获取检索器实例（若未初始化则自动初始化）"""
    if _retriever is None:
        return init_vector_store()
    return _retriever