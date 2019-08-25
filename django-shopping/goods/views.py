from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import *
import math
from untils.tools.decorator import *



class IndexVie(View):
    def get(self, request, cid=1, num=1):
        cid = int(cid)
        num = int(num)
        # 查询分类
        categroys_list = Categroy.objects.all().order_by('id')
        # 查询当前的类别下的所有商品信息
        goods_list = Goods.objects.filter(categroy_id=cid).order_by('id')

        # 分页（每页显示1条信息）
        pager = Paginator(goods_list, 1)

        # 获取当前页数据
        page_goods_list = pager.page(num)

        # 每页开始页码
        begin = (num - int(math.ceil(10.0 / 2)))
        if begin < 1:
            begin = 1

        # 每页结束页码
        end = begin + 9
        if end > pager.num_pages:
            end = pager.num_pages

        if end <= 10:
            begin = 1
        else:
            begin = end - 9
        pagelist = range(begin, end + 1)

        return render(request, 'index.html',
                      {'categorys_list': categroys_list, 'goods_list': page_goods_list,
                       'currentcid': cid,'pagelist': pagelist, 'currentnum': num})


class DetailViwe(View):
    @recommend
    def get(self, request, goodsid,recommendList=[]):
        goodsid = int(goodsid)

        # 根据goodsid查询商品的详细信息
        goods = Goods.objects.get(id=goodsid)

        return render(request, 'detail.html', {'goods': goods,'recommendList':recommendList})
