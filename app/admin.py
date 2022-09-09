from django.contrib import admin

from .models import Manufacturer, SinglePod, SinglePodImages, Taste, SinglePodStock, Order, OrderDetail, ManufacturerLiquid, Liquid, LiquidImages, LiquidTaste, LiquidStock, OrderLiquid, LiquidOrderDetail, Review

admin.site.register(Manufacturer)
admin.site.register(SinglePod)
admin.site.register(SinglePodImages)
admin.site.register(Taste)
admin.site.register(SinglePodStock)
admin.site.register(Order)
admin.site.register(OrderDetail)

admin.site.register(ManufacturerLiquid)
admin.site.register(Liquid)
admin.site.register(LiquidImages)
admin.site.register(LiquidTaste)
admin.site.register(LiquidStock)
admin.site.register(OrderLiquid)
admin.site.register(LiquidOrderDetail)
admin.site.register(Review)
