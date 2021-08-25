from django.urls import path
from . import views

urlpatterns = [
    path("product/", views.ProductListView.as_view(),
         name="product-list"),
    path("product/create/", views.ProductCreateView.as_view(), name="product-create"),
    path("product/<int:pk>/", views.ProductDetailView.as_view(),
         name="product-detail"),
    path("category/", views.CategoryListView.as_view(),
         name="category-list"),
    path("category/create/", views.CategoryCreateView.as_view(),
         name="category-create"),
    path("category/<int:pk>/", views.CategoryDetailView.as_view(),
         name="category-detail"),
    path("cart/", views.CartItemView.as_view(), name="cart"),
    path("cart/add/", views.CartItemAddView.as_view()),
    path("cart/delete/<int:pk>/", views.CartItemDelView.as_view()),
    path("cart/add_one/<int:pk>/", views.CartItemAddOneView.as_view()),
    path("cart/reduce_one/<int:pk>/", views.CartItemReduceOneView.as_view()),
    path("order/<user>/", views.NurseryOrderView.as_view()),
]
