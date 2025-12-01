from django.db.models import Q, F
from django.shortcuts import render
from .models import Product

def queries_view(request):
    q1 = Product.objects.filter(Q(price__gt=50) | Q(quantity__lt=10))
    q2 = Product.objects.filter(Q(name__icontains="phone") & Q(price__gte=100) & Q(price__lte=500))
    q3 = Product.objects.filter(~Q(price__lt=200))

    updated_price = Product.objects.update(price=F("price") + 10)
    f2 = Product.objects.filter(price__gt=F("quantity"))
    updated_qty = Product.objects.update(quantity=F("quantity") + 1)

    return render(request, "results.html", {})
