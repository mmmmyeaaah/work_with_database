from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', 'name')

    if sort == 'min_price':
        phones = Phone.objects.all().order_by('price')
        context = {
            'phones': phones
        }
        return render(request, template, context)

    if sort == 'max_price':
        phones = Phone.objects.all().order_by('-price')
        context = {
            'phones': phones
        }
        return render(request, template, context)

    else:
        phones = Phone.objects.all().order_by(sort)
        context = {
            'phones': phones
        }
        return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_obj = Phone.objects.filter(slug=slug)
    phones = [ph for ph in phone_obj]
    phone = phones[0]
    context = {
        'phone': phone
    }
    return render(request, template, context)
