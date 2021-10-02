from datetime import datetime
from sqlalchemy import event
from slugify import slugify
from zooshicovid import db

class Registers(db.Model):

    ReferNo = db.Column(db.String(15),primary_key=True)
    CardID = db.Column(db.String(20))
    FName = db.Column(db.String(100))
    LName = db.Column(db.String(100))
    AgeStr = db.Column(db.String(50))
    Sex = db.Column(db.String(10))
    RequestDate = db.Column(db.DateTime)
    Hn = db.Column(db.String(15))

  
############### mserch ###############
class Register(db.Model):
    __searchable__ = ['CardID']
    ReferNo = db.Column(db.String(15),primary_key=True)
    CardID = db.Column(db.String(20),nullable=False)
    FName = db.Column(db.String(100),nullable=False)
    LName = db.Column(db.String(100),nullable=False)
    AgeStr = db.Column(db.String(50),nullable=False)
    Sex = db.Column(db.String(10),nullable=False)
    RequestDate = db.Column(db.DateTime)
    Hn = db.Column(db.String(15),nullable=False)

    def __repr__(self):
        return '<Register %r' % self.CardID

    @staticmethod 
    def generate_slug(target,value,oldvalue,initiator):
        if value and (not target.slug or value != oldvalue):
            target.slug = slugify(value)
db.event.listen(Register.CardID,'set',Register.generate_slug,retval=False)
 