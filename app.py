from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["todo_db"]
collection = db["items"]

# Backend API for handling POST request
@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    item_name = request.form.get("itemName")
    item_desc = request.form.get("itemDescription")
    if item_name and item_desc:
        collection.insert_one({
            "itemName": item_name,
            "itemDescription": item_desc
        })
        return "Item submitted successfully!"
    else:
        return "Missing fields", 400

if __name__ == "__main__":
    app.run(debug=True)
