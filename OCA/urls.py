"""
URL configuration for OCA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from chatting import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chatting.urls')),
    path('logout/',views.logout_view,name='logout'),
    path('get-messages/<int:user_id>/<int:user2_id>/',views.get_messages,name='get_messages'),
    path('save-messages/save/',views.save_messages,name='save_messages'),
    path('get-users/',views.get_users,name='get_users'),
    path('search-user/',views.search_user,name='search_user'),
    path('profile/',views.profile_view,name='profile'),
    path('update/',views.update_profile,name='update'),
    path('delete/',views.delete_account,name='delete'),
    path('save-feedback/',views.save_feedback,name='save_feedback'),
    path('get-feedbacks/',views.get_feedbacks,name='get_feedbacks'),
    path('save-all-message/save/',views.save_all_message,name='save_all_message')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)