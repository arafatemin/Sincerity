from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
@login_required(login_url = "not_account")

def gallery(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()

    paginator = Paginator(Photo.objects.all(), 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {
        'categories': categories,
        'photos': photos,
        'page_obj': page_obj,
        'category': category,   # tıklanan ismi üst kısımda göstermek için
        }
    return render(request, 'photos/gallery.html', context)



@login_required(login_url = "not_account")
def addphoto(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None
        for image in images:
            photo = Photo.objects.create(
                category=category,
                description=data['description'],
                image=image,
            )
        return redirect('gallery')
    context = {
        'categories': categories,
    }
    return render(request, 'photos/addphoto.html', context)