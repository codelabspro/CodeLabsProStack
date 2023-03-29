from fastapi import FastAPI, Depends, Response, status, HTTPException
from typing import Optional
from sqladmin import Admin, ModelView
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from starlette.responses import RedirectResponse

from router import post, user, authentication
from typing import List

import models
from database import SessionLocal, engine, get_db, create_db_and_tables
from sqlalchemy.orm import Session
from hashing import Hash

from fastapi.middleware.cors import CORSMiddleware


###############################################################################
# app = FastAPI()
app = FastAPI(title ="CodeLabsProStack API", version="0.1.0")

#We define authorizations for middleware components
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000", "https://codelabsprostack.onrender.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#We use a callback to trigger the creation of the table if they don't exist yet
#When the API is starting
@app.on_event("startup")
def on_startup():
    print("Calling Created DB and Tables")
    create_db_and_tables()

###############################################################################
class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username, password = form["username"], form["password"]

        # Validate username/password credentials
        # And update session
        request.session.update({"token": "..."})

        return True

    async def logout(self, request: Request) -> bool:
        # Usually you'd want to just clear the session
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> Optional[RedirectResponse]:
        token = request.session.get("token")

        if not token:
            return RedirectResponse(request.url_for("admin:login"), status_code=302)

        # Check the token in depth


authentication_backend = AdminAuth(secret_key="12345")
admin = Admin(app=app, engine=engine, authentication_backend=authentication_backend)

# admin = Admin(app, engine)

class UserAdmin(ModelView, model=models.User):
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True
    column_list = [models.User.id, models.User.name]

class PostAdmin(ModelView, model=models.Post):
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True
    column_list = [models.Post.id, models.Post.title, models.Post.body, models.Post.author_id, models.Post.author]


admin.add_view(UserAdmin)
admin.add_view(PostAdmin)
###############################################################################
@app.get('/')
def index():
    return 'CodeLabsProStack'


app.include_router(authentication.router)
app.include_router(post.router)
app.include_router(user.router)

###############################################################################

###############################################################################


