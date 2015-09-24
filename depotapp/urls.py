from django.conf.urls import url, patterns, include
from .models import *
from .views import *
from rest_framework import serializers, viewsets, routers

# Serializers define the API representation.
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product 
        fields = ('title', 'description','image_url','price','date_available')
#class LineItemSerializer(serializers.HyperlinkedModelSerializer):
#	product = ProductSerializer()
class LineItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = LineItem
		fields = ('product','unit_price','quantity')


# ViewSets define the view behavior.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
class LineItemViewSet(viewsets.ModelViewSet):
#	queryset = request.session['cart'].items()
	queryset = LineItem.objects.all()
	serializer_class = LineItemSerializer


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'Product', ProductViewSet)
router.register(r'LineItem', LineItemViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


urlpatterns +=[

    url(r'^product/create/$', create_product, name='create_product'),
    url(r'^product/list/$', list_product, name='list_product'),
    url(r'^product/edit/(?P<id>[^/]+)/$', edit_product, name='edit_product'),
    url(r'^product/view/(?P<id>[^/]+)/$', view_product, name='view_product'),
    
]
urlpatterns += [
	url(r'^indexlog/$',indexlog),
	url(r'^store/$',store_view,name='store_view'),
	url(r'^cart/view/$',view_cart,name='view_cart'),
	url(r'^cart/add/(?P<id>\d+)$',add_to_cart,name='add_to_cart'),
	url(r'^cart/clean/$',clean_cart,name='clean_cart'),
]
