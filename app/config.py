"""
Configuration settings for PatchContext.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# ----------------------------
# GitHub Repository
# ----------------------------
OWNER = "fastapi"
REPO = "fastapi"

REPO_URL = f"https://github.com/{OWNER}/{REPO}"
API_URL = f"https://api.github.com/repos/{OWNER}/{REPO}"

# ----------------------------
# Authentication
# ----------------------------
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# ----------------------------
# Request Configuration
# ----------------------------
HEADERS = {
    "Accept": "application/vnd.github+json"
}

if GITHUB_TOKEN:
    HEADERS["Authorization"] = f"Bearer {GITHUB_TOKEN}"

# ----------------------------
# Data Paths
# ----------------------------
RAW_DATA = "data/raw"
PROCESSED_DATA = "data/processed"
VECTOR_DB = "vectorstore"
