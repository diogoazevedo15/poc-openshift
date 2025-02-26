from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello from the backend!"})

if __name__ == '__main__':
    # Listen on all interfaces (0.0.0.0) so it's accessible inside the container.
    app.run(host='0.0.0.0', port=8000)
