from flask import Flask, render_template, request
import json
from config import db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # warning: This disables CORS policy, use with caution

@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'


@app.get('/user')
def user():
    return {"users": ["user1", "user2", "user3"]}

@app.get('/test')
def test():
    return "This is a test endpoint 1.0"

@app.get('/home')
def home():
    return "This is the home page"

@app.get('/api/about')
def about():
    print("About endpoint accessed")
    name = "John Doe"
    return name 

@app.get('/api/students')
def students():
    print("Students endpoint accessed")
    students_list = ["erick", "jeffrey", "george", "rafa", "isai", "nar"]
    return students_list

@app.get("/greet/<name>")
def greet(name):
    print("Greet endpoint accessed")
    return "Hello " + name

@app.get("/contact")
def contact_api():
    print("Contact API endpoint accessed")
    name = "John Doe"
    return render_template("contact.html" , name=name)

products = []
@app.get("/api/products")
def get_products():
    products = []  # Move inside function to avoid global variable issues
    cursor = db.products.find()
    for product in cursor:
        products.append(fix_id(product))
    print("Products endpoint accessed")
    return json.dumps(products)  # Add this return statement

def fix_id(obj):
    obj["_id"] = str(obj["_id"])
    return obj

@app.post("/api/products")
def post_products():
    item = request.get_json()
    print("Item received:", item)
    # products.append(item)
    db.products.insert_one(item)
    return json.dumps(fix_id(item))

@app.get("/api/categories")
def get_categories():
    categories = []
    cursor = db.products.find({})
    for product in cursor:
        categories.append(product["category"])
    categories = list(set(categories))
    print("Categories endpoint accessed")
    return json.dumps(categories)

@app.get("/api/reports/total")
def get_reports_total():
    total = 0
    cursor = db.products.find({})
    for product in cursor:
        total += product["price"]
    print("Total endpoint accessed")
    return json.dumps(total)

@app.put("/api/products/<int:index>")
def put_products(index):
    upload_item = request.get_json()
    if len(products) > index >= 0:
        products[index] = upload_item
        return json.dumps(upload_item)
    else:
        return "Index out of range", 404
    
@app.delete("/api/products/<int:index>")
def delete_products(index):
    if len(products) > index >= 0:
        deleted_item = products.pop(index)
        return json.dumps(deleted_item)
    else:
        return "Index out of range", 404
    
#patch
@app.patch("/api/products/<int:index>")
def patch_products(index):
    if len(products) > index >= 0:
        item = request.get_json()
        products[index].update(item)
        return json.dumps(products[index])
    else:
        return "Index out of range", 404



def hello():
    print("Hello from Python")


hello()    

def test_1():
    name = "Rafael"
    last = "Cabrera"

    print(name + " " + last)

test_1()

def test_if(age):
    if age < 21:
        print("You can not drink")
    else:
        print("Please, have a beer")

def test_for():
    nums = [2,4,3,167,34,73,74,13,67,8]
    total = 0
    for num in nums:
        total += num

    print("The total sum is: " + str(total))    

def test_dict():
    dog = { 
        "name" : "Lola", 
        "age":3
    }

    print(dog)
    print(dog["name"])

def test_list():
    products = [
        {"title": "Wireless Mouse", "price": 25.99, "category": "Electronics"},
        {"title": "Yoga Mat", "price": 19.99, "category": "Fitness"},
        {"title": "Coffee Maker", "price": 49.99, "category": "Home Appliances"},
        {"title": "Bluetooth Headphones", "price": 79.99, "category": "Electronics"},
        {"title": "Running Shoes", "price": 59.99, "category": "Footwear"},
        {"title": "Desk Lamp", "price": 22.50, "category": "Office Supplies"}
    ]

    for prod in products:
        print(prod["title"])
    
    total = 0
    for prod in products:
        total += prod["price"]

    print("Your total is: " + str(total))
test_if(18)   
test_if(21)   

test_for()

test_dict()

test_list()






#####################################################
#########            API COUPONS          ###########
#####################################################


@app.post("/api/coupons")
def post_coupons():
    coupon = request.get_json()
    print("Coupon received:", coupon)
    db.coupons.insert_one(coupon)
    return json.dumps(fix_id(coupon))

@app.get("/api/coupons")
def get_coupons():
    coupons = []
    cursor = db.coupons.find()
    for coupon in cursor:
        coupons.append(fix_id(coupon))
    print("Coupons endpoint accessed")
    return json.dumps(coupons)

    
app.run(debug=True, port=8000)

