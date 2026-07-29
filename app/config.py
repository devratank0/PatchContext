"""
PatchContext Configuration
--------------------------
Stores project settings and environment variables.
"""

from pathlib import Path
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# -----------------------------
# Project Paths
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
VECTORSTORE_DIR = BASE_DIR / "vectorstore"

# -----------------------------
# GitHub Repository
# -----------------------------
GITHUB_OWNER = "fastapi"
GITHUB_REPO = "fastapi"

# -----------------------------
# API Keys
# -----------------------------
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# -----------------------------
# GitHub API
# -----------------------------
GITHUB_API_BASE = "https://api.github.com"

HEADERS = {
    "Accept": "application/vnd.github+json"
}

if GITHUB_TOKEN:
    HEADERS["Authorization"] = f"Bearer {GITHUB_TOKEN}"