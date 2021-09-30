from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from passlib.hash import sha256_crypt
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/ecommerce'
db = SQLAlchemy(app)

class Customer(db.Model):
    __tablename__ = 'customer'

    id = db.Column(db.Integer, primary_key=True)
    username  = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    postal_code = db.Column(db.String(255), nullable=True)
    gender = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.Date, nullable=False)

    def __init__(self, id, username, password, first_name, last_name, postal_code, gender,created_at ):
        self.id = id
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.postal_code = postal_code
        self.gender = gender
        self.created_at = created_at 

    def json(self):
        return {"id": self.id, "username": self.username,  "first_name": self.first_name, "last_name": self.last_name, "postal_code":self.postal_code, "gender":self.gender, "created_at": self.created_at}

@app.route('/customer', methods=['GET'])
def get_all():
	return jsonify({"customer": [customer.json() for customer in Customer.query.all()]})

@app.route('/login', methods=["POST"])
def authenticate():
    data = request.get_json()
    username = data['username']
    password = data['password']


    customer = Customer.query.filter_by(username=username).first()

    if customer:
        if password == customer.password :
            username = customer.username
            return jsonify({"username":username}), 201

    return jsonify({"message": "Invalid username or password."}), 404

@app.route("/create", methods=['POST'])
def createProfile():
    data = request.get_json()
    username = data['username']
    password=data['password']
    first_name= data['first_name']
    last_name= data['last_name']
    postal_code=data['postal_code']
    gender = data['gender']
    
    if (Customer.query.filter_by(username=username).first()):
        return jsonify({"message": "Username '{}' already exists.".format(username)}), 400

    customer = Customer(1,username,password,first_name,last_name,postal_code,gender,created_at= datetime.datetime.now())

    try:
        db.session.add(customer)
        db.session.commit()
    except:
        return jsonify({"message": "An error occurred creating profile."}), 500

    return jsonify(customer.json()), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6500, debug=True)