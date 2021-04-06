from flask import *
from flask_pymongo import PyMongo
from bson.json_util import dumps

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://root:password@mongo:27017/restdb?authSource=admin'

mongo = PyMongo(app)

@app.route('/greeting')
def greeting():
    name = request.args['name']
    return render_template('greeting.html', name=name)

@app.route('/login')
def signin():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login/validate', methods=['POST'])
def validate():
    error = None
    user = mongo.db.users
    username = request.form.get('uname')
    password = request.form.get('psw')
    print(username)
    print(password)
    # return redirect(url_for('home', name=username))
    user_details = user.find_one(
        {
            'username': username
        },
        {
            '_id': 0
        }
    )
    return jsonify(user_details)

@app.route('/handle_data', methods=['POST'])
def handle_data():
    user = mongo.db.users
    details = {
        'name': request.form.get('name'),
        'email': request.form.get('email'),
        'mobile': request.form.get('num'),
        'username': request.form.get('uname'),
        'password': request.form.get('psw')
    }
    user.insert(details)
    return redirect(url_for('index'))

@app.route('/home/<name>')
def home(name):
    return render_template('home.html', name=name)
    
if __name__ == "__main__":
    app.run(debug=True)