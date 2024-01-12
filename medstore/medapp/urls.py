import statistics
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from .views import  logout


from medapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path("login_user", views.login_user, name='login_user'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
    path('admin_view', views.admin_view, name='admin_view'),
    path('upload_medicine/', views.upload_medicine, name='upload_medicine'),
    path('update_medicine/<int:medicine_id>/', views.update_medicine, name='update_medicine'),
    path('delete_medicine/<int:medicine_id>/', views.delete_medicine, name='delete_medicine'),
    path('user', views.user, name='user'),
    path('details', views.details, name='details'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)