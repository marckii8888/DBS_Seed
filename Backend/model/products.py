from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root123@localhost:3306/ecommerce'
# app.config['SQLALCHEYMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'

db = SQLAlchemy(app)

class Products(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.Text)
    price = db.Column(db.Float)
    description = db.Column(db.Text)
    image = db.Column(db.Text)
    qty = db.Column(db.Integer)

    def __init__(self, id, title, price, description, image, qty):
        self.id = id
        self.title = title
        self.price = price
        self.description = description
        self.image = image
        self.qty = qty

    def json(self):
        return {
            "id":self.id,
            "title":self.title,
            "price":self.price,
            "description":self.description,
            "image":self.image,
            "qty":self.qty
            }

# Methods
@app.route('/list_products', methods=['GET'])
def get_all():
    return jsonify({
        "product": [product.json() for product in Products.query.all()]
    })

# Update an product
@app.route('/product/<int:id>/update', methods=['POST'])
def update(id):
    order = Products.query.filter_by(id=id).first()
    if order:
        db.session.delete(order)
        db.session.commit()
        data = request.get_json()
        product_id = data['product_id']
        order_id = data['order_id']
        product_qty = data['product_qty']
        total_price = data['total_price']
        orderItem = Products(product_id=product_id, order_id=order_id, product_qty=product_qty, total_price=total_price)
        db.session.add(orderItem)
        db.session.commit()

        return make_response(jsonify({"response": "Added"}), 200)
    return make_response(jsonify({"response": "No such order"}), 200)