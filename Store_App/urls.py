from django.urls import path
from  . import views 
from rest_framework.authtoken import views as auth_view


urlpatterns=[
    path('categories',views.CategoryEndpoint.as_view(), name='categories'),
    path('category/<int:pk>', views.SingleCategoryEndpoint.as_view(), name='category-details'),
    path('category/<int:pk>/delete',views.CategoryDeleteEndpoint.as_view(), name='delete-category'),
    #path('products-list', views.ProductEndpoint.as_view(), name='products-list'),
    path('products', views.ProductListEndpoint.as_view(), name='products'),
    path('product/<int:product_id>', views.ProductDetailEndpoint.as_view(), name='product-detail'),
    path('store/', views.StoreListEndpoint.as_view(), name='store'),
    #path('store-list/', views.StoreEndpoint.as_view(), name='store'),
    path('store/<int:store_id>', views.StoreDetailEndpoint.as_view(), name='store-detail')

]