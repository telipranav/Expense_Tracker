from flask import Flask, render_template, request, redirect, session, flash
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "supersecretkey123")

client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017/"))
db = client["expense_tracker"]
col = db["transactions"]
users_col = db["users"]

def login_required(f):
    from functools import wraps
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return redirect("/login")
        return f(*args, **kwargs)
    return wrapper

# ---------- Auth Routes ----------

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username").strip()
        email    = request.form.get("email").strip().lower()
        password = request.form.get("password")

        if users_col.find_one({"email": email}):
            flash("Email already registered. Please login.", "error")
            return redirect("/register")

        users_col.insert_one({
            "username": username,
            "email":    email,
            "password": generate_password_hash(password)
        })
        flash("Account created! Please login.", "success")
        return redirect("/login")

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email    = request.form.get("email").strip().lower()
        password = request.form.get("password")
        user     = users_col.find_one({"email": email})

        if user and check_password_hash(user["password"], password):
            session["user_id"]   = str(user["_id"])
            session["username"]  = user["username"]
            return redirect("/")

        flash("Invalid email or password.", "error")
        return redirect("/login")

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

# ---------- App Routes ----------

@app.route("/")
@login_required
def index():
    transactions  = list(col.find({"user_id": session["user_id"]}).sort("_id", -1))
    total_income  = sum(int(t["amount"]) for t in transactions if t["type"] == "income")
    total_expense = sum(int(t["amount"]) for t in transactions if t["type"] == "expense")
    balance       = total_income - total_expense
    return render_template("index.html",
                           transactions=transactions,
                           balance=balance,
                           total_income=total_income,
                           total_expense=total_expense,
                           username=session["username"])

@app.route("/add", methods=["POST"])
@login_required
def add():
    col.insert_one({
        "user_id": session["user_id"],
        "title":   request.form.get("title"),
        "amount":  request.form.get("amount"),
        "type":    request.form.get("type")
    })
    return redirect("/")

@app.route("/delete/<id>")
@login_required
def delete(id):
    col.delete_one({"_id": ObjectId(id), "user_id": session["user_id"]})
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
