import uuid

from sqlalchemy import func
from sqlalchemy.orm import Session
from sql_app import models, schemas


def get_menu(db: Session, skip: int = 0, limit: int = 100):
    menus = db.query(models.MenuModel).offset(skip).limit(limit).all()
    for menu in menus:
        menu.submenus_count = db.query(func.count(models.SubmenuModel.id)).filter_by(menu_id=menu.id).scalar()
        menu.dishes_count = db.query(func.count(models.DishModel.id)).join(models.SubmenuModel).scalar()
    return menus


def create_menu(db: Session, menu: schemas.BaseSchemas):
    db_menu = models.MenuModel(title=menu.title, description=menu.description)
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return db_menu


def get_menu_by_id(db: Session, menu_id: uuid.UUID):
    menus = db.query(models.MenuModel).filter(models.MenuModel.id == menu_id).first()
    if menus is not None:
        menus.submenus_count = db.query(func.count(models.SubmenuModel.id)).filter_by(menu_id=menus.id).scalar()
        # menus.dishes_count = db.query(func.count(models.DishModel.id)).filter_by(submenu_id=menus.id).scalar()
        menus.dishes_count = db.query(func.count(models.DishModel.id)).join(models.SubmenuModel).scalar()
    return menus


def update_menu(db: Session, menu_id: uuid.UUID, menu: schemas.BaseSchemasAllCreate):
    db_menu = db.query(models.MenuModel).filter(models.MenuModel.id == menu_id).first()
    db_menu.title = menu.title
    db_menu.description = menu.description
    db.commit()
    db.refresh(db_menu)
    return db_menu


def delete_menu(db: Session, menu_id: uuid.UUID):
    db_menu = db.query(models.MenuModel).filter(models.MenuModel.id == menu_id).delete()
    db.commit()
    return db_menu


def get_submenu(db: Session, skip: int = 0, limit: int = 100):
    submenus = db.query(models.SubmenuModel).offset(skip).limit(limit).all()
    for submenu in submenus:
        submenu.dishes_count = db.query(func.count(models.DishModel.id)).filter_by(submenu_id=submenu.id).scalar()
    return submenus


def create_submenu(db: Session, submenu: schemas.BaseSchemasAllCreate, menu_id: uuid.UUID):
    db_submenu = models.SubmenuModel(title=submenu.title, description=submenu.description, menu_id=menu_id)
    db.add(db_submenu)
    db.commit()
    db.refresh(db_submenu)
    return db_submenu


def get_submenu_by_id(db: Session, submenu_id: uuid.UUID):
    submenus = db.query(models.SubmenuModel).filter(models.SubmenuModel.id == submenu_id).first()
    if submenus is not None:
        submenus.dishes_count = db.query(func.count(models.DishModel.id)).join(models.SubmenuModel).scalar()
        # submenus.dishes_count = db.query(func.count(models.DishModel.id)).filter_by(submenu_id=submenus.id).scalar()
        # dishes_count = db.query(func.count(models.DishModel.id)).join(models.SubmenuModel).scalar()
    return submenus


def update_submenu(db: Session, submenu_id: uuid.UUID, submenu: schemas.BaseSchemasAllCreate):
    db_submenu = db.query(models.SubmenuModel).filter(models.SubmenuModel.id == submenu_id).first()
    db_submenu.title = submenu.title
    db_submenu.description = submenu.description
    db.commit()
    db.refresh(db_submenu)
    return db_submenu


def delete_submenu(db: Session, submenu_id: uuid.UUID):
    db_submenu = db.query(models.SubmenuModel).filter(models.SubmenuModel.id == submenu_id).delete()
    db.commit()
    return db_submenu


def get_dish(db: Session, skip: int = 0, limit: int = 100):
    dishes = db.query(models.DishModel).offset(skip).limit(limit).all()
    return dishes


def create_dish(db: Session, dish: schemas.DishSchemas, submenu_id: uuid.UUID):
    db_dish = models.DishModel(title=dish.title, description=dish.description, price=dish.price, submenu_id=submenu_id)
    db.add(db_dish)
    db.commit()
    db.refresh(db_dish)
    return db_dish


def get_dish_by_id(db: Session, dish_id: uuid.UUID):
    dish = db.query(models.DishModel).filter(models.DishModel.id == dish_id).first()
    return dish


def update_dish(db: Session, dish_id: uuid.UUID, dish: schemas.DishSchemas):
    db_dish = db.query(models.DishModel).filter(models.DishModel.id == dish_id).first()
    db_dish.title = dish.title
    db_dish.description = dish.description
    db_dish.price = dish.price
    db.commit()
    db.refresh(db_dish)
    return db_dish


def delete_dish(db: Session, dish_id: uuid.UUID):
    db_dish = db.query(models.DishModel).filter(models.DishModel.id == dish_id).delete()
    db.commit()
    return db_dish
