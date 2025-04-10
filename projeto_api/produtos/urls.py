from django.urls import path
from . import views

urlpatterns = [
    path('categorias/', views.categorialist.as_view(), name='categoria-list'),
    path('categorias/<int:pk>/', views.CategoriaDetail.as_view(), name='categoria-detail'),
    path('Produtos/', views.ProdutoList.as_view(), name='Produto-list'),
    path('Produtos/<int:pk>/', views.ProdutoDetail.as_view(), name='Produto-detail'),
]