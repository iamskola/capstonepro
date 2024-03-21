from django.urls import path
from  . import views 
from rest_framework.authtoken import views as auth_view


urlpatterns=[
    path('categories',views.CategoryEndpoint.as_view(), name='categories'),
    path('category/<int:pk>', views.SingleCategoryEndpoint.as_view(), name='category-details'),
    path('category/<int:pk>/delete',views.CategoryDeleteEndpoint.as_view(), name='delete-category'),
    path('products_create', views.ProductEndpoint.as_view(), name='products_create'),
    path('products_list_only', views.ProductListEndpoint.as_view(), name='products_list'),
    path('product/<int:product_id>', views.ProductDetailEndpoint.as_view(), name='product-detail'),
    path('store_list_only/', views.StoreListEndpoint.as_view(), name='store_list'),
    path('store_create/', views.StoreEndpoint.as_view(), name='store'),
    path('store/<int:store_id>', views.StoreDetailEndpoint.as_view(), name='store-detail')

]