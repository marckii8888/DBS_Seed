from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root123@localhost:3306/ecommerce'
# app.config['SQLALCHEYMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'

db = SQLAlchemy(app)

class Categories(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.Text)
    image = db.Column(db.Text)

    def __init__(self, id, name, description, image):
        self.id = id
        self.name = name
        self.description = description
        self.image = image

    def json(self):
        return{
            "id": self.id,
            "name":self.name,
            "description": self.description,
            "image": self.image
        }

# Methods
@app.route('/list_categories', methods=['GET'])
def get_all():
    return jsonify({
        "categories" : [category.json() for category in Categories.query.all()]
    })

