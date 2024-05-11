from flask import Flask, render_template, request, jsonify
from bank import Bank

app = Flask(__name__)
bank = Bank('Ashish',6386352801,581320619988,'3yyyt35',790,1234)  # This line should be removed or adjusted

@app.route('/')
def index():
    return render_template('index.html', bank_name=bank.bank_name)

@app.route('/create_account', methods=['POST'])
def create_account():
    data = request.get_json()
    name = data.get('name')
    mno = data.get('mno')
    pan = data.get('pan')
    initial_deposit = float(data.get('initial_deposit'))
    pin = data.get('pin')

    # Instantiate Bank class with account details
    new_account_message = Bank.create_account(name, mno, pan, initial_deposit, pin)
    return jsonify({'message': new_account_message})

@app.route('/check_balance', methods=['POST'])
def check_balance():
    data = request.get_json()
    accno = int(data.get('accno'))
    pin = data.get('pin')

    # Get account instance from Bank.accounts list
    account = bank.accounts[accno - 1]  # Assuming accno is 1-based index
    if account.validate_pin(pin):
        current_balance = account.check_balance()
        return jsonify({'message': f'Current balance: {current_balance}'})
    else:
        return jsonify({'message': 'Incorrect PIN.'}), 403

@app.route('/withdraw', methods=['POST'])
def withdraw():
    data = request.get_json()
    accno = int(data.get('accno'))
    amount = float(data.get('amount'))
    pin = data.get('pin')

    # Get account instance from Bank.accounts list
    account = bank.accounts[accno - 1]  # Assuming accno is 1-based index
    if account.validate_pin(pin):
        withdrawal_message = account.withdraw(amount)
        return jsonify({'message': withdrawal_message})
    else:
        return jsonify({'message': 'Incorrect PIN.'}), 403

@app.route('/deposit', methods=['POST'])
def deposit():
    data = request.get_json()
    accno = int(data.get('accno'))
    amount = float(data.get('amount'))
    pin = data.get('pin')

    # Get account instance from Bank.accounts list
    account = bank.accounts[accno - 1]  # Assuming accno is 1-based index
    if account.validate_pin(pin):
        deposit_message = account.deposit(amount)
        return jsonify({'message': deposit_message})
    else:
        return jsonify({'message': 'Incorrect PIN.'}), 403

@app.route('/change_pin', methods=['POST'])
def change_pin():
    data = request.get_json()
    accno = int(data.get('accno'))
    old_pin = data.get('old_pin')
    new_pin = data.get('new_pin')

    # Get account instance from Bank.accounts list
    account = bank.accounts[accno - 1]  # Assuming accno is 1-based index
    if account.validate_pin(old_pin):
        change_pin_message = account.change_pin(old_pin, new_pin)
        return jsonify({'message': change_pin_message})
    else:
        return jsonify({'message': 'Incorrect old PIN.'}), 403

if __name__ == '__main__':
    app.run(debug=True)
