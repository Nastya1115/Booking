from django.urls import path
import appname.views as views

urlpatterns = [
    path("", views.main_page, name="main_page"),
]