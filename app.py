from flask import Flask, request
from flask import render_template

from google.oauth2 import service_account
import googleapiclient.discovery


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
DOCUMENT_ID = '1TmjDLbyQjlQoFDhmNIkieH0wJY16eG4BtOcZsi4gq_8'


def t(f):
    credentials = service_account.Credentials.from_service_account_file(
        f,
        scopes=[
            "https://www.googleapis.com/auth/calendar",
            "https://www.googleapis.com/auth/calendar.events",
            "https://www.googleapis.com/auth/spreadsheets.currentonly",
            "https://www.googleapis.com/auth/spreadsheets",
        ],
    )
    sheet_service = googleapiclient.discovery.build("sheets", "v4", credentials=credentials)
    r=sheet_service.spreadsheets().get(spreadsheetId=DOCUMENT_ID)
    response = r.execute()
    print(response)
    return response

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def handle_upload():
    print('file ..')
    file = request.files['file']
    file.save('./s.json')
    print(dir(file))
    
    return {'message':  t('./s.json')}

if __name__ == '__main__':
    app.run()
