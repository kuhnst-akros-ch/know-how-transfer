import os
import psycopg2
import time
from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

conn_args = dict(
    host=os.environ["DB_HOST"],
    dbname=os.environ["DB_NAME"],
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"],
)

@app.route("/add", methods=["POST"])
def add():
    name = request.form.get("name", "").strip()
    if name:
        with psycopg2.connect(**conn_args) as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO entries (name) VALUES (%s)", (name,))
                conn.commit()
    return redirect("/")

@app.route("/list")
def list_entries():
    with psycopg2.connect(**conn_args) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT name FROM entries")
            rows = cur.fetchall()
    return render_template_string("".join(f"<li>{row[0]}</li>" for row in rows))

def init_db():
    for i in range(10):  # Retry up to 10 times (1 second apart)
        try:
            with psycopg2.connect(**conn_args) as conn:
                with conn.cursor() as cur:
                    cur.execute("CREATE TABLE IF NOT EXISTS entries (name TEXT NOT NULL)")
                    conn.commit()
            print("✅ Database connection successful.")
            return
        except psycopg2.OperationalError as e:
            print(f"❌ Database not ready ({i + 1}/10): {e}")
            time.sleep(1)
    raise RuntimeError("Database not available after 10 seconds")

init_db()