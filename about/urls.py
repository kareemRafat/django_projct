from django.urls import path
from . import views

# to use the name as about:index - about:show
app_name = 'about'

urlpatterns = [
   path('' , views.index , name = 'index'),
   path('show/<int:id>' , views.show , name = 'show'),
   path('new-user/' , views.new_user , name = 'new-user')
]

# <int:id>  Path converters
# https://docs.djangoproject.com/en/5.0/topics/http/urls/#path-converters