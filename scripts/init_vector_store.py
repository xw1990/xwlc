# scripts/init_vector_store.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.vector_store.knowledge_base import init_vector_store

if __name__ == "__main__":
    print("正在初始化知识库...")
    retriever = init_vector_store()
    if retriever:
        print("✅ 知识库初始化成功")
    else:
        print("❌ 初始化失败，请检查 data/knowledge_base 文件夹")