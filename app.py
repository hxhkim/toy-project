from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# SQLite DB 초기화 함수
def init_db():
    with sqlite3.connect("app.db") as conn:
        # 사용자 데이터를 저장할 테이블 생성
        conn.execute('''CREATE TABLE IF NOT EXISTS user_data (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            email TEXT)''')
    print("Database initialized")

# 데이터베이스에 사용자 데이터를 저장하는 함수
def save_to_db(name, email):
    with sqlite3.connect("app.db") as conn:
        conn.execute("INSERT INTO user_data (name, email) VALUES (?, ?)", (name, email))
    print(f"Saved data: {name}, {email}")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        
        # 폼에서 받은 데이터 DB에 저장
        save_to_db(name, email)
        
        return "Form submitted and data saved successfully!"
    
    return render_template("index.html")

if __name__ == "__main__":
    init_db()  # DB 초기화
    app.run(debug=True)
