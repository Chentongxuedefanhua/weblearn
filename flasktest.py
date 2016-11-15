from flask import Flask,render_template,request


app = Flask(__name__)


@app.route('/',methods=["POST","GET"])
def index():
    if request.method == 'POST':
        date = request.form.get('reservation')
    return render_template('index.html',date=date)


if __name__ == '__main__':
    app.run()