from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtistViewSet, ArtworkViewSet, ExhibitionViewSet

router = DefaultRouter()
router.register(r'artists', ArtistViewSet, basename='artists')
router.register(r'artworks', ArtworkViewSet ,basename='artworks')
router.register(r'exhibitions', ExhibitionViewSet, basename='exhibitions')

urlpatterns = [
    path('', include(router.urls)),
]
