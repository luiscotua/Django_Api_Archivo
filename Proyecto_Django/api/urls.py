from django.urls import include, path
from django.conf.urls import include, url
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'clasificadores', views.ClasificadorViewSet, 'clasificador')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/rest-auth/', include('rest_auth.urls')),
    url(r'^clasificadordata/(?P<pk>\d+)$', views.clasificadorData.as_view()),
]