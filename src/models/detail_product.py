from src import db
from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey, Text
from sqlalchemy.orm import relationship

from .allcodes import Allcodes
from .product import Product


class DetailProduct(db.Model):
    __tablename__ = "DetailProduct"

    # Define column
    id = Column(Integer, primary_key=True, autoincrement=True)
    contentHTML = Column(Text, nullable=True)
    contentMarkdown = Column(Text, nullable=True)
    simSlots = Column(Integer, nullable=False, default=1)
    osID = Column(String(255), ForeignKey(Allcodes.keyMap))
    batteryText = Column(String(255), nullable=False)
    batteryID = Column(String(255), ForeignKey(Allcodes.keyMap))
    screenText = Column(String(255), nullable=False)
    screenID = Column(String(255), ForeignKey(Allcodes.keyMap))
    brandID = Column(String(255), ForeignKey(Allcodes.keyMap))
    featureID = Column(String(255), ForeignKey(Allcodes.keyMap))
    productID = Column(Integer, ForeignKey(Product.id))
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), server_default=func.now())

    """
    Define relationship 
     product_data = relationship(Product, foreign_keys=[productID])
    color_data = relationship(Allcodes, foreign_keys=[colorID])
    """
    os_data = relationship(Allcodes, foreign_keys=[osID])
    battery_data = relationship(Allcodes, foreign_keys=[batteryID])
    screen_data = relationship(Allcodes, foreign_keys=[screenID])
    brand_data = relationship(Allcodes, foreign_keys=[brandID])
    feature_data = relationship(Allcodes, foreign_keys=[featureID])
    product_data = relationship(Product, foreign_keys=[productID])

    # Constructor
    def __init__(
        self,
        contentHTML,
        contentMarkdown,
        simSlots,
        osID,
        batteryText,
        batteryID,
        screenText,
        screenID,
        brandID,
        featureID,
        productID,
    ):
        self.contentHTML = contentHTML
        self.contentMarkdown = contentMarkdown
        self.simSlots = simSlots
        self.osID = osID
        self.batteryText = batteryText
        self.batteryID = batteryID
        self.screenText = screenText
        self.screenID = screenID
        self.brandID = brandID
        self.featureID = featureID
        self.productID = productID
