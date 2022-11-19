from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template("index_html.html")

@app.route('/about')
def index():
    return render_template("about.html")

@app.route('/user/<string:user_name>/<int:user_id>')
def user(user_name, user_id):
    return f'User page {user_name} {user_id}'

if __name__ == '__main__':
    app.run(debug=True)
