# FastAPI_Menu

Простой FastAPI API для ресторанного меню.


[![My Skills](https://skillicons.dev/icons?i=py,fastapi,postgres,github)](https://skillicons.dev)

## Документация по проекту

### Для запуска проекта необходимо

* ### 1. Установить зависимости:

```bash
pip install -r requirements.txt
```
 cvb
* ### 2. Создать .env файл в общей папке и указать значение для Postgresql:

DATABASE_URL = "postgresql://пользователь:пароль@сервер/имя_базы"

* ### 3. Запуск сервера:

```bash
uvicorn main:app --reload
```

docker image build . --tag=my_app_08


## Requests:

| Description                        | Method                                              | Request                                                          |
|------------------------------------|-----------------------------------------------------|------------------------------------------------------------------|
| Просматривает список меню          | ![GET](https://img.shields.io/badge/-GET-blue)      | `/api/v1/menus`                                                  |
| Создает меню                       | ![POST](https://img.shields.io/badge/-POST-success) | `/api/v1/menus`                                                  |
| Просматривает определенное меню    | ![GET](https://img.shields.io/badge/-GET-blue)      | `/api/v1/menus/{menu_id}`                                        |
| Обновляет меню                     | ![PATCH](https://img.shields.io/badge/-PATCH-9cf)   | `/api/v1/menus/{menu_id}`                                        |
| Удаляет меню                       | ![DELETE](https://img.shields.io/badge/-DELETE-red) | `/api/v1/menus/{menu_id}`                                        |
| Просматривает список подменю       | ![GET](https://img.shields.io/badge/-GET-blue)      | `/api/v1/menus/{menu_id}/submenus`                               |
| Создает подменю                    | ![POST](https://img.shields.io/badge/-POST-success) | `/api/v1/menus/{menu_id}/submenus`                               |
| Просматривает определенное подменю | ![GET](https://img.shields.io/badge/-GET-blue)      | `/api/v1/menus/{menu_id}/submenus/{submenu_id}`                  |
| Обновляет подменю                  | ![PATCH](https://img.shields.io/badge/-PATCH-9cf)   | `/api/v1/menus/{menu_id}/submenus/{submenu_id}`                  |
| Удаляет подменю                    | ![DELETE](https://img.shields.io/badge/-DELETE-red) | `/api/v1/menus/{menu_id}/submenus/{submenu_id}`                  |
| Просматривает список блюд          | ![GET](https://img.shields.io/badge/-GET-blue)      | `/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes`           |
| Создает блюдо                      | ![POST](https://img.shields.io/badge/-POST-success) | `/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes`           |
| Просматривает определенное блюдо   | ![GET](https://img.shields.io/badge/-GET-blue)      | `/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}` |
| Обновляет блюдо                    | ![PATCH](https://img.shields.io/badge/-PATCH-9cf)   | `/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}` |
| Удаляет блюдо                      | ![DELETE](https://img.shields.io/badge/-DELETE-red) | `/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}` |

