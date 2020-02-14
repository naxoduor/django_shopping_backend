from django.shortcuts import render

from .models import product
from .models import department
from .models import category
from .models import shopping_cart
from rest_framework.decorators import api_view
from django.http import JsonResponse

@api_view(['GET' ])
def index(request):
    pro=product.objects.all().values()
    pro_list=list(pro)
    return JsonResponse(pro_list, safe=False)

@api_view(['GET' ])
def test(request, user_id):
    return JsonResponse({"route":"testing the route"})

@api_view(['GET' ])
def showAllDepartments(request):
    departments=department.objects.all().values()
    return JsonResponse(list(departments), safe=False)

@api_view(['GET' ])
def showProductsInCategory(request,id):
    products=product.objects.select_related().filter(product_category__category_id=id).values()
    return JsonResponse(list(products), safe=False)

@api_view(['GET'])
def showAllCategories(request):
    categories=category.objects.all().values()
    return JsonResponse(list(categories), safe=False)

@api_view(['GET'])
def showCategoriesByDepartment(request, department_id):
    categories=category.objects.filter(department_id=department_id).values()
    return JsonResponse(list(categories), safe=False)

@api_view(['GET'])
def countProductsInCategory(request, id):
    productsCount=product.objects.select_related().filter(product_category__category_id=id).count();
    return JsonResponse(productsCount, safe=False)

@api_view(['GET'])
def generateUniqueId(request):
    return JsonResponse({"GeneratedId"})

@api_view(['GET'])
def getCartItems(request, cart_id):
    print(cart_id)
    cart=shopping_cart.objects.filter(cart_id=cart_id).select_related('product').values('item_id','cart_id','attributes','quantity','buy_now','added_on','product__name','product__price','product__description','product__image')
    return JsonResponse(list(cart), safe=False)

@api_view(['POST'])
def handlePostRequest(request):
    print("Return the request")
    data=request.data
    print(data)
    print(data.get("name"))
    print(data.get("description"))
    #print(request.data.name)
    #print(request.data.description)
    return JsonResponse({"route":"testing the route"})
    


#Create your views here.




