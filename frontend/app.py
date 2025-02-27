import requests
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    try:
        # URL uses backend’s service name in the cluster: "backend-service" (we'll define it later)
        response = requests.get('http://poc-openshift-backend:8000/data', timeout=2)
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
    app.run(host='0.0.0.0', port=8001)
