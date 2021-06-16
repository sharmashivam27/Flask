from flask import Flask,redirect,url_for,render_template
from flask.helpers import send_file

app=Flask(__name__)
@app.route("/home")
@app.route("/")
def home():
 return  render_template("index.html")

@app.route("/content")
def content_():
    return render_template("content.html")

@app.route("/download")
def download():
    p=r"C:\Users\Sharma\Desktop\Flask\Files\Ultrasonic.ino"
    return send_file(p,as_attachment=True)
if __name__=="__main__":
    app.run(debug=True)
