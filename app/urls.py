from django.urls import path

from . import views

urlpatterns = [
    path('', views.SinglePodList.as_view(), name='index'),
    path('detail/<int:pk>/', views.SinglePodDetail.as_view(), name='detail'),
    path('order/', views.create_order, name='create_order'),
    path('review/', views.create_review, name='create_review'),
    path('liquidlist/', views.LiquidList.as_view(), name='liquid_list'),
    path('LiquidDetail/<int:pk>', views.LiquidDetail.as_view(), name='liquid_detail'),
    path('Liquidorder/', views.create_order_liquid, name='create_order_liquid')

]