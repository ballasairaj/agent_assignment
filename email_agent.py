
import re
from typing import Dict

def extract_sender(email_content: str)-> str:
    """Extract sender's email address from the email content."""
    match = re.search(r'From:\s*(.*?)(\r\n|\n)', email_content)
    return match.group(1).strip() if match else "Unknown"