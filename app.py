# import all objects
import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for
    )
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from pygments.lexer import words
if os.path.exists("env.py"):
    import env 


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

#render index page
@app.route("/")
@app.route("/index")
def index():
    naam = mongo.db.naam.find()
    return render_template("index.html", naam=naam)

@app.route("/update_number")
def update_number(naam_id):
    number = mongo.db.naam.find_one({_id: ObjectId(naam_id)})
    if request.method == "POST":
        naam_dict = {
            "eerstegooi": request.form.get("eerstegooi")
        }
        mongo.db.naam.update({"_id": ObjectId(naam_id)}, naam_dict)
        
    return redirect(url_for("index"))




if __name__=="__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)