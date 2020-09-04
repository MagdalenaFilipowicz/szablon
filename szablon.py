from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/mypage/me")
def hello():
    return render_template("form.html")

@app.route("/message/contact", methods=["POST"])
def post_message():
    return request.form.get("text")
    

app.run()
