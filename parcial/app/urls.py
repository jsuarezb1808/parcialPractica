from django.urls import path
#se importa las vistas asi debido 
#a que es mas facil de visualizar 
# en pantalla dividida
from .views import HomePageView,AboutPageView
from .views import ContactPageView,ProductIndexView
from .views import ProductShowView,ProductCreateView
from .views import CartView,CartRemoveAllView

urlpatterns = [
    path('', HomePageView.as_view(), name='base'),
   ]
