from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<Category {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
        }

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    category_a = db.Column(db.String(200))
    sub_category_a = db.Column(db.String(200))
    
    category_id = db.Column(db.Integer, db.ForeignKey('category.id') )
    category = db.relationship('Category', backref=db.backref('expenses', lazy=True))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), )
    user = db.relationship('User', backref=db.backref('expenses', lazy=True))

    def __repr__(self):
        return f'<Expense {self.description} - {self.amount}>'

    def serialize(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "description": self.description,
            "category": self.category.serialize(),
            "user_id": self.user_id,
        }