from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from main import models
from django.contrib import messages
from django.db.models import Q



@login_required(login_url='dashboard:log_in')
def index(request):
    categories = models.Category.objects.all()
    user = User.objects.last()
    context = {
        'categories': categories,
        'user': user,
    }
    return render(request, 'dashboard/index.html', context)



"""here has written about region"""

@login_required(login_url='dashboard:log_in')
def create_region(request):
    if request.method == "POST":
        try:
            name = request.POST['name']
            models.Region.objects.create(name=name)
            messages.success(request, 'Region created succesfully')
        except:
            messages.error(request, 'Something getting wrong')
    return render(request, 'dashboard/region/create.html')



@login_required(login_url='dashboard:log_in')
def list_region(request):
    regions = models.Region.objects.all()
    context = {'regions':regions}
    return render(request, 'dashboard/region/list.html', context)


def detail_region(request, id):
    region = models.Region.objects.get(id=id)
    context = {'region':region}
    return render(request, 'dashboard/region/detail.html', context)


@login_required(login_url='dashboard:log_in')
def edit_region(request, id):
    region = models.region.objects.get(id=id)
    if request.method =='POST':
        try:
            region.name = request.POST['name']
            region.save()
            messages.success(request, 'Region updated succesfully')
        except:
            messages.error(request, 'Something getting wrong')
        return redirect('dashboard:region_detail', region.id)
    context = {'region':region}
    return render(request, 'dashboard/region/edit.html', context)


def delete_region(request, id):
    try:
        models.Region.objects.get(id=id).delete()
        messages.error(request, 'Region deleted')
    except:
        messages.error(request, 'Something getting wrong')
    return redirect('dashboard:region_list')



"""Here has written about category"""

@login_required(login_url='dashboard:log_in')
def create_category(request):
    if request.method == "POST":
        try:
            name = request.POST['name']
            models.Category.objects.create(name=name,)
            messages.success(request, 'categoriya created succesfully')
        except:
            messages.error(request, 'Something getting wrong')
    return render(request, 'dashboard/category/create.html')


@login_required(login_url='dashboard:log_in')
def list_category(request):
    categories = models.Category.objects.all()
    context = {'categories':categories}
    return render(request, 'dashboard/category/list.html', context)


@login_required(login_url='dashboard:log_in')
def detail_category(request, id):
    category = models.Category.objects.get(id=id)
    context = {'category':category}
    return render(request, 'dashboard/category/detail.html', context)


@login_required(login_url='dashboard:log_in')
def edit_category(request, id):
    category = models.category.objects.get(id=id)
    if request.method =='POST':
        try:
            category.name = request.POST['name']
            category.save()
            messages.success(request, 'categoriya updated succesfully')
        except:
            messages.error(request, 'Something getting wrong')

        return redirect('dashboard:category_list', category.id)
    context = {'category':category}
    return render(request, 'dashboard/category/edit.html', context)


@login_required(login_url='dashboard:log_in')
def delete_category(request, id):
    try:
        models.Category.objects.get(id=id).delete()
        messages.error(request, 'c')
    except:
        messages.error(request, 'Something getting wrong')
    return redirect('dashboard:category_list')


""" Here has written about posts"""

@login_required(login_url='dashboard:log_in')
def create_post(request):
    users = models.User.objects.all()
    categories = models.Category.objects.all()
    regions = models.Region.objects.all()
    context = {
        'users':users,
        'categories':categories,
        'regions':regions
    }
    if request.method == 'POST':
       
            title = request.POST['title']
            body = request.POST['body']
            banner_img = request.FILES['banner_img']
            date = request.POST['date']
            user_id = request.POST['user_id']
            category_id = request.POST['category_id']
            region_id = request.POST['region_id']
            user = models.User.objects.get(id=user_id)
            category = models.Category.objects.get(id=category_id)
            region = models.Region.objects.get(id=region_id)
            post = models.Post.objects.create(
                title=title,
                body=body,
                banner_img=banner_img,
                date=date,
                user=user,
                region=region,
                category=category
                )

    return render(request, 'dashboard/post/create.html', context)


@login_required(login_url='dashboard:log_in')
def list_post(request):
    posts = models.Post.objects.all()
    context = {'posts': posts}
    return render(request, 'dashboard/post/list.html', context)


@login_required(login_url='dashboard:log_in')
def detail_post(request, id):
    post = models.Post.objects.get(id=id)
    context = {'post': post}
    return render(request, 'dashboard/post/detail.html', context)


@login_required(login_url='dashboard:log_in')
def edit_post(request, id):
    post = models.Post.objects.get(id=id)
    if request.method == 'POST':
        try:
            title = request.POST.get('title')
            body = request.POST.get('body')
            banner_img = request.POST.get('banner_img')
            date = request.POST.get('date')
            author = request.POST.get('author')
            category = request.POST.get('category')
            region = request.POST.get('region')
            models.Post.objects.filter(id=id).update(
                title=title,
                body=body,
                banner_img=banner_img,
                date=date,
                author=author,
                category=category,
                region=region
            )
            messages.success(request, 'post updated succesfully')
            return redirect('dashboard:detail_post', post.id)
        except:
            messages.error(request, 'Something getting wrong')

    return render(request, 'dashboard/post/edit.html', context={'post': post})


@login_required(login_url='dashboard:log_in')
def delete_post(request, id):
    try:
        models.Post.objects.filter(id=id).delete()
        messages.success(request, 'post deleted succesfully')
        return redirect('dashboard:list_post')
    except:
        messages.error(request, 'Something getting wrong')
    return render(request, 'dashboard/post/list.html')



"""Here has written about contact"""

@login_required(login_url='dashboard:log_in')
def list_contact(request):   
    contacts = models.Contact.objects.all()
    context = {'contacts':contacts}
    return render(request, 'dashboard/contact/list.html', context)


@login_required(login_url='dashboard:log_in')
def detail_contact(request, id):
    contacts = models.Contact.objects.get(id=id) 
    context = {'contacts':contacts}
    return render(request, 'dashboard/contact/detail.html', context)

@login_required(login_url='dashboard:log_in')
def edit_contact(request, id):
    contact = models.Contact.objects.get(id=id)
    if request.method == "POST":
        try:
            is_show = request.POST.get('is_show')  
            contact.is_show = is_show == 'on'
            contact.save()
            messages.success(request, 'information of contact updated succesfully')
        except:
            messages.error(request, 'Something getting wrong')
        return redirect('dashboard:contact_list')
    context = {'contact': contact}
    return render(request, 'dashboard/contact/edit.html', context)



""" Here has written about register, login and logout"""


def register(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            password_confirm = request.POST['password_confirm']
            if password == password_confirm:
                User.objects.create_user(
                    username=username,
                    password=password
                )
            messages.success(request, 'username created succesfully')
        except:
            messages.error(request, 'Something getting wrong')
            return redirect('dashboard:index')
    return render(request, 'dashboard/auth/register.html')


def log_in(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            messages.success(request, 'You are welcome!')
        except:
            messages.error(request, 'Something getting wrong')
        if user is not None:
            login(request, user)
            return redirect('dashboard:index')
        else:
            return render(request, 'dashboard/auth/login.html', {'error_message': 'Invalid username or password.'})
    else:
        return render(request, 'dashboard/auth/login.html')


def log_out(request):
    logout(request)
    return redirect('main:index')


def query(request):
    q = request.GET['q']
    posts = models.Post.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))
    region = models.Region.objects.filter(Q(name__icontains=q))
    category = models.Category.objects.filter(Q(name__icontains=q))
    contact = models.Contact.objects.filter(Q(name__icontains=q) | Q(email__icontains=q) | Q(phone__icontains=q))
    context = {
        'posts':posts,
        'region':region,
        'category':category,
        'contact':contact,
    }
    return render(request, 'dashboard/query.html', context)