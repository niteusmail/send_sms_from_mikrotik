from flask import Flask, render_template, request
from sms_sender import send_sms 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        phone_number = request.form['phone_number']
        message = request.form['message']
        send_sms(phone_number, message)  
        return f'Отправка SMS на номер {phone_number} с сообщением: {message}'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
