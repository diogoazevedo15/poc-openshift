import requests
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    try:
        response = requests.get('http://backend-service:80/data', timeout=2)
        data = response.json()
        message = data.get('message', 'No message found')
    except Exception as e:
        message = f"Could not reach backend. Error: {e}"

    html = f"""
    <html>
    <head><title>Frontend</title></head>
    <body>
      <h1>Frontend</h1>
      <p>Backend says: <strong>{message}</strong></p>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8011)
