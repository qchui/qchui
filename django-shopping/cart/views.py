from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .models import CartItem
from userapp.models import UserInfo


# Create your views here.
class AddCartView(View):
    def post(self, request):
        # 获取当前操作类型
        flag = request.POST.get('flag', )
        goodsid = request.POST.get('goodsid', )
        colorid = request.POST.get('colorid', )
        sizeid = request.POST.get('sizeid', )
        count = request.POST.get('count', )
        user = request.session.get('user', '')

        cart = CartItem.objects.filter(goodsid=goodsid, colorid=colorid, sizeid=sizeid)[0]

        if cart:
            print(count)
            if count == '0':
                cart.delete()
            else:
                cart.count = count
                cart.save()
        else:
            CartItem.objects.create(goodsid=goodsid, colorid=colorid, sizeid=sizeid, user=user, count=count)

        return HttpResponseRedirect('/cart/queryAll')


class QueryALlView(View):
    def get(self, request):
        user = request.session.get('user', '')
        cartlist = CartItem.objects.filter(user=user)

        return render(request, 'cart.html', {'cartlist': cartlist})
