from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)
entries = []

@app.route("/add", methods=["POST"])
def add():
    name = request.form.get("name", "").strip()
    if name:
        entries.append(name)
    return redirect("/")

@app.route("/list")
def list_entries():
    return render_template_string("""
        {% for entry in entries %}
          <li>{{ entry }}</li>
        {% endfor %}
    """, entries=entries)
