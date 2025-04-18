from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"

@app.route('/hello')
def hello():
    response = make_response('Hello, World!\n')
    response.status_code = 202
    response.headers['Content-Type'] = 'text/plain'   # or 'application/octet-stream'
    return response

@app.route('/goodbye')
def goodbye():
    return "Goodbye, World!\n"

@app.route('/yurrr', methods=['GET', 'POST' ])
def yurrr():
    if request.method == 'GET':
        return "YOu are using GET method\n"
    elif request.method == 'POST':
        return "You are using POST method\n"
    else:
        return "You will never see this message\n"

@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}!\n"

@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    return f"The sum of {number1} and {number2} is {number1 + number2}.\n"


@app.route('/handle_url_params')
def handle_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args.get('greeting')
        name = request.args.get('name')
    else: 
        return "Some parameters are missing\n"
        

    return f'{greeting} {name}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000 , debug=True)
    