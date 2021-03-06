# -*- coding: utf-8 -*-
# Author  : Yang Hao
# File    : company_model.py
# Software: PyCharm
# Time    : 2020/3/20 10:06
# Description:
from app import db
from app.models.base_model import BaseModel


class Company(db.Model, BaseModel):
    __tablename__ = 'company'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(10), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(50), nullable=False)
