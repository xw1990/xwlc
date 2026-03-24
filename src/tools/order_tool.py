# src/tools/order_tool.py
from langchain.tools import tool

@tool
def get_order_status(order_id: str) -> str:
    """根据订单号查询订单状态。输入必须是订单号，例如'ORD123'。"""
    # 实际应该调用订单服务 API，这里简单模拟
    order_db = {"ORD123": "已发货", "ORD456": "正在配送", "ORD789": "已完成"}
    return order_db.get(order_id, "未找到该订单，请检查订单号。")