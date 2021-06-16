from flask import Flask,redirect,url_for,render_template
from flask.helpers import send_file
from flask_restful import Api,Resource

file={0:r"C:\Users\Sharma\Desktop\Flask\Files\Ultrasonic.ino"}

app=Flask(__name__)
api=Api(app)

class files(Resource):
    def get(self,file_id):
        if file_id in file:
            return send_file(file[file_id],as_attachment=True)
        else:
            return  'File not Found'  

api.add_resource(files,"/download/<int:file_id>")

@app.route("/home")
@app.route("/")
def home():
 return  render_template("index.html")

@app.route("/content")
def content_():
    return render_template("content.html")



if __name__=="__main__":
    app.run(debug=True)
