from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,base_name='helloviewset')
router.register('profile',views.UserProfileViewSet,base_name='userprofile')
router.register('login',views.LoginViewSet,base_name='login')
router.register('feed',views.ProfileFeedItemViewSet,base_name='feed')

urlpatterns = [
    path('hello/',views.HelloApiView.as_view(),name='helloapi'),
    path('',include(router.urls))
]
