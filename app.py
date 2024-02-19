from flask import Flask, request, jsonify
from flask_oidc import OpenIDConnect
import africastalking
import sqlite3

app = Flask(__name__)
app.config['OIDC_CLIENT_SECRETS'] = 'client_secrets.json'
app.config['OIDC_COOKIE_SECURE'] = False
app.config['OIDC_CALLBACK_ROUTE'] = '/oidc/callback'
app.config['OIDC_SCOPES'] = ['openid', 'email', 'profile']

oidc = OpenIDConnect(app)

africastalking.initialize(username='YOUR_USERNAME', api_key='YOUR_API_KEY')
sms = africastalking.SMS

# Connect to the SQLite database
conn = sqlite3.connect('customer_order.db')
cursor = conn.cursor()

# Create customers table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        code TEXT
    )
""")

# Create orders table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item TEXT,
        amount INTEGER,
        time TIMESTAMP,
        customer_id INTEGER,
        FOREIGN KEY (customer_id) REFERENCES customers (id)
    )
""")
conn.commit()

@app.route('/customers', methods=['POST'])
@oidc.require_login
def create_customer():
    # Logic to create a new customer
    name = request.form.get('name')
    code = request.form.get('code')
    
    cursor.execute("INSERT INTO customers (name, code) VALUES (?, ?)", (name, code))
    conn.commit()
    
    return jsonify({"message": "Customer created successfully"})

@app.route('/orders', methods=['POST'])
@oidc.require_login
def create_order():
    # Logic to create a new order
    item = request.form.get('item')
    amount = request.form.get('amount')
    customer_id = request.form.get('customer_id')
    
    cursor.execute("INSERT INTO orders (item, amount, customer_id) VALUES (?, ?, ?)", (item, amount, customer_id))
    conn.commit()
    
    # Send SMS alert to customer
    phone_number = "+254725847094"  # Replace with customer's phone number
    message = "Your order has been placed successfully"
    response = sms.send(message, [phone_number])
    
    return jsonify({"message": "Order created successfully"})

if __name__ == '__main__':
    app.run()