from flask import *
from training import *
app=Flask(__name__)

@app.route("/")# This is for test 
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/result",methods=['POST','GET'])
def result():
    out=request.form.to_dict()
    url=out["url"]
    if check(url):
        return render_template("phishing.html")
    return render_template("legitimate.html",url='https:/'+url)


if __name__ == '__main__':
    app.run(debug=True,port=5000)
