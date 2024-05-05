import os
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

VALID_API_KEY = "8dab6627008b162e707171789c0c98c5dc5ef82c"

# Define the path to the databases folder
DATABASES_FOLDER = "databases"

# Ensure the databases folder exists, create it if it doesn't
if not os.path.exists(DATABASES_FOLDER):
    os.makedirs(DATABASES_FOLDER)

def validate_api_key(api_key):
    return api_key == VALID_API_KEY

def create_sqlite_db(db_name):
    # Construct the path to the database file in the databases folder
    db_path = os.path.join(DATABASES_FOLDER, f'{db_name}.db')
    
    # Connect to the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            email TEXT,
            password TEXT,
            pro_status INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def validate_user(username, password, db_name):
    db_path = os.path.join(DATABASES_FOLDER, f'{db_name}.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None

def return_pro_status(username, db_name):
    db_path = os.path.join(DATABASES_FOLDER, f'{db_name}.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT pro_status FROM users WHERE username=?', (username,))
    pro_status = cursor.fetchone()
    conn.close()
    return pro_status

def add_user(username, email, password, pro_status, db_name):
    db_path = os.path.join(DATABASES_FOLDER, f'{db_name}.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, email, password, pro_status) VALUES (?, ?, ?, ?)', (username, email, password, pro_status))
    conn.commit()
    conn.close()

def delete_user(username, db_name):
    db_path = os.path.join(DATABASES_FOLDER, f'{db_name}.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE username=?', (username,))
    conn.commit()
    conn.close()

@app.route('/create_db', methods=['POST'])
def create_db():
    api_key = request.headers.get('X-API-Key')
    if not api_key or not validate_api_key(api_key):
        return jsonify({"error": "Unauthorized"}), 401
    
    db_name = request.json['db_name']
    create_sqlite_db(db_name)
    return jsonify({"message": f"Database {db_name}.db created successfully!"})

@app.route('/return_pro_status', methods=['POST'])
def return_pro_status_route():
    api_key = request.headers.get('X-API-Key')
    if not api_key or not validate_api_key(api_key):
        return jsonify({"error": "Unauthorized"}), 401
    
    db_name = request.json['db_name']
    username = request.json['username']
    return jsonify({"pro_status": return_pro_status(username, db_name)})

@app.route('/validate_user', methods=['POST'])
def validate_user_route():
    api_key = request.headers.get('X-API-Key')
    if not api_key or not validate_api_key(api_key):
        return jsonify({"error": "Unauthorized"}), 401
    
    db_name = request.json['db_name']
    username = request.json['username']
    password = request.json['password']
    
    if validate_user(username, password, db_name):
        return jsonify({"message": "User validated successfully"})
    else:
        return jsonify({"error": "Invalid username or password"}), 401

@app.route('/add_user', methods=['POST'])
def add_user_route():
    api_key = request.headers.get('X-API-Key')
    if not api_key or not validate_api_key(api_key):
        return jsonify({"error": "Unauthorized"}), 401
    
    db_name = request.json['db_name']
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    pro_status = request.json['pro_status']
    
    add_user(username, email, password, pro_status, db_name)
    return jsonify({"message": "User added successfully"})

@app.route('/delete_user', methods=['POST'])
def delete_user_route():
    api_key = request.headers.get('X-API-Key')
    if not api_key or not validate_api_key(api_key):
        return jsonify({"error": "Unauthorized"}), 401
    
    db_name = request.json['db_name']
    username = request.json['username']
    
    delete_user(username, db_name)
    return jsonify({"message": f"User {username} deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
