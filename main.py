from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello from Render!</h1><p>Python test app is running successfully.</p>'

@app.route('/health')
def health():
    return {'status': 'healthy', 'message': 'App is running'}

@app.route('/api/data')
def get_data():
    return {
        'users': [
            {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
            {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'}
        ],
        'total': 2,
        'timestamp': '2025-01-01T12:00:00Z'
    }

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)