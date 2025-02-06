from flask import Flask, render_template,request
app = Flask(__name__)

@app.route("/api", methods=['POST'])
def hello():
    name = request.form['name']
    return render_template("hello.html", person=name)

@app.route("/")
def index():
    return render_template("hello.html")

if __name__ == "__main__":
    app.run()

