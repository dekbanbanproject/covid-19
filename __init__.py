from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_msearch import Search


# def create_app():
app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = f'mssql://uat:uatS@dmin@http://labrdc.ddns.net/uatdb?driver=SQL Server Native Client 11.0'
app.config['SQLALCHEMY_DATABASE_URI'] = f'mssql://sa:123456@ZOOSHI/covid_19?driver=SQL Server Native Client 11.0'
app.config['SECRET_KEY'] = 'dekbanbanproject-0981581238'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
search = Search()
search.init_app(app)

from zooshicovid import routes