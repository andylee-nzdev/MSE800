from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, Flask!"

@app.route("/bye")
def bye():
    return "<p>Goodbye Flask!</p>"

@app.route("/user/<username>")
def show_user_profile(username):
    return f"<p>Hello, {username} is learning Flask!</p>"

@app.route("/<name>/<int:number>")
def learn(name, number):
    return f"{name}: is learning Flask! She wakes up at {number} every day."

if __name__ == "__main__":
    app.run(debug=True)
