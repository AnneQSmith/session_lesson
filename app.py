from flask import Flask, render_template, request, redirect, session, url_for, flash
import model

app = Flask(__name__)
app.secret_key = "shhhhthisisasecret"

@app.route("/")
def index():
    if session.get("username"):
        print "User %s is logged in!!!!!! YAY!" %session["username"]
        return redirect(url_for("logged_out"))
    else:
        return render_template("index.html")

@app.route("/logged_out")
def logged_out():
    session.clear()
    return redirect(url_for("index"))

@app.route("/", methods=["POST"])
def process_login():
    username = request.form.get("username")
    password = request.form.get("password")
    model.connect_to_db()
    user_id = model.authenticate(username, password)
    if user_id > 0:
        flash("User authenticated")
        print (" model authenticated valid password"), 
        session['user_id'] = user_id
        print session
    else:
        flash("Invalid credentials")
        print ("model said no go on password")
    model.CONN.close()
    return redirect(url_for("index"))
  #  return render_template("login.html")

@app.route("/register")
def register():
    print ("We are rendering register.html")
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def create_account():
    username = request.form.get("username")
    password1 = request.form.get("password")
    password2 = request.form.get("password_verify")

    print "top of create account", username,password1,password2
    
    if len(username) < 1:
        flash("username must be longer than 0 characters")
        return redirect(url_for("register"))

    if password1 != password2:
        flash ("passwords must match, try again")
        return redirect(url_for("register"))

    
    else:
        print "I'm connecting to the database cause the passwords matched!"
        model.connect_to_db()
        if model.user_exists(username):
            flash ("That user already exists")
        else:
            model.create_new_account(username, password1)
            flash ("Welcome")
            
        model.CONN.close()

        return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug = True)

    #return render_template("register.html")
