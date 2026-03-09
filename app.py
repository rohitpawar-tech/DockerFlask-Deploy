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
<style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background-color: #f0f2f5;
        color: #333;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
    }
    .container {
        background-color: white;
        padding: 40px;
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        text-align: center;
        max-width: 500px;
        width: 100%;
    }
    h1 {
            color: #2c3e50;
        margin-bottom: 10px;
    }
    p {
        color: #666;
        line-height: 1.6;
    }
    .nav-buttons {
        margin-top: 30px;
    }
    .btn {
        display: inline-block;
        padding: 10px 20px;
        margin: 5px;
        text-decoration: none;
        background-color: #007bff;
        color: white;
        border-radius: 5px;
        transition: background-color 0.3s;
        font-weight: bold;
    }
    .btn:hover {
        background-color: #0056b3;
    }
    .btn-secondary {
        background-color: #6c757d;
    }
    .btn-secondary:hover {
        background-color: #545b62;
    }
    .health-badge {
        display: inline-block;
        padding: 5px 10px;
        background-color: #28a745;
        color: white;
        border-radius: 20px;
        font-size: 0.9em;
        margin-top: 10px;
    }
</style>
"""
# 1. Home Page Route
@app.route('/')
def home():
    logger.info("Home page accessed.")
    
    # We inject the CSS_STYLES variable into the HTML string
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Home</title>
        {CSS_STYLES}
    </head>
    <body>
        <div class="container">
            <h1>Welcome! 🐳</h1>
            <p>This is a Dockerized Python Flask Application.</p>
            <div class="nav-buttons">
                <a href="/about" class="btn">About Project</a>
                <a href="/health" class="btn btn-secondary">Health Check</a>
            </div>
        </div>
    </body>
    </html>
    """
    return html_content

# 2. About Page Route
@app.route('/about')
def about():
    logger.info("About page accessed.")
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>About</title>
        {CSS_STYLES}
    </head>
    <body>
        <div class="container">
            <h1>About This Project</h1>
            <p>This project demonstrates containerization.</p>
            <p>We used Python, Flask, and Docker to create a portable web application.</p>
            <div class="nav-buttons">
                <a href="/" class="btn">Go Back Home</a>
            </div>
        </div>
    </body>
    </html>
    """
    return html_content
# 3. Health Check API
# Note: We return JSON here as it is standard for API monitoring tools.
# If you open this in a browser, it will look like raw text data.
@app.route('/health')
def health():
    logger.info("Health check performed.")
    return jsonify({"status": "healthy", "message": "System is operational"}), 200
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    # debug=False is better for production/docker logs
    app.run(host='0.0.0.0', port=port, debug=False)
