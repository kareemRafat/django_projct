from django.urls import path
from . import views

# to use the name as about:index - about:show
app_name = 'about'

urlpatterns = [
   path('' , views.index , name = 'index'),
   path('show/<str:id>' , views.show , name = 'show')
]