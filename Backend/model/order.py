from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root123@localhost:3306/ecommerce'
# app.config['SQLALCHEYMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'

db = SQLAlchemy(app)

class Order(db.Model):
    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer)
    status = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)

    
    def __init__(self, id, customer_id, status, created_at):
        self.id = id
        self.customer_id = customer_id
        self.status = status
        self.created_at = created_at

    def json(self):
        return {
            "id":self.id,
            "customer_id":self.customer_id,
            "status": self.status,
            "created_at":self.created_at,
        }

# Methods
# Insert products added into database
@app.route('/create_order', methods=['POST'])
def create_todo():
    data = request.get_json()
    id = data['id']
    customer_id = data['customer_id']
    status = data['status']
    created_at = data['created_at']
    order = Order(id=id, customer_id=customer_id, status=status, created_at=datetime.now())
    db.session.add(order)
    db.session.commit()
    return make_response(jsonify({"response": "Added"}), 200)

# Update an order from Order table
@app.route('/order/<int:id>/update', methods=['POST'])
def update(id):
    order = Order.query.filter_by(id=id).first()
    if order:
        db.session.delete(order)
        db.session.commit()
        data = request.get_json()
        customer_id = data['customer_id']
        status = data['status']
        neworder = Order(id=id, customer_id=customer_id, status=status, created_at=datetime.now())
        db.session.add(neworder)
        db.session.commit()

        return make_response(jsonify({"response": "Added"}), 200)
    return make_response(jsonify({"response": "No such order"}), 200)