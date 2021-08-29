from flask import Flask, render_template, request

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/echo/')
def echo():
    thing = request.args.get('thing')
    place = request.args.get('place')
    return render_template('flask3.html', thing=thing, place=place)

app.run(host='localhost', port=8000, debug=True)


