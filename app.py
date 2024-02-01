from flask import Flask, jsonify, request
import mysql.connector as mysql
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

DB_USERNAME = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')



# try:
#     conn = mysql.connect(
#         host=DB_HOST,
#         database=DB_NAME,
#         user=DB_USERNAME,
#         password=DB_PASSWORD
#     )
#     print("Successfully connected to database")
# except Error as e:
#     print("Error while connecting to database", e)

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to Artist API"

@app.route('/api/v1/artists')
def get_artists():
    conn = mysql.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USERNAME,
        password=DB_PASSWORD
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM artist")
    rows = cursor.fetchall()
    return jsonify(rows)

@app.route('/api/v1/artists/id', methods=['GET'])
def get_artist_by_id():
    artist_id = request.args.get('id')
    conn = mysql.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USERNAME,
        password=DB_PASSWORD
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM artist WHERE nconst = %s", (artist_id,))
    rows = cursor.fetchall()
    return jsonify(rows)

@app.route('/api/v1/artists/name', methods=['GET'])
def get_artist_by_name():
    artist_name = request.args.get('name')
    conn = mysql.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USERNAME,
        password=DB_PASSWORD
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM artist WHERE primaryName LIKE %s", (artist_name,))
    rows = cursor.fetchall()
    return jsonify(rows)

@app.route('/api/v1/artists/knownForTitles', methods=['GET'])
def get_artist_by_title():
    title = request.args.get('title')
    conn = mysql.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USERNAME,
        password=DB_PASSWORD
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM artist WHERE knownForTitles LIKE %s", (title,))
    rows = cursor.fetchall()
    return jsonify(rows)

@app.route('/api/v1/artists/deathYear', methods=['GET'])
def get_artist_by_death_year():
    death_year = request.args.get('deathYear')
    conn = mysql.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USERNAME,
        password=DB_PASSWORD
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM artist WHERE deathYear = %s", (death_year,))
    rows = cursor.fetchall()
    return jsonify(rows)

@app.route('/api/v1/artists/birthYear', methods=['GET'])
def get_artist_by_birth_year():
    birth_year = request.args.get('birthYear')
    conn = mysql.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USERNAME,
        password=DB_PASSWORD
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM artist WHERE birthYear = %s", (birth_year,))
    rows = cursor.fetchall()
    return jsonify(rows)

@app.route('/api/v1/artists', methods=['POST'])
def create_artist():
    data = request.get_json()
    conn = mysql.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USERNAME,
        password=DB_PASSWORD
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("INSERT INTO artist (nconst, primaryName, birthYear, deathYear, primaryProfession, knownForTitles) VALUES (%s, %s, %s, %s, %s, %s)", (data['nconst'], data['primaryName'], data['birthYear'], data['deathYear'], data['primaryProfession'], data['knownForTitles']))
    conn.commit()
    return jsonify(data)

@app.route('/api/v1/artists', methods=['PUT'])
def update_artist():
    data = request.get_json()
    conn = mysql.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USERNAME,
        password=DB_PASSWORD
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("UPDATE artist SET primaryName = %s, birthYear = %s, deathYear = %s, primaryProfession = %s, knownForTitles = %s WHERE nconst = %s", (data['primaryName'], data['birthYear'], data['deathYear'], data['primaryProfession'], data['knownForTitles'], data['nconst']))
    conn.commit()
    return jsonify(data)

@app.route('/api/v1/artists', methods=['DELETE'])
def delete_artist():
    data = request.get_json()
    conn = mysql.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USERNAME,
        password=DB_PASSWORD
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("DELETE FROM artist WHERE nconst = %s", (data['nconst'],))
    conn.commit()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)



