from flask import Flask, request, render_template, redirect, url_for, jsonify, json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    who = request.args.get('who', 'World')

    return {"foo": who}


@app.route('/about/')
def about():
    return render_template("about.html")


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/foo', methods=['POST'])
def foo():
    raw_data = request.get_json()
    hum = raw_data['humidity']
    temp = raw_data['temp']

    return 'The humidity {} and temperature {} at your apartment'.format(hum, temp)
    #raw_data = request.json
    #data = json.loads(raw_data)
    # return jsonify(raw_data)


@app.route('/about', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


if __name__ == "__main__":
    app.run(debug=True)
