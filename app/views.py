from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, DeleteView, CreateView

from .models import SinglePod, SinglePodStock, Order, OrderDetail, \
    ManufacturerLiquid, Liquid, LiquidImages, LiquidTaste, LiquidStock, OrderLiquid, LiquidOrderDetail, Review


# За один день это точно не сделать 😏.


class SinglePodList(ListView):
    model = SinglePod
    queryset = SinglePod.objects.all()
    template_name = 'app/single-pod-list.html'
    context_object_name = 'single_pods'
    paginate_by = 1


class SinglePodDetail(DetailView):
    model = SinglePod
    template_name = 'app/single-pod-detail.html'
    context_object_name = 'single_pod'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        single_pod_id = self.kwargs.get('pk')

        single_pod_stocks = SinglePodStock.objects.filter(taste__single_pod_id=single_pod_id, quantity__gte=1)

        context['single_pod_stocks'] = single_pod_stocks

        return context


def create_order(request):

    if request.method == "POST":

        single_pod_stock_id = request.POST['single_pod_stock']
        quantity = request.POST['quantity']
        
        single_pod_stock = SinglePodStock.objects.get(id=single_pod_stock_id)

        single_pod_stock.quantity = single_pod_stock.quantity - int(quantity)
        single_pod_stock.save()

        return redirect('index')






class LiquidList(ListView):
    model = Liquid
    queryset = Liquid.objects.all()
    template_name = 'app/liquid-list.html'
    context_object_name = 'liquids'






class LiquidDetail(DetailView):
    model = Liquid
    template_name = 'app/liquid_detail.html'
    context_object_name = 'liquids'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        liquid_id = self.kwargs.get('pk')

        liquid_stocks = LiquidStock.objects.filter(taste__liquid_id=liquid_id, quantity__gte=1)

        context['liquid_stocks'] = liquid_stocks

        return context


def create_order_liquid(request):
    if request.method == "POST":
        liquid_stock_id = request.POST['liquid_stock']
        quantity = request.POST['quantity']

        liquid_stock = LiquidStock.objects.get(id=liquid_stock_id)

        liquid_stock.quantity = liquid_stock.quantity - int(quantity)
        liquid_stock.save()

        return redirect('index')



def create_review(reguest):
    if reguest.method == 'POST':
         single_pod_id = reguest.POST['single_pod_id']
         massage = reguest.POST['massage']
         review = Review(user_id=1, single_pod_id=single_pod_id, maasege=massage)
         review.save()

         return redirect('detail', pk=single_pod_id)