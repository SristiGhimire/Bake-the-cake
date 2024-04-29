from django.shortcuts import render, HttpResponse,redirect
from .models import *
from rest_framework import generics
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings 
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.generic import ListView,CreateView
from app.serializer import *
from .serializer import *
from rest_framework.response import Response
from .decorators import login_required


# Create your views here.



def index(request):
    shop = Shop.objects.all()[:4]
    decoration = Decoration.objects.all()[:4]
    context= {"shop":shop, "decoration" : decoration}
    return render(request, 'app/index.html', context)

def login(request):
    return render(request, 'app/login.html')

def contact(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')  # method1
        lname = request.POST['lname'] # second method
        # print(lname)
        email = request.POST['email']
        message = request.POST['message']

        # contact_obj = Contact.objects.create(firstName =fname, lastName =lname, email = email, message = message)  # method 1 for data stire on db
        contact_obj = Contact(firstName =fname, lastName =lname, email = email, message = message) # second method for data stire on db
        contact_obj.save()
        
        # send mail with customer query
        subject  ="Customer Query "
        message =f"User Name :{fname} {lname} message : {message}"
        email_from = settings.EMAIL_HOST_USER
        user_email = ['ghimiresristi9@gmail.com',email]
        send_mail(subject, message, email_from, user_email)
        return redirect('contact')

        
    else:
        return render(request, 'app/contact.html')

@login_required
def shop(request):
    shop = Shop.objects.all()
    context= {"shop":shop}
    return render(request, 'app/shop.html', context)

@login_required
def product(request, id=None):
    item = Shop.objects.get(id=id) # get is used for retrive single item from db
    products =Shop.objects.all()[:4]
    return render(request, 'app/product.html',{'product_detail':item,'products':products})

def decoration(request):
    decorations = Decoration.objects.all()
    context = {"decorations": decorations}
    return render(request, 'app/decoration.html', context)

def decorationdetail(request, id=None):
    item = Decoration.objects.get(id=id)
    products = Decoration.objects.all()[:4]
    return render(request, 'app/decorationdetail.html', {'product_detail': item, 'products': products})


# def cake(request):
#     cake = Cake.objects.all()
#     context= {"cake":cake}
#     return render(request, 'app/cake.html', context)

# def cupcake(request):
#     cupcake = Cupcake.objects.all()
#     context= {"cupcake":cupcake}
#     return render(request, 'app/cupcake.html', context)

# def brownie(request):
#     brownie =   Brownie.objects.all()
#     context= {"brownie":brownie}
#     return render(request, 'app/brownie.html', context)

# def weddingcake(request):
#     weddingcake = weddingcake.objects.all()
#     context= {"weddingcake":weddingcake}
#     return render(request, 'app/weddingcake.html', context)

def searchbar(request):
    if request.method=="GET":
        query = request.GET.get('query')
        if query:
            products = Shop.objects.filter(name__icontains=query)
            context={"products": products}
            return render(request,'app/searchbar.html', context)
        else:
            print("No result")
            return request(request,'searchbar.html',{})


from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email =  request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print('Username exists! try another username..')
                return redirect('login')

            elif User.objects.filter(email=email).exists():  # Use exists() instead of existed()
                print('Email is already taken! try another one')
                return redirect('login')

            else:
                user = User.objects.create_user(username=username, email=email, password=password1)  # Use create_user instead of create_creaeuser
                user.save()
                return redirect('login')
        else:
            print('password did not matched!..')
            return redirect('login')
    else:
        return render(request, 'app/login.html')



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            print('Invalid user')
            return redirect('login')
    
    else:
        return render(request, 'app/login.html')


# for logout
def userlogout(request):
    auth.logout(request)
    messages.info(request, "logout successfully..")
    return redirect('index')


def error(request, exception):
    return render(request, 'app/error.html')


#for api
class ShopListView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ShopSerializers(queryset, many= True)
        return Response({"data": serializer.data, "msg": "successful"})

class ShopRetrieveUpdatedelete(generics.RetrieveAPIView, generics.DestroyAPIView, generics.UpdateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    lookup_field = 'pk'


    






