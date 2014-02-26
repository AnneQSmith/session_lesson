from flask import Flask, render_template, request, redirect, session, url_for, flash
import model

app = Flask(__name__)
app.secret_key = "shhhhthisisasecret"

@app.route("/")
def index():
    if session.get("username"):
        print "User %s is logged in!!!!!! YAY!" %session["username"]
        return redirect(url_for("loggedin"))
    else:
        return render_template("index.html")

@app.route("/loggedin")
def loggedin():
    session.clear()
    return redirect(url_for("index"))

@app.route("/", methods=["POST"])
def process_login():
    username = request.form.get("username")
    password = request.form.get("password")
    print "Im working yay!", username, password
    model.connect_to_db()
    user_id = model.authenticate(username, password)
    if user_id > 0:
        flash("User authenticated")
        print (" model authenticated valid password"), 
        session['username'] = username
    else:
        flash("Invalid credentials")
        print ("model said no go on password")
    model.CONN.close()
    return redirect(url_for("index"))
  #  return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug = True)
