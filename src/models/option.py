from src import db
from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey, Text
from sqlalchemy.orm import relationship

from .product import Product
from .allcodes import Allcodes


class Option(db.Model):
    __tablename__ = "Option"
    id = Column(Integer, primary_key=True, autoincrement=True)
    productID = Column(Integer, ForeignKey(Product.id))
    ram = Column(String(255), nullable=False)
    rom = Column(String(255), nullable=False)
    price = Column(String(255), nullable=False)
    image = Column(Text, nullable=True)
    colorID = Column(String(255), ForeignKey(Allcodes.keyMap))
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), server_default=func.now())

    # Define relationship
    product_data = relationship(Product, foreign_keys=[productID])
    color_data = relationship(Allcodes, foreign_keys=[colorID])

    def __init__(self, productID, ram, rom, price, image, colorID):
        self.productID = productID
        self.ram = ram
        self.rom = rom
        self.price = price
        self.image = image
        self.colorID = colorID
