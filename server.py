from flask import Flask, request
import json
from config import db

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.get("/test")
def test():
    return "This is a test endpoint"

@app.get("/home")
def home():
    print("Home endpoint accessed")
    return "Welcome to home page"



@app.get("/users")
def get_users():
    return {"users": ["Alice", "Bob", "Charlie"]}

@app.get("/api/about")
def about():
    print("About endpoint accessed")
    name = {"name": "Leo Miranda"}
    return name

@app.get("/api/students")
def students():
    print("About endpoint accessed")
    student_names = ["Jeffrey", "George", "Nar", "Raefel", "Isai", "Eric"]
    return student_names

@app.get("/greet/<name>")
def greet(name):
    print("About endpoint accessed")
    # return "Hello " + name
    return f"Hello {name} {5+5}"

products = []

@app.get("/api/products")
def get_products():
    cursor = db.products.find({})
    for prod in cursor:
        products.append(fix_id(prod))
    return json.dumps(products)

def fix_id(obj):
    obj["_id"] = str(obj["_id"])
    return obj

@app.post("/api/products")
def post_products():
    item = request.get_json()
    print()
    


    #mock save
    #products.append(item)
    db.products.insert_one(item)
    print(item)
    return json.dumps(fix_id(item))

#put
@app.put("/api/products/<int:index>")
def put_products(index):
    updated_item =request.get_json()
    if len(products) > index >= 0:
        return json.dumps(updated_item)
    else: 
        return "that index doesnot exist"
    
@app.delete("/api/products/<int:index>")
def delete(index):
    delete_item = request.get_json()
    if 0<= index < len(products):
        delete_item = products.pop(index)
        return json.dumps(delete_item)
    else:
        return "thst index doesnot exist"
    

# patch

@app.patch("/api/products/<int:index>")
def patch_function(index):
    patch_item = request.get_json()
    if 0<= index < len(products):
        products(index).update(patch_item)
        
        return json.dumps(patch_item)
    else:
        return "thst index doesnot exist"






app.run(debug=True, port=8000)