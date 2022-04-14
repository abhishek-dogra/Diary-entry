from django.urls import path
from . import views

app_name='todo'

urlpatterns=[
path('',views.TheList),
path('addItem/',views.addItem),
path('delItem/<int:item_id>',views.delItem)
]
