from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, base_name='logn')
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello_view', views.HelloApiView.as_view()),
    path('', include(router.urls))
]
