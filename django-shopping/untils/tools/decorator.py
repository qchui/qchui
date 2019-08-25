from goods.models import Goods


def recommend(func):
    def wrapper(detailView, request, goodsid, *args, **kwargs):
        # 将存放在cookie中的goodsid获取
        cookie_str = request.COOKIES.get('recommend', '')

        # 存放所有goodsid的列表
        goodsIDList = [gid for gid in cookie_str.split() if gid.strip()]

        # 最终需要获取的推荐商品
        goodsObjList = [Goods.objects.get(id=gsid) for gsid in goodsIDList if
                        gsid != goodsid and Goods.objects.get(id=gsid).categroy_id == Goods.objects.get(id=goodsid).categroy_id][:4]

        # 将goodsObjList传递给get方法
        response = func(detailView, request, goodsid, goodsObjList, *args, **kwargs)

        # 判断goodsid是否存在在goodsList中
        if goodsid in goodsIDList:
            goodsIDList.remove(goodsid)
            goodsIDList.insert(0, goodsid)
        else:
            goodsIDList.insert(0, goodsid)

        # 将goodsIDList中的数据保存到cookie中
        response.set_cookie('recommend', ' '.join(goodsIDList), max_age=3 * 24 * 60 * 60)

        return response
    return wrapper
