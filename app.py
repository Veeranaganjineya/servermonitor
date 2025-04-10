from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz
import getpass

app = Flask(__name__)

@app.route('/htop')
def htop():
    full_name = "Yelampalli Veeranagnajineya Reddy"  # Replace with your actual name
    username = getpass.getuser()
    
    # Get server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    # Get `top` command output
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode()
    except Exception as e:
        top_output = str(e)

    html = f"""
    <h1>/htop Output</h1>
    <p><b>Name:</b> {full_name}</p>
    <p><b>Username:</b> {username}</p>
    <p><b>Server Time (IST):</b> {server_time}</p>
    <pre>{top_output}</pre>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
