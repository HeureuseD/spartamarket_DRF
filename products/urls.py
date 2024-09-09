from django.urls import path
from .views import ProductList, ProductDetail

app_name="products"
urlpatterns = [
    path("products/", ProductList.as_view(), name="product-List"),
    path("<int:productid>/", ProductDetail.as_view(), name="product-detail"),
]