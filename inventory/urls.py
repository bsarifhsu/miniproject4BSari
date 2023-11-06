# INF601 - Advanced Programming in Python
# Bunyamin Sari
# Mini Project 4


from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "inventory"
urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('<int:product_id>/edit/', views.product_edit, name='product_edit'),
    path('<int:product_id>/delete/', views.product_delete, name='product_delete'),
    path('create/', views.product_create, name='product_create'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
