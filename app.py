from flask import Flask, render_template

app = Flask(__name__)

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


@app.route('/')
def hello_world():  # put application's code here
   user = User('John', 'xx@qq.com')
    return render_template('index.html')


@app.route('/blog/<blog_id>')
def blog_detail(blog_id):
    return render_template("blog_detail.html", blog_id=blog_id)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
