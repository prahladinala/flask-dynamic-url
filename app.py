from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def welcome():
    return "Hello Prahlad Inala"


@app.route('/pass/<int:score>')
def success(score):
    return "<h2 style='color: green'>The Person has passed and the marks is " + str(score) + "</h2>"
# http://127.0.0.1:5000/pass/50


@app.route('/fail/<int:score>')
def fail(score):
    return "<h2 style='color: red'>The Person has failed and the marks is " + str(score) + "</h2>"
# http://127.0.0.1:5000/fail/30


# @app.route('/results/<int:score>')
# def results(score):
#     result = ""
#     if score < 50:
#         result = 'fail'
#     else:
#         result = 'pass'
#     return result

# http://127.0.0.1:5000/results/55
# pass
# http://127.0.0.1:5000/results/30
# fail

@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks < 50:
        result = 'fail'
    else:
        result = 'success'
    return redirect(url_for(result, score=marks))


if __name__ == "__main__":
    app.run(debug=True)
