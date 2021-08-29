# flask1.py
from flask import Flask

# Flaskの静的ファイルのフォルダホームディレクトリはstaticであり、そのディレクトリのファイルに対するURLも
# /staticで始まる。そこで、ホームディレクトリを'.'（カレントディレクトリに移動し、URLのプレフィックスも''にして）
# /というURLがindex.htmlファイルにマッピングされるようにする
app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/echo/<thing>')
def echo(thing):
    return thing

app.run(host='localhost', port=9000, debug=True)


