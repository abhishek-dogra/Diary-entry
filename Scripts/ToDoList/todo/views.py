from django.shortcuts import render

from .models import todoItem

from django.http import HttpResponseRedirect

from django.utils import timezone
# Create your views here.
def TheList(request):
    all_items = todoItem.objects.all()
    items={"all_items":all_items}
    return render(request,"todo/TheList.html",items)

def addItem(request):
    new_item=request.POST["content"]
    add_time=timezone.now()
    todoItem.objects.create(item_text=new_item,added_date=add_time)
    all_items = todoItem.objects.all()
    print(all_items)
    items={"all_items":all_items}
    return HttpResponseRedirect("/")

def delItem(request,item_id):
    todoItem.objects.get(id=item_id).delete()
    return HttpResponseRedirect("/")
