"""
This module is for setting global variables
"""

import os

BASE_URL = os.getenv("BASE_URL", "http://localhost:1234/v1")       # Url for llm inference endpoint (default value for LM Studio)
