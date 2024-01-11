from django.shortcuts import render
from apps.base.models import Ass, BackImage
from apps.secondary.models import Advertising, BlogPost
from apps.menu import models
# Create your views here.
def menu(request):
    advertising = Advertising.objects.all()
    ass = Ass.objects.latest('id')
    blog_post = BlogPost.objects.all()
    image = BackImage.objects.latest('id')

    # all products
    set_menu1 = models.SetFamily.objects.all()
    set_menu2 = models.SetCouple.objects.all()
    set_menu3 = models.SetIndivudal.objects.all()
    all_menu_products = list(set_menu1) + list(set_menu2) + list(set_menu3)
    # Fast Foot
    fast_food1 = models.FootPizza.objects.all()
    fast_food2 = models.FootBurger.objects.all()
    fast_food3 = models.FootPasta.objects.all()
    all_fast_food = list(fast_food1) + list(fast_food2) + list(fast_food3)
    # desert
    desert1 = models.DessertCake.objects.all()
    desert2 = models.DessertIceCream.objects.all()
    desert3 = models.DessertSnake.objects.all()
    all_deserts =  list(desert1) + list(desert2) + list(desert3)
    # Juise
    juice1 = models.JuiceCoffee.objects.all()
    juice2 = models.JuiceFruitJuice.objects.all()
    all_juice =  list(juice1) + list(juice2)
    return render(request, 'pages/menu.html', locals())