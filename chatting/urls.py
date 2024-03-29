from django.urls import path
from chatting import views

urlpatterns = [
    path('',views.login,name='login'),
    path('verify_otp/', views.verify_otp, name='verify_otp'),
    path('verify_admin/',views.verify_admin,name='verify_admin'),
    path('set_profile_users',views.set_profile_users,name='set_profile_users')
]
