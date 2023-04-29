from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Success!'

@app.route('/api', methods=['GET'])
def get_data():
    data = {
        'id': 00,
        'name': 'Tarek Rahman',
        'email': 'tarek@example.com'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run()
