from django.urls import include, path
from rest_framework import routers

from . import views

# router = routers.DefaultRouter()
# router.register('single', views.MessageViewSet)

message_list = views.MessageViewSet.as_view({
    'get': 'list',
})
single_message_detail = views.MessageViewSet.as_view({
    'get': 'retrieve'
})

create_message = views.MessageViewSet.as_view({
    'post': 'create'
})

urlpatterns = [
    path('single/<int:pk>/', single_message_detail),
    path('list/<int:page>/', message_list),
    path('create/', create_message)
]