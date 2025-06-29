import json
from typing import Dict

def extract_and_reformat(json_data: Dict) -> Dict:
    """Extract and reformat JSON data"""
    # Use LLM to extract and reformat data
    # For demonstration purposes, a simple implementation is provided
    extracted_data = {}
    for key, value in json_data.items():
        if key == 'invoice_number':
            extracted_data['invoice_id'] = value
        elif key == 'request_for_quote':
            extracted_data['rfq_id'] = value
    return extracted_data

def flag_anomalies(json_data: Dict) -> bool:
    """Flag anomalies or missing fields"""
    # Use LLM to flag anomalies or missing fields
    # For demonstration purposes, a simple implementation is provided
    required_fields = ['invoice_number', 'request_for_quote']
    for field in required_fields:
        if field not in json_data:
            return True
    return False

def process_json(json_data: Dict) -> Dict:
    """Process JSON data"""
    extracted_data = extract_and_reformat(json_data)
    anomalies = flag_anomalies(json_data)
    return {'extracted_data': extracted_data, 'anomalies': anomalies}

# Example usage
json_data = {'invoice_number': '12345', 'request_for_quote': 'RFQ-12345'}
processed_data = process_json(json_data)
print(processed_data)