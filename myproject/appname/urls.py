from django.urls import path
import appname.views as views

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("register/", views.register_user, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path('user/', views.my_reservations, name='my_reservations'),
    path('hotel/<str:hotel_name>/', views.hotel_page, name='hotel_page'),
    path('room/<int:room_id>/', views.room_page, name='room_page'),
    path('get_reserved_dates/<int:room_id>/', views.get_reserved_dates, name='get_reserved_dates'),
]