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

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self



# Methods

# Insert products added into database
@app.route('/create_orderitem', methods=['POST'])
def create_todo():
    data = request.get_json()
    product_id = data['product_id']
    order_id = data['order_id']
    product_qty = data['product_qty']
    total_price = data['total_price']
#    product_id = request.form['product_id']
#    order_id = request.form['order_id']
#    product_qty = request.form['product_qty']
#    total_price = request.form['total_price']
    orderItem = OrderItem(product_id=product_id, order_id=order_id, product_qty=product_qty, total_price=total_price)
    # orderItem.create()
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
@app.route('/orderitem/<int:id>/delete', methods=['POST'])
def delete(id):
    orderitem = OrderItem.query.filter_by(order_id=id).all()
    if orderitem:
        db.session.delete(orderitem)
        db.session.commit()
        return jsonify({
            "response" : "item deleted"
        })

# Update an order from OrderItem table

'''
@app.route('/data/<int:id>/update',methods = ['GET','POST'])
def update(id):
    employee = EmployeeModel.query.filter_by(employee_id=id).first()
    if request.method == 'POST':
        if employee:
            db.session.delete(employee)
            db.session.commit()
 
            name = request.form['name']
            age = request.form['age']
            position = request.form['position']
            employee = EmployeeModel(employee_id=id, name=name, age=age, position = position)
 
            db.session.add(employee)
            db.session.commit()
            return redirect(f'/data/{id}')
        return f"Employee with id = {id} Does nit exist"
 
    return render_template('update.html', employee = employee)
'''


'''
− Insert products added from frontend cart into database [3]
− Delete from the OrderItem table [5]
− Update the Orders, Products, and OrderItem table [6]
'''