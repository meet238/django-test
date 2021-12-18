from django.urls import path

from website.views import IndexView, ListOfProductView, ListOfCategoryView, ListOfProductViewUser, AddProductView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('admin-product', ListOfProductView.as_view(), name='list-of-product'),
    path('admin-category', ListOfCategoryView.as_view(), name='list-of-category'),
    path('user-product', ListOfProductViewUser.as_view(), name='list-of-user-product'),
    path('add-product', AddProductView.as_view(), name='add-product'),
]
