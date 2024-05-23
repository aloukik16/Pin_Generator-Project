from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

pin_holder_list = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_pin', methods=['POST'])
def generate_pin():
    data = request.get_json()
    digit_count = int(data['digit_count'])
    repudiation = data['repudiation'] == 'yes'
    zero = data['zero'] == 'yes'

    def generate_unique_pin(length, allow_repudiation, allow_zero):
        while True:
            if allow_zero:
                pin = ''.join(random.choices('0123456789', k=length))
            else:
                pin = ''.join(random.choices('123456789', k=1) + random.choices('0123456789', k=length-1))
            if allow_repudiation and len(set(pin)) != length:
                continue
            if pin not in pin_holder_list:
                pin_holder_list.append(pin)
                return pin

    pin = generate_unique_pin(digit_count, repudiation, zero)
    return jsonify(pin=pin)

if __name__ == '__main__':
    app.run(debug=True)
