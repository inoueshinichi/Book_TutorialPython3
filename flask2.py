from flask import Flask, render_template, request

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/echo/<thing>')
def echo(thing):
    return render_template('flask2.html', thing=thing)

app.run(port=9000, debug=True)

