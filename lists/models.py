from django.db import models
def new_list(request):
    list_user=List.objects.create()
    Item.objects.create(text=request.POST['item_text'],list=list_user)
    return redirect('/lists/the-new-page/')
class List(models.Model):
    pass
class Item(models.Model):
    text=models.TextField(default='')
    list=models.ForeignKey(List,on_delete=models.CASCADE,default=None)
# Create your models here.
