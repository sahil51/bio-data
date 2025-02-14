from django.shortcuts import render
from .models import Hero_page
# Create your views here.
def home(request):
    hero = Hero_page.objects.filter(is_active=True).first()
    sociallink = hero.social_links.all() if hero else []
    context = {
        'hero':hero,
        'links':sociallink
    }
    return render(request,'base.html',context)