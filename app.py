
from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def login():
    return render_template("login.html")


@app.route("/upload", methods=["GET", "POST"])
def upload():

    if request.method == "POST":

        files = {
            "audience": request.files.get("audience"),
            "events": request.files.get("events"),
            "landing": request.files.get("landing"),
            "pages": request.files.get("pages"),
            "traffic": request.files.get("traffic"),
            "user_acquisition": request.files.get("user_acquisition")
        }

        for file in files.values():
            if file and file.filename != "":
                file.save(os.path.join(UPLOAD_FOLDER, file.filename))

        return redirect("/dashboard")

    return render_template("upload.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)