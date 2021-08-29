from flask import Flask, render_template, request

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/echo/')
def echo():
    kwargs = {}
    kwargs['thing'] = request.args.get('thing')
    kwargs['place'] = request.args.get('place')
    return render_template('flask3.html', **kwargs)

app.run(host='localhost', port=8000, debug=True)


