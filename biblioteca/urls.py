from django.urls import path, include
from core.views import AutorDetail, AutorViewSet, CategoriaDetail, LivroDetail, LivroViewSet, ColecaoViewSet, ColecaoDetail, CategoriaViewSet
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Documentação da API',
        default_version='v1',
        description='Documentação da API ',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email='contact@snippets.local'),
        license=openapi.License(name='BSD License')
    ),
    public=True
)

router = routers.DefaultRouter()
router.register('livros', LivroViewSet)
router.register('colecoes', ColecaoViewSet)
router.register('autor', AutorViewSet)
router.register('categoria', CategoriaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('livro/<int:pk>', LivroDetail.as_view()),
    path('colecao/<int:pk>', ColecaoDetail.as_view()),
    path('autor/<int:pk>', AutorDetail.as_view()),
    path('categoria/<int:pk>', CategoriaDetail.as_view()),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]
