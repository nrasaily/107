from flask import Flask, request
import json
from config import db
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # warning thid disable CORS policy
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
    products = []
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


@app.get("/api/categories")
def get_categories():
    categories = []
    cursor = db.products.find({})
    for prod in cursor:
        cat =prod["category"]
        if cat not in categories:
            categories.append(cat)
    return json.dumps(categories)

@app.get("/api/reports/total")
def get_total():
    total = 0
    cursor = db.products.find({})
    for prod in cursor:
        total += prod["price"]
    return json.dumps(total)

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





@app.post("/api/coupons")
def post_coupon():
    coupon = request.get_json()
    db.coupons.insert_one(coupon)
    return json.dumps(fix_id(coupon))

@app.get("/api/coupons")
def get_coupons():
    results =[]
    cursor = db.coupons.find({})
    for cp in cursor:
        results.append(fix_id(cp))
    return json.dumps(results)


app.run(debug=True, port=8000)