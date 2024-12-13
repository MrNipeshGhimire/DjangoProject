from django.urls import path
from .views.main_view import home,create_product,edit_product,single_product
from .views.auth_view import login_page,register_page

urlpatterns = [
    path("",home, name="home"),
    path("create/",create_product,name="create"),
    path("edit/",edit_product, name="edit"),
    path("single/",single_product, name="single"),

    path("login/",login_page,name="login"),
    path("register/",register_page, name="register")
]
