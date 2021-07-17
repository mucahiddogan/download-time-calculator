import speedtest
from flask import Flask, render_template, request

app = Flask(__name__)
servers = []
threads = None

def get_speed():
    s = speedtest.Speedtest()
    return s.download(threads=threads)/8000000

@app.route("/") 
def index():
    return render_template("main.html")

@app.route("/sonuc", methods=['POST', 'GET']) 
def sonuc():
    if request.method == 'POST':
        boyut = request.form.get('boyut') 
    total = int(float(boyut)*1024/float(get_speed())/60)
    return render_template("sonuc.html", total=total)

app.run(debug =True)
