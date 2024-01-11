from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from apps.base.models import Ass, BackImage
from apps.secondary.models import Advertising, BlogPost
from apps.goods import models 
# Create your views here.

def shop(request):
    blog_post = BlogPost.objects.all()
    advertising = Advertising.objects.all()
    ass = Ass.objects.latest('id')
    image = BackImage.objects.latest('id')

    donuts = models.Donuts.objects.all()
    bread = models.Bread.objects.all()
    cake = models.Cake.objects.all()
    all_products = list(donuts) + list(bread) + list(cake)

    
    posts_per_page = 4
    
    paginator = Paginator(all_products, posts_per_page)
    
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # Если номер страницы не является целым числом, поставим его на первую страницу
        posts = paginator.page(1)
    except EmptyPage:
        # Если номер страницы больше максимального, поставим на последнюю страницу
        posts = paginator.page(paginator.num_pages)
    
    return render(request, 'shop/shop.html', locals())



def shop_detail(request, id):
    blog_post = BlogPost.objects.all()
    advertising = Advertising.objects.all()
    ass = Ass.objects.latest('id')
    image = BackImage.objects.latest('id')

    donuts = models.Donuts.objects.all()
    bread = models.Bread.objects.all()
    cake = models.Cake.objects.all()
    all_products = list(donuts) + list(bread) + list(cake)

    
    donuts1 = models.Donuts.objects.get(id=id)
    bread2 = models.Bread.objects.get(id=id)
    cake3 = models.Cake.objects.get(id=id)
    # all_product = list(donuts1) + list(bread2) + list(cake3)

    for all_product in donuts1,bread2,cake3:
        return render(request, 'shop/shop-details.html', locals())