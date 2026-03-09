# app.py
from flask import Flask, jsonify
import logging
import os
app = Flask(__name__)

# Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
# --- CSS STYLES ---
# We define the CSS as a string to keep it simple for this beginner project.
# In a larger app, this would go into a static/css/style.css file.
CSS_STYLES = """
