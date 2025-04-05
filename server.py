from flask import Flask, render_template

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

app.run(debug=True, port=8000)

