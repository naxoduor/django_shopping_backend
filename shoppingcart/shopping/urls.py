from django.urls import path

from . import views

app_name = 'shopping'
urlpatterns = [
    path('', views.index, name='index'),
    path('test/<int:user_id>/', views.test, name='test'),
    path('departments/', views.showAllDepartments, name='showAllDepartments'),
    path('products/inCategory/<int:id>/',views.showDepartmentsById,name='showDepatmentsById'),
    path('categories/', views.showAllCategories),
    path('categories/inDepartment/<int:department_id>/', views.showCategoriesByDepartment),
    path('categories/totalitems/<int:id>/', views.countProductsInCategory)
]
