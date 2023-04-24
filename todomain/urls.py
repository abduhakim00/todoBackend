from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

router = DefaultRouter()

router.register('',views.TodoViewSet, basename="todo")

urlpatterns = [
    path('tags/', views.TagApiView.as_view()),
    path('tagguh/', views.TagView)
]

urlpatterns += router.urls