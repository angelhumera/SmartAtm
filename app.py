from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Read balance
def get_balance():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return data['balance']

# Update balance
def update_balance(amount):
    with open('data.json', 'r+') as f:
        data = json.load(f)
        data['balance'] -= amount
        f.seek(0)
        json.dump(data, f)
        f.truncate()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/balance')
def balance():
    bal = get_balance()
    return render_template('balance.html', balance=bal)

@app.route('/withdraw', methods=['POST'])
def withdraw():
    amount = int(request.form['amount'])
    update_balance(amount)
    return redirect(url_for('balance'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
