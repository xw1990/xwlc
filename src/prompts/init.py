# src/prompts/__init__.py
from langchain.prompts import PromptTemplate
import os

def load_customer_service_prompt() -> PromptTemplate:
    path = os.path.join(os.path.dirname(__file__), "customer_service.txt")
    with open(path, "r", encoding="utf-8") as f:
        template = f.read()
    return PromptTemplate.from_template(template)