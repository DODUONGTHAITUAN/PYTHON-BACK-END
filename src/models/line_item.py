from src import db
from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    func,
    ForeignKey,
)

from sqlalchemy.orm import relationship
from .order import Order
from .product import Product

# Define class
class LineItem(db.Model):
    __tablename__ = "LineItem"

    # Define Columns
    id = Column(Integer, autoincrement=True, primary_key=True)
    orderID = Column(Integer, ForeignKey(Order.id), primary_key=True)
    productID = Column(Integer, ForeignKey(Product.id), primary_key=True)
    quantity = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), server_default=func.now())

    # Constructor
    def __init__(self, **lineItem):
        for key, value in lineItem.items():
            self.__dict__[key] = value

    def __repr__(self):
        return f"<LineItem {self.orderID}>"

    # Using self[] operator
    def __getitem__(self, key):
        return self.__dict__[key]
