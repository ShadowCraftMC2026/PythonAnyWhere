import time
from datetime import datetime
from flask import Flask
from threading import Thread

# PROJECT NAME: PythonAnyWhere by Shadow
# DESCRIPTION: 24/7 Real Python Script for any workspace

app = Flask(__name__)

@app.route('/')
def home():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <html>
        <head>
            <title>PythonAnyWhere by Shadow</title>
            <style>
                body {{ font-family: 'Courier New', monospace; background-color: #121212; color: #00ff00; text-align: center; padding-top: 100px; }}
                .container {{ border: 2px solid #00ff00; display: inline-block; padding: 30px; box-shadow: 0 0 15px #00ff00; }}
                h1 {{ font-size: 28px; text-transform: uppercase; }}
                p {{ font-size: 20px; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>PythonAnyWhere by Shadow</h1>
                <p>Status: RUNNING 24/7</p>
                <p>Server Time: {current_time}</p>
            </div>
        </body>
    </html>
    """

def run_web_server():
    # Runs the web endpoint to prevent the host from sleeping
    app.run(host='0.0.0.0', port=8080)

def background_worker():
    # This is your main 24/7 loop where your actual logic goes
    print("[SYSTEM] 24/7 Background Worker Started Successfully.")
    loop_count = 0
    while True:
        loop_count += 1
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"[{current_time}] PythonAnyWhere by Shadow is active. Loop: {loop_count}")
        
        # Put your background task logic here (e.g., data scraping, parsing, etc.)
        
        time.sleep(60) # Sleeps for 1 minute before repeating

if __name__ == '__main__':
    # 1. Start the web server thread
    web_thread = Thread(target=run_web_server)
    web_thread.daemon = True
    web_thread.start()
    
    # 2. Start the infinite 24/7 loop
    background_worker()
