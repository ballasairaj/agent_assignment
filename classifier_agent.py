import os
import json
from typing import Dict
from PyPDF2 import PdfReader
import redis

# Initialize Redis connection
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def classify_format(file_path: str) -> str:
    """Classify file format"""
    if file_path.endswith('.pdf'):
        return 'PDF'
    elif file_path.endswith('.json'):
        return 'JSON'
    else:
        return 'Email'

def classify_intent(text: str) -> str:
    """Classify intent using LLM"""
    # Use LLM to classify intent
    # For demonstration purposes, a simple implementation is provided
    if 'invoice' in text.lower():
        return 'Invoice'
    elif 'rfq' in text.lower():
        return 'RFQ'
    else:
        return 'Unknown'

def route_to_agent(format: str, intent: str) -> str:
    """Route to correct agent"""
    if format == 'JSON':
        return 'JSON Agent'
    elif format == 'Email':
        return 'Email Agent'
    elif format == 'PDF':
        return 'PDF Agent'
    else:
        return 'Unknown'

def classify_and_route(file_path: str, text: str) -> Dict:
    """Classify and route to correct agent"""
    format = classify_format(file_path)
    intent = classify_intent(text)
    agent = route_to_agent(format, intent)
    #redis_client.hset('classification', file_path, json.dumps({'format': format, 'intent': intent}))
    return {'format': format, 'intent': intent, 'agent': agent}

# Example usage
file_path = 'D:\\Isnartech\\VTO_project\\Mr Sai raj sir quotation .pdf'
text = 'This is an example PDF file.'
classification = classify_and_route(file_path, text)
print(classification)
