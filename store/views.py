from ast import Or
from http.client import HTTPResponse
from unicodedata import category
from django.shortcuts import HttpResponse
from itertools import product
from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
import json
import datetime
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from oracledb import DatabaseError
from store.forms import CommentForm, CreateUserForm
from store.models import *
from django.db import transaction, connection


# need to create forms and models

# Create your views here.

# Store view
# case 1: user đã login -> lấy order của user đó -> lấy tất cả các item trong order đó -> lấy cartItems từ order đó
# case 2: user chưa login -> tạo order mới -> để cart items = 0 và ko có mặt hàng nào trong order đó

# -> Sau đó, lấy tất cả các sản phẩm từ cơ sở dữ liệu và trả về một trang HTML với thông tin về các sản phẩm và số lượng mặt hàng trong giỏ hàng.


#def call_update_stock_before_order(order_id):
 #  with connection.cursor() as cursor:
  #    cursor.callproc('update_stock_before_order', [order_id])

def store(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0, 'shipping': False}
        cartItems = order['get_cart_items']
    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/store.html', context)

# home view tương tự như store view nhưng chỉ lấy 4 sản phẩm đầu tiên
# và 3 bài viết đầu tiên -> sau đó trả về một trang HTML với thông tin về các sản phẩm và số lượng mặt hàng trong giỏ hàng.


def home(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0, 'shipping': False}
        cartItems = order['get_cart_items']
    products = Product.objects.all()[:4]
    articles = Post.objects.all()[:3]
    context = {'articles': articles,
               'products': products, 'cartItems': cartItems}
    return render(request, 'store/home.html', context)

# product view xử lý yêu cầu của người dùng để xem chi tiết sản phẩm
# -> sau đó trả về một trang HTML với thông tin về sản phẩm và các sản phẩm liên quan, sử dụng slug để xác định sản phẩm cụ thể và
# lấy các sản phẩm liên quan từ cùng một danh mục.
# -> nếu sản phẩm không tồn tại, trả về một trang 404


def product(request, slug):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0, 'shipping': False}
        cartItems = order['get_cart_items']
    print('Product slug', slug)
    product = get_object_or_404(Product, slug=slug)
    related_products = Product.objects.filter(category=product.category)[:4]
    context = {'product': product, 'related_products': related_products, 'cartItems': cartItems}
    return render(request, 'store/product.html', context)

# blog_article view xử lý yêu cầu của người dùng để xem chi tiết bài viết
# -> sau đó trả về một trang HTML với thông tin về bài viết và các bài viết liên quan, sử dụng slug để xác định bài viết cụ thể và
# lấy các bài viết liên quan từ cùng một danh mục.
# -> nếu bài viết không tồn tại, trả về một trang 404


def blog_article(request, slug):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0, 'shipping': False}
        cartItems = order['get_cart_items']
    print('post slug', slug)
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm(request.POST, instance=post)
    if (request.method == 'POST'):
        if (form.is_valid):
            body = form.cleaned_data['body']
            print(body)
            c = Comment(post=post, body=body, date_commented=datetime.now())
            c.save()
            return redirect('store/blog_article.html')
        else:
            print('form is invalid')

    context = {'post': post, 'form': form, 'cartItems': cartItems}
    return render(request, 'store/blog_article.html', context)

# blog view trả về một trang HTML với tất cả các bài viết


def blog(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0, 'shipping': False}
        cartItems = order['get_cart_items']
    posts = Post.objects.all()
    context = {'posts': posts, 'cartItems': cartItems}
    return render(request, 'store/blog.html', context)

# contact view trả về một trang HTML với thông tin liên hệ


def contact(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0, 'shipping': False}
        cartItems = order['get_cart_items']   
    context = {'cartItems': cartItems}
    # return render(request, 'store/contact.html')
    return render(request, 'store/contact.html', context)

# cart view trả về một trang HTML với thông tin về các sản phẩm trong giỏ hàng (mặt hàng, đơn hàng, số lượng)


def cart(request):
    # cart o payement wkol maysyro ken b customer is already connected sinn yatl3o 0
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0, 'shipping': False}
        cartItems = order['get_cart_items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)

# checkout view
# -> nếu người dùng đã đăng nhập, lấy đơn hàng của người dùng đó và số lượng mặt hàng trong giỏ hàng
# -> nếu người dùng chưa đăng nhập, trả về một trang HTML với các sản phẩm trong giỏ hàng (mặt hàng, đơn hàng, số lượng) là 0

@transaction.atomic
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0, 'shipping': False}
        cartItems = order['get_cart_items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)

# updateItem view xử lý yêu cầu của người dùng để thêm hoặc xóa một sản phẩm trong giỏ hàng
# -> sau đó trả về một JSON với thông tin về sản phẩm đã được thêm hoặc xóa
# Lưu thay đổi vào csdl

@transaction.atomic
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action : ', action)
    print('productId : ', productId)

    customer = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)
    if (action == 'add'):
        orderItem.quantity = (orderItem.quantity + 1)
    elif (action == 'remove'):
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)

# processOrder view xử lý yêu cầu của người dùng để thanh toán
# -> kiểm tra người dùng -> Lấy đơn hàng hiện tại của người dùng hoặc tạo một đơn hàng mới nếu không tồn tại.
# -> Lấy tổng số tiền của đơn hàng từ dữ liệu đã được chuyển đổi -> gán ID -> kiểm tra tiền -> lưu thay đổi vào csdl
# -> kiểm tra thuộc tính của đơn hàng -> kiểm tra yêu cầu giao hàng -> tạo địa chỉ giao hàng mới

def call_update_stock_before_order(order_id):
   with connection.cursor() as cursor:
     cursor.callproc('update_stock_before_order', [order_id])


def set_serializable_isolation_level():
    with connection.cursor() as cursor:
        cursor.execute('SET TRANSACTION ISOLATION LEVEL SERIALIZABLE')
@transaction.atomic
def processOrder(request):
    try:
        set_serializable_isolation_level()
        with transaction.atomic():
            print('Received data:', request.body)
            transaction_id = datetime.datetime.now().timestamp()
            data = json.loads(request.body)

            if request.user.is_authenticated:
                customer = request.user
                print(f"Processing order for authenticated user: {customer.username}")

                order, created = Order.objects.get_or_create(
                    customer=customer, complete=False)
                if created:
                    print(f"Created new order with ID: {order.id}")
                else:
                    print(f"Found existing order with ID: {order.id}")

                total = float(data['form']['total'])
                order.transaction_id = transaction_id

                if total == order.get_cart_total:
                    order.complete = True
                    print(f"Order total matches cart total. Marking order {order.id} as complete.")
                order.save()
                print(f"Order {order.id} saved with transaction ID: {transaction_id}")

                # Gọi stored procedure để cập nhật số lượng tồn kho
                call_update_stock_before_order(order.id)

                if order.shipping:
                    print(f"Creating shipping address for order {order.id}")
                    ShippingAddress.objects.create(
                        customer=customer,
                        order=order,
                        address=data['shipping']['address'],
                        city=data['shipping']['city'],
                        state=data['shipping']['state'],
                        zipcode=data['shipping']['zipcode'],
                    )
                    print(f"Shipping address created for order {order.id}")

            else:
                print('User is not logged in.')
                return JsonResponse('User is not logged in.', status=401, safe=False)

        print("Order processing completed successfully.")
        return JsonResponse('Payment complete!', safe=False)

    except DatabaseError as e:
        # Rollback transaction in case of database error
        transaction.rollback()
        print('Database error occurred:', e)
        return JsonResponse({'error': 'Database error: ' + str(e)}, status=500, safe=False)
    except Exception as e:
        # Rollback transaction in case of other errors
        transaction.rollback()
        print('Error occurred:', e)
        return JsonResponse({'error': 'Error: ' + str(e)}, status=500, safe=False)

# Login page view xử lý yêu cầu của người dùng để đăng nhập
# -> nếu người dùng đã đăng nhập, chuyển hướng người dùng đến trang chủ
# -> nếu người dùng chưa đăng nhập, kiểm tra yêu cầu của người dùng -> kiểm tra thông tin đăng nhập
# -> nếu thông tin đăng nhập hợp lệ, kiểm tra yêu cầu có phải là POST hay không? -> POST -> xử lý form đăng nhập
# -> lấy tên người dùng và mật khẩu từ form -> xác thực -> kiểm tra trùng lặp người dùng -> tồn tại -> đăng nhập -> chuyển hướng người dùng đến trang chủ
# -> không tồn tại -> thông báo lỗi


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'auth/login.html', context)

# Register page view xử lý yêu cầu của người dùng để đăng ký
# -> kiểm tra người dùng đã đăng nhập chưa -> nếu rồi thì chuyển về home
# -> chưa đăng nhập -> tạo form đăng ký -> kiểm tra yêu cầu của người dùng -> kiểm tra form đăng ký
# trả về trang HTML auth/register.html với form đăng ký


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

        context = {'form': form}
        return render(request, 'auth/register.html', context)

# logout page view xử lý yêu cầu của người dùng để đăng xuất
# nhận đăng xuất -> chuyển hướng người dùng đến trang chủ


def logoutUser(request):
    logout(request)
    return redirect('home')


def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        quantity = request.POST['quantity']
        # Now you can add the product to the cart


