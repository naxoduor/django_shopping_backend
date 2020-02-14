from django.urls import path

from . import views

app_name = 'shopping'
urlpatterns = [
    path('', views.index, name='index'),
    path('test/<int:user_id>/', views.test, name='test'),
    path('departments/', views.showAllDepartments, name='showAllDepartments'),
    path('products/inCategory/<int:id>/',views.showProductsInCategory,name='showProductsInCategory'),
    path('categories/', views.showAllCategories),
    path('categories/inDepartment/<int:department_id>/', views.showCategoriesByDepartment),
    path('categories/totalitems/<int:id>/', views.countProductsInCategory),
    path('categories/post/', views.handlePostRequest),
    path('shoppingcart/generateUniqueId', views.generateUniqueId),
    path('shoppingcart/<slug:cart_id>',views.getCartItems)
]
