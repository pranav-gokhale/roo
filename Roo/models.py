from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from Roo.database import Base

class Bag(Base):
  __tablename__ = 'bags'
  id = Column(Integer, primary_key=True)
  store = Column(String(30), unique=False)
  threshold = Column(Integer, unique=False)
  amountinbag = Column(Integer, unique=True)
  network = Column(String(30), unique=False)

  def __init__(self, store=None, threshold=None, amountinbag=None, network=None):
    self.store = store
    self.threshold = threshold
    self.amountinbag = amountinbag
    self.network = network

  def __repr__(self):
    '<Bag %r>' % (self.store)

class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  firstname = Column(String(30), unique=False)
  lastname = Column(String(30), unique=False)
  email = Column(String(40), unique=True)
  password = Column(String(40), unique=True)
  address = Column(String(80), unique=False)
  bag_id = Column(Integer, ForeignKey('bags.id'))

  bag = relationship("Bag", backref=backref('users', order_by=id))

  def __init__(self, firstname, lastname=None, email=None, address=None, bag_id=None):
    self.firstname = firstname
    self.lastname = lastname
    self.email = email
    self.address = address

  def __repr__(self):
    '<User %r>' % (self.firstname)
