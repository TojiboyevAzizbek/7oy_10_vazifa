from django.shortcuts import render
from . import models

"""furnctions for models and views  """

def index(request):
    posts = models.Post.objects.all()
    context = {
        'posts':posts,
    }
    return render(request, 'front/index.html', context)




def categories(request):
    """furnction for categories  """
    categories = models.Category.objects.all()
    posts = models.Post.objects.all()
    context = {
        'categories':categories,
        'posts':posts,
    }
    return render(request, 'front/category.html', context)


def posts(request):
    """furnction for post  """
    posts = models.Post.objects.all()
    comments = models.Comment.objects.all()
    context = {
        'posts':posts,
        'comments':comments,
    }
    return render(request, 'front/post.html', context)


def contact(request):
    """furnction for contact  """
    if request.method == 'POST':
        try:
            models.Contact.objects.create(
                name=request.POST['name'],
                phone=request.POST['phone'],
                email=request.POST['email'],
                body=request.POST['message']
            )
        except:
            ...
    return render(request, 'front/contact.html')