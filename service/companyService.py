# -*- coding: utf-8 -*-
# Author  : Yang Hao
# File    : companyService.py
# Software: PyCharm
# Time    : 2020/3/20 10:20
# Description:
from app.models.company import Company


def getAllCompany():
    companys = Company.query.all()
    return companys
