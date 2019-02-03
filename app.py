from flask import Flask, render_template, send_from_directory, request
import os
import scraper

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return "Hello Anumeha"

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, 'client')
app = Flask(__name__,
            template_folder=template_path,
            static_url_path='', 
            static_folder='client/static')

@app.route("/")
def index():
    # return "Hello"
    return render_template("index.html")


@app.route("/post")
def post():
    # return "Hello"
    return render_template("post.html")


@app.route("/category")
def category():
    # return "Hello"
    return render_template("category.html")

@app.route('/js/<path:path>')
def send_js(path):
    print(path)
    return send_from_directory(os.path.join(app.static_folder,'js'), path)


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory(os.path.join(app.static_folder,'css'), path)


@app.route('/search', methods=['POST'])
def search():
    print(request.form)

if __name__ == '__main__':
   app.run(debug=True)