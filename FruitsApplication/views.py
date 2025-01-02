from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from FruitsApplication.models import Item


# Create your views here.
def home(request):
    # Fetch all Item instances from the database
    items = Item.objects.all()

    # Pass the items to the template
    return render(request, 'index.html', {'items': items})
def index(request):
    return render(request, 'index.html')
def item_detail(request, item_id):
    # Fetch the item with the given ID, or return a 404 if not found
    item = get_object_or_404(Item, pk=item_id)

    # Pass the item to the template
    return render(request, 'detail_view.html', {'item': item})
def fruit(request):
    return render(request, 'fruit.html')
def service(request):
    return render(request, 'service.html')
def contact(request):
    return render(request, 'contact.html')