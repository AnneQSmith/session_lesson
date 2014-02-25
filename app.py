from flask import Flask, render_template, request, redirect, session, url_for, flash
import model

app = Flask(__name__)
app.secret_key = "shhhhthisisasecret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def process_login():
    username = request.form.get("username")
    password = request.form.get("password")
    print "Im working yay!", username, password

    if model.authenticate(username, password):
        flash("User authenticated")
        print (" model authenticated valid password")
    else:
        flash("Invalid credentials")
        print ("model said no go on password")

    return redirect(url_for("index"))
  #  return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug = True)
