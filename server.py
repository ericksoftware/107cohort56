from flask import Flask, render_template, request
import json

app = Flask(__name__)

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
    print("Products endpoint accessed")
    return json.dumps(products)

@app.post("/api/products")
def post_products():
    item = request.get_json()
    print("Item received:", item)
    products.append(item)
    return json.dumps(item)

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
    
app.run(debug=True, port=8000)

