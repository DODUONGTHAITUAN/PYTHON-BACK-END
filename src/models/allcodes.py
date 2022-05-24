from src import db
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship


class Allcodes(db.Model):
    __tablename__ = "Allcodes"
    # Define column
    id = Column(Integer, nullable=False, unique=True, autoincrement=True)
    keyMap = Column(String(255), primary_key=True)
    type = Column(String(255), nullable=False)
    value = Column(String(255), nullable=False)
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), server_default=func.now())

    # Add Relationship
    """ Tạo quan hệ one to many"""
    """ Product để trong ngoặc thì phải ghi đúng tên class
        backref: sẽ là một đối tượng khi mà chúng ta kéo product lên 
        Ví dụ: bên dưới là dùng backref với product nên khi mình get product lên 
        p = Product.get(id)
        p.brand_data.value ==> trả về giá trị value trong bảng allcode
     """
    # Raltionship one to many vơi bảng Product
    products = relationship("Product", backref="brand_data", lazy=True)

    # Constuctor
    def __init__(self):
        pass

    def __repr__(self):
        return f"<Allcodes {self.id}>"
