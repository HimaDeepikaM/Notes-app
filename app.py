from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

@app.route('/')
def serve_frontend():
    return send_file('index.html')

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sridurga@7670",
    database="notes_app"
)
cursor = conn.cursor(dictionary=True)

@app.route('/api/add_note', methods=['POST'])
def add_note():
    data = request.get_json()
    cursor.execute("INSERT INTO notes (title, content) VALUES (%s, %s)", (data['title'], data['content']))
    conn.commit()
    return jsonify({'message': 'Note added'})

@app.route('/api/notes', methods=['GET'])
def get_notes():
    cursor.execute("SELECT * FROM notes ORDER BY created_at DESC")
    notes = cursor.fetchall()
    return jsonify(notes)

if __name__ == '__main__':
    app.run(debug=True)
