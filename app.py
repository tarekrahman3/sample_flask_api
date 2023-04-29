from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api', methods=['GET'])
def get_data():
    data = {
        'id': 1,
        'name': 'John Doe',
        'age': 30,
        'email': 'johndoe@example.com'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
