from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from products import Products
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

    # def get_product_id(self):
    #     return self.product_id

    # def create(self):
    #     db.session.add(self)
    #     db.session.commit()
    #     return self



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