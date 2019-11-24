from flask import Flask
app = Flask(__name__)
def fibonnacci (n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonnacci(n-1) + fibonnacci(n-2)

@app.route("/")
def send_number():
    try:
        return str(fibonnacci(int(request.args['n'])))
    except ValueError:
        return "Plese use proper integer in input"