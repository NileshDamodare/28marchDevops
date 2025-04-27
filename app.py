from flask import request
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["todo_db"]
collection = db["items"]

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
