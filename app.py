from flask import Flask, request, make_response, render_template, redirect, url_for

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    myvalue = "Some value"
    myresult = 10 + 20
    mylist = [1, 2, 3, 4, 5]
    return render_template('index.html', myvalue=myvalue, myresult=myresult, mylist=mylist)

@app.route('/other')
def other():
    some_text = "Hello World"
    return render_template('other.html', some_text=some_text)

@app.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('other'))

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

@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]

@app.template_filter('repeat')
def repreat(s, n=2):
    return s * n

@app.template_filter('alternate_case')
def alternate_case(s):
    return ''.join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s))    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000 , debug=True)
    