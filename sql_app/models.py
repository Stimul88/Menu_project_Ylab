import uuid
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DECIMAL
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy.dialects.postgresql import UUID


class MenuModel(Base):
    __tablename__ = "menus"

    # id = Column(Integer, primary_key=True, index=True)
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, index=True, unique=True)
    description = Column(String, index=True, unique=True)
    submenu = relationship("SubmenuModel", back_populates="menu", cascade="all, delete")


class SubmenuModel(Base):
    __tablename__ = "submenus"

    # id = Column(Integer, primary_key=True, index=True)
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, index=True, unique=True)
    description = Column(String, index=True, unique=True)
    # menu_id = Column(Integer, ForeignKey("menus.id", ondelete="CASCADE"))
    menu_id = Column(UUID(as_uuid=True), ForeignKey("menus.id", ondelete="CASCADE"))

    menu = relationship("MenuModel", back_populates="submenu")
    dish = relationship("DishModel", back_populates="submenu", cascade="all, delete")


class DishModel(Base):
    __tablename__ = "dishes"

    # id = Column(Integer, primary_key=True, index=True)
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, index=True, unique=True)
    description = Column(String, index=True, unique=True)
    price = Column(Float(precision=2))
    # submenu_id = Column(Integer, ForeignKey("submenus.id", ondelete="CASCADE"))
    submenu_id = Column(UUID(as_uuid=True), ForeignKey("submenus.id", ondelete="CASCADE"))

    submenu = relationship("SubmenuModel", back_populates="dish")
