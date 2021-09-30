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
