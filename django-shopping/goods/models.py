from django.db import models


# Create your models here.
class Categroy(models.Model):
    cname = models.CharField(max_length=10)

    def __unicode__(self):
        return u'Categroy:%s' % self.cname


class Goods(models.Model):
    gname = models.CharField(max_length=10)
    gdesc = models.CharField(max_length=100)
    oldprice = models.DecimalField(max_digits=8, decimal_places=2)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    categroy = models.ForeignKey(Categroy, on_delete=False)

    def __unicode__(self):
        return u'Goods:%s' % self.gname

    # 获取商品的大图
    def getGImg(self):
        return self.inventory_set.first().color.colorurl

    # 获取商品的颜色对象
    def getColor(self):
        colorList = []
        for inventory in self.inventory_set.all():
            color = inventory.color
            if color not in colorList:
                colorList.append(color)
        return colorList

    # 获取商品的尺码对象
    def getSize(self):
        sizeList = []
        for inventory in self.inventory_set.all():
            size = inventory.size
            if size not in sizeList:
                sizeList.append(size)
        return sizeList

    def getDetail(self):
        import collections
        # 创建一个有序字典存放详情信息(key:详情名称，value：图片列表)
        datas = collections.OrderedDict()
        for goodsdetail in self.goodsdetail_set.all():
            # 详情名称
            gdname = goodsdetail.name()
            if not datas.get(gdname, None):
                datas[gdname] = [goodsdetail.gdurl]
            else:
                datas[gdname].append(goodsdetail.gdurl)
        return datas


class GoodsDetailName(models.Model):
    gdname = models.CharField(max_length=30)

    def __unicode__(self):
        return u'GoodsDetailName:%s' % self.gdname


class GoodsDetail(models.Model):
    gdurl = models.ImageField(upload_to='')
    gdname = models.ForeignKey(GoodsDetailName, on_delete=False)
    goods = models.ForeignKey(Goods, on_delete=False)

    # 获取详情名称
    def name(self):
        return self.gdname.gdname


class Size(models.Model):
    sname = models.CharField(max_length=10)

    def __unicode__(self):
        return u'Size:%s' % self.sname


class Color(models.Model):
    colorname = models.CharField(max_length=10)
    colorurl = models.ImageField(upload_to='color/')

    def __unicode__(self):
        return u'Color:%s' % self.colorname


class Inventory(models.Model):
    count = models.PositiveIntegerField()
    color = models.ForeignKey(Color, on_delete=False)
    goods = models.ForeignKey(Goods, on_delete=False)
    size = models.ForeignKey(Size, on_delete=False)
