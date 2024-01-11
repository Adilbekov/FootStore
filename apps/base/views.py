from django.shortcuts import render
from apps.telegram_bot.views import get_text

from apps.base import models
from apps.secondary.models import Slide, Quality, Foot, Advertising, BlogPost
from apps.goods.models import Donuts, Bread, Cake, LowPrice
# Create your views here.

def index(request):
    # secondary
    blog_post = BlogPost.objects.all()
    slide = Slide.objects.latest('id')
    quality = Quality.objects.latest('id')
    foot = Foot.objects.all()
    advertising = Advertising.objects.all()
    
    # goods
    donuts = Donuts.objects.all()
    bread = Bread.objects.all()
    cake = Cake.objects.all()
    all_products = list(donuts) + list(bread) + list(cake)
    low_price = LowPrice.objects.all()

    # base
    image = models.BackImage.objects.latest('id')
    clients = models.Clients.objects.all()
    ass = models.Ass.objects.latest('id')
    return render(request, 'home/index.html', locals())


def contact(request):
    blog_post = BlogPost.objects.all()
    ass = models.Ass.objects.latest('id')
    image = models.BackImage.objects.latest('id')
    advertising = Advertising.objects.all()



    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contacts = models.Contact.objects.create(name=name, email=email, subject=subject, message=message)
        
        get_text(f"""
оставлена Обратная связь 
Имя: {name}
Почта {email}
Обьект {subject}
Сообщение {message}"""
        )
    return render(request, 'pages/contact.html', locals())


def reservations(request):
    image = models.BackImage.objects.latest('id')
    ass = models.Ass.objects.latest('id')

    advertising = Advertising.objects.all()
    blog_post = BlogPost.objects.all()
    clients = models.Clients.objects.all()
    if request.method == 'POST':
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        person = request.POST.get('person')
        phone = request.POST.get('phone')
        data = request.POST.get('date')
        time = request.POST.get('time')
        message = request.POST.get('message')
        data = models.Reservations.objects.create(name=name, email=email, person=person, phone=phone, data=data, time=time, message=message)

    return render(request, 'pages/reservation.html', locals())



