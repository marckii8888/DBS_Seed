from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from products import Products

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root123@localhost:3306/ecommerce'
# app.config['SQLALCHEYMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'

db = SQLAlchemy(app)

class OrderItem(db.Model):
    __tablename__ = 'order_item'

    product_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, primary_key=True)
    product_qty = db.Column(db.Integer)
    total_price = db.Column(db.Float)

    def __init__(self, product_id, order_id, product_qty, total_price):
        self.product_id = product_id
        self.order_id = order_id
        self.product_qty = product_qty
        self.total_price = total_price

    def json(self):
        return {
            "product_id":self.product_id,
            "order_id":self.order_id,
            "product_qty":self.product_qty,
            "total_price": self.total_price,
        }

    def get_product_id(self):
        return self.product_id




# Methods

# Insert products added into database
@app.route('/create_orderitem', methods=['POST'])
def create_todo():
    data = request.get_json()
    product_id = data['product_id']
    order_id = data['order_id']
    product_qty = data['product_qty']
    total_price = data['total_price']
    orderItem = OrderItem(product_id=product_id, order_id=order_id, product_qty=product_qty, total_price=total_price)
    db.session.add(orderItem)
    db.session.commit()
    return make_response(jsonify({"response": "Added"}), 200)

# Return a list of all products from the OrderItem table
@app.route('/list_orderitems', methods=['GET'])
def get_products():
    # products = [product.json() for product in Products.query.filter_by]
    productIDs = [orderItem.get_product_id() for orderItem in OrderItem.query.all() ]

    result = []
    for productID in productIDs:
        result.extend([product.json() for product in Products.query.filter_by(id=productID)])

    return jsonify({
        "product": result
    })


# Delete an item from the OrderItem table
# Order_id = refer order
# product id = refer product
@app.route('/orderitem/<int:id>/delete', methods=['POST'])
def delete(id):
    orderitems = OrderItem.query.filter_by(order_id=id).all()
    if orderitems:
        for orderitem in orderitems:
            db.session.delete(orderitem)
            db.session.commit()
        return jsonify({
            "response" : "item deleted"
        })

    return jsonify({
        "response" : "item not found"
    })
# Update an order from OrderItem table
@app.route('/orderitem/<int:id>/update', methods=['POST'])
def update(id):
    order = OrderItem.query.filter_by(order_id=id).first()
    if order:
        db.session.delete(order)
        db.session.commit()
        data = request.get_json()
        product_id = data['product_id']
        order_id = data['order_id']
        product_qty = data['product_qty']
        total_price = data['total_price']
        orderItem = OrderItem(product_id=product_id, order_id=order_id, product_qty=product_qty, total_price=total_price)
        db.session.add(orderItem)
        db.session.commit()

        return make_response(jsonify({"response": "Added"}), 200)
    return make_response(jsonify({"response": "No such order"}), 200)
