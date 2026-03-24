运行方式

cd ~/langchain_demo
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 准备知识库
mkdir -p data/knowledge_base
# 将你的 faq.txt 放入 data/knowledge_base/

# 初始化向量库（可选，服务启动时会自动初始化）
python scripts/init_vector_store.py

# 启动服务
python src/main.py

访问 http://localhost:8000/docs 测试 API
