from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# my imports
from apps.base import models
from apps.secondary.models import Advertising, BlogPost, Comments, SendComment, Quality
# Create your views here.

def about(request):
    clients = models.Clients.objects.all()
    advertising = Advertising.objects.all()
    blog_post = BlogPost.objects.all()
    blog_post = BlogPost.objects.all()

    image = models.BackImage.objects.latest('id')
    ass = models.Ass.objects.latest('id')
    quality = Quality.objects.latest('id')

    return render(request, 'pages/about.html', locals())

def blog(request):
    ass = models.Ass.objects.latest('id')
    image = models.BackImage.objects.latest('id')

    advertising = Advertising.objects.all()
    blog_post = BlogPost.objects.all()
    posts = BlogPost.objects.all()
    all_posts = BlogPost.objects.all()

    posts_per_page = 3
    paginator = Paginator(all_posts, posts_per_page)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # Если номер страницы не является целым числом, поставим его на первую страницу
        posts = paginator.page(1)
    except EmptyPage:
        # Если номер страницы больше максимального, поставим на последнюю страницу
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/blogs.html', locals())


def blog_detiles(request, id):
    photo = models.BackImage.objects.latest('id')
    ass = models.Ass.objects.latest('id')

    advertising = Advertising.objects.all()
    blog_post = BlogPost.objects.all()
    comments = Comments.objects.all()

    blog = BlogPost.objects.get(id=id)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment_text = request.POST.get('message')
        all_comment = SendComment.objects.create(name=name, email=email, comment=comment_text)

    return render(request, 'blog/blog-details.html', locals())


def bag(request):
    return render(request, 'pages/404.html', locals())