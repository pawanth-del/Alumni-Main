from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import CheckConstraint
from werkzeug.security import generate_password_hash, check_password_hash
import re

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    _email = db.Column(db.String(120), unique=False, nullable=False, index=True)
    _order_id = db.Column(db.String(100), unique=True, nullable=True)
    first_name = db.Column(db.String(50), nullable=False)
    middle_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=False)
    _phone_number = db.Column(db.String(64), nullable=False)
    country_code = db.Column(db.String(10), nullable=False)
    is_whatsapp_same = db.Column(db.Boolean, default=False, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    year_of_graduation = db.Column(db.Integer, nullable=False)
    branch = db.Column(db.String(100), nullable=False)
    accompanied_person = db.Column(db.String(50), nullable=True)
    parents = db.Column(db.Boolean, default=False, nullable=False)
    children = db.Column(db.Boolean, default=False, nullable=False)
    initiated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    order_total = db.Column(db.Float, nullable=True)
    contribution_amount = db.Column(db.Float, nullable=True)
    order_status = db.Column(db.String(10), nullable=False, default='pending')
    is_active = db.Column(db.Boolean, default=True, nullable=False)

    __table_args__ = (
        CheckConstraint(gender.in_(['Male', 'Female', 'Other']), name='check_gender'),
        CheckConstraint(order_status.in_(['pending', 'completed', 'failed']), name='check_order_status'),
    )

    @hybrid_property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValueError("Invalid email address format")
        self._email = value.lower()

    @hybrid_property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        if not re.match(r"^\+?[1-9]\d{1,14}$", value):
            raise ValueError("Invalid phone number format")
        self._phone_number = generate_password_hash(value)

    def verify_phone_number(self, phone_number):
        return check_password_hash(self._phone_number, phone_number)

    @hybrid_property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = generate_password_hash(value)

    def verify_order_id(self, order_id):
        return check_password_hash(self._order_id, order_id)
