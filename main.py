import uuid

import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from database import engine, SessionLocal
from sql_app import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api/v1/menus", response_model=list[schemas.MenuSchemas])
def get_menu(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_menu(db, skip=skip, limit=limit)


@app.post("/api/v1/menus", response_model=schemas.BaseSchemasAllReturn,
          status_code=201)
def create_menu(menu: schemas.BaseSchemasAllCreate,
                db: Session = Depends(get_db)):
    db_menu = crud.create_menu(db=db, menu=menu)
    return db_menu


@app.get("/api/v1/menus/{menu_id}",
         response_model=schemas.MenuSchemas)
def get_menu_by_id(menu_id: uuid.UUID,
                   db: Session = Depends(get_db)):
    db_menu = crud.get_menu_by_id(db, menu_id=menu_id)
    if db_menu is None:
        raise HTTPException(status_code=404, detail="menu not found")
    return db_menu


@app.patch("/api/v1/menus/{menu_id}",
           response_model=schemas.BaseSchemasAllCreate)
def update_menu(menu_id: uuid.UUID, menu: schemas.BaseSchemasAllCreate,
                db: Session = Depends(get_db)):
    return crud.update_menu(db, menu_id=menu_id, menu=menu)


@app.delete("/api/v1/menus/{menu_id}")
def delete_menu(menu_id: uuid.UUID, db: Session = Depends(get_db)):
    return crud.delete_menu(db=db, menu_id=menu_id)


@app.get("/api/v1/menus/{menu_id}/submenus",
         response_model=list[schemas.SubmenuSchemas])
def get_submenu(skip: int = 0,
                limit: int = 100,
                db: Session = Depends(get_db)):
    return crud.get_submenu(db=db, skip=skip, limit=limit)


@app.post("/api/v1/menus/{menu_id}/submenus",
          response_model=schemas.BaseSchemasAllReturn,
          status_code=201)
def create_submenu(
    menu_id: uuid.UUID,
        submenu: schemas.BaseSchemasAllCreate,
        db: Session = Depends(get_db)):
    return crud.create_submenu(db=db, submenu=submenu, menu_id=menu_id)


@app.get("/api/v1/menus/{menu_id}/submenus/{submenu_id}",
         response_model=schemas.SubmenuSchemas)
def get_submenu_by_id(submenu_id: uuid.UUID, db: Session = Depends(get_db)):
    db_submenu = crud.get_submenu_by_id(db, submenu_id=submenu_id)
    if db_submenu is None:
        raise HTTPException(status_code=404, detail="submenu not found")
    return db_submenu


@app.patch("/api/v1/menus/{menu_id}/submenus/{submenu_id}",
           response_model=schemas.BaseSchemasAllCreate)
def update_submenu(submenu_id: uuid.UUID,
                   submenu: schemas.BaseSchemasAllCreate,
                   db: Session = Depends(get_db)):
    return crud.update_submenu(db, submenu_id=submenu_id, submenu=submenu)


@app.delete("/api/v1/menus/{menu_id}/submenus/{submenu_id}")
def delete_submenu(submenu_id: uuid.UUID, db: Session = Depends(get_db)):
    return crud.delete_submenu(db=db, submenu_id=submenu_id)


@app.get("/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes",
         response_model=list[schemas.DishSchemas])
def get_dish(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_dish(db=db, skip=skip, limit=limit)


@app.post("/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes",
          response_model=schemas.DishSchemasReturn,
          status_code=201)
def create_dish(submenu_id: uuid.UUID,
                dish: schemas.DishSchemas,
                db: Session = Depends(get_db)):
    return crud.create_dish(db=db, dish=dish, submenu_id=submenu_id)


@app.get("/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}",
         response_model=schemas.DishSchemasReturn)
def get_dish_by_id(dish_id: uuid.UUID, db: Session = Depends(get_db)):
    db_dish = crud.get_dish_by_id(db, dish_id=dish_id)
    if db_dish is None:
        raise HTTPException(status_code=404, detail="dish not found")
    return db_dish


@app.patch("/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}",
           response_model=schemas.DishSchemas)
def update_dish(dish_id: uuid.UUID, dish: schemas.DishSchemas,
                db: Session = Depends(get_db)):
    return crud.update_dish(db, dish_id=dish_id, dish=dish)


@app.delete("/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}")
def delete_dish(dish_id: uuid.UUID,
                db: Session = Depends(get_db)):
    return crud.delete_dish(db=db, dish_id=dish_id)


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
