from django.shortcuts import render

from .models import product
from .models import department
from .models import category
from .models import shopping_cart
from .models import customer

from django.contrib.auth.hashers import make_password
from django.contrib.auth.signals import user_logged_in
from rest_framework.permissions import AllowAny, IsAuthenticated

from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes 
from django.http import JsonResponse
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework_jwt.utils import jwt_payload_handler

from django.conf import settings
import jwt

@api_view(['GET' ])
@permission_classes([AllowAny, ])
def index(request):
    pro=product.objects.all().values()
    pro_list=list(pro)
    return JsonResponse(pro_list, safe=False)

@api_view(['GET' ])
@permission_classes([AllowAny, ])
def test(request, user_id):
    return JsonResponse({"route":"testing the route"})

@api_view(['GET' ])
@permission_classes([AllowAny, ])
def showAllDepartments(request):
    departments=department.objects.all().values()
    return JsonResponse(list(departments), safe=False)

@api_view(['GET' ])
@permission_classes([AllowAny, ])
def showProductsInCategory(request,id):
    products=product.objects.select_related().filter(product_category__category_id=id).values()
    return JsonResponse(list(products), safe=False)

@api_view(['GET'])
@permission_classes([AllowAny, ])
def showAllCategories(request):
    categories=category.objects.all().values()
    return JsonResponse(list(categories), safe=False)

@api_view(['GET'])
@permission_classes([AllowAny, ])
def showCategoriesByDepartment(request, department_id):
    categories=category.objects.filter(department_id=department_id).values()
    return JsonResponse(list(categories), safe=False)

@api_view(['GET'])
@permission_classes([AllowAny, ])
def countProductsInCategory(request, id):
    productsCount=product.objects.select_related().filter(product_category__category_id=id).count();
    return JsonResponse(productsCount, safe=False)

@api_view(['GET'])
@permission_classes([AllowAny, ])
def generateUniqueId(request):
    return JsonResponse({"GeneratedId"})

@api_view(['GET'])
def getCartItems(request, cart_id):
    print(cart_id)
    cart=shopping_cart.objects.filter(cart_id=cart_id).select_related('product').values('item_id','cart_id','attributes','quantity','buy_now','added_on','product__name','product__price','product__description','product__image')
    return JsonResponse(list(cart), safe=False)

@api_view(['POST'])
def addProductToCart(request):
    data=request.data
    cartId=data.get("cartId")
    productId=data.get("productId")
    quantity=data.get("quantity")
    entry=shopping_cart.objects.filter(cart_id=cartId,product_id=productId).values()
    if(entry.exists()):
        print(entry)
        #update
    else:
        cart=shopping_cart(cart_id=cartId,product_id=productId,quantity=quantity,added_on=timezone.now())
        cart.save()
        finalcart=shopping_cart.objects.filter(cart_id=cartId).select_related('product').values('item_id','cart_id','attributes','quantity','buy_now','added_on','product__name','product__price','product__description','product__image')
    return JsonResponse(list(finalcart), safe=False)

@api_view(['POST'])
@permission_classes([AllowAny, ])
def createCustomer(request):
    print("create new customer")
    name = request.data['username']
    password = request.data['password']
    email = request.data['email']
    mob_phone = request.data['mobile']
    userCustomer=customer(name=name,password=password,email=email,mob_phone=mob_phone)
    userCustomer.save()
    user=customer.objects.filter(email=email).values()
    return JsonResponse(list(user), safe=False)


@api_view(['POST'])
@permission_classes([AllowAny, ])
def login_user(request):
    try:
        email = request.data['email']
        password = request.data['password']
        user = customer.objects.get(email=email,password=password)
        if user:
            print(user)
            try:
                payload = jwt_payload_handler(user)
                token = jwt.encode(payload, settings.SECRET_KEY)
                user_details = {}
                user_details['name'] = "%s" % (
                    user.name
                )
                user_details['token'] = token
                return Response(user_details, status=status.HTTP_200_OK)

            except Exception as e:
                raise e
        else:
            res={
                "error": "cannot authenticate with the given credentials or the account has been deactivated"
            }
            return Response(res, status=status.HTTP_403_FORBIDDEN)
        print(user)
    
    except KeyError:
        res={
            'error':'please provide an email and a password'
        }
        return Response(res)


        
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




