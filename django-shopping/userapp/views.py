from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views import View
from .models import Area
from userapp.models import UserInfo,Address
from django.core.serializers import serialize


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        # 获取信息
        uname = request.POST.get('uname', '')
        pwd = request.POST.get('pwd', '')

        # 插入到数据库
        user = UserInfo.objects.create(uname=uname, pwd=pwd)

        # 判断是否注册成功
        if user:
            # 将用户信息存放在session对象中
            request.session['user'] = user

            return HttpResponseRedirect('/user/center')
        return HttpResponseRedirect('/user/register')


class CheckUanemView(View):
    def get(self, request):
        # 获取相关参数
        uname = request.GET.get('uname', '')

        # 根据用户名去数据库中查询
        userList = UserInfo.objects.filter(uname=uname)

        flag = False

        # 判断是否存在
        if userList:
            flag = True

        return JsonResponse({'flag': flag})


class CenterUanemView(View):
    def get(self, request):
        return render(request, 'center.html')


class Logoutviews(View):
    def post(self, request):
        # 删除登录用户信息
        if 'user' in request.session:
            del request.session['user']

        return JsonResponse({'deflag': True})


class Loginviews(View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        #获取参数
        uname=request.POST.get('uname','')
        pwd=request.POST.get('pwd','')

        #查询数据库中是否存在
        user=UserInfo.objects.filter(uname=uname,pwd=pwd)

        if user:
            request.session['user']=user[0]
            return HttpResponseRedirect('/user/center')
        return HttpResponseRedirect('/user/login')


class Addressviews(View):
    def get(self,request):
        # 获取当前用户的所有收货地址
        user = request.session.get('user', '')

        #展示地址管理部分
        addrlist = user.address_set.all()
        return render(request,'address.html',{'addrlist':addrlist})

    def post(self,request):
        #获取请求参数
        aname=request.POST.get('aname','')
        aphone=request.POST.get('aphone','')
        addr=request.POST.get('addr','')
        user = request.session.get('user', '')


        #将数据插入数据库
        Address.objects.create(aname=aname,aphone=aphone,addr=addr,userinfo=user,
                               isdefault=(lambda count:True if count==0 else False)(user.address_set.all().count()))

        # 展示地址管理部分
        addrlist = user.address_set.all()

        return render(request,'address.html',{'addrlist':addrlist})


class Loadviews(View):
    def get(self,request):
        #获取请求参数
        pid=request.GET.get('pid','')
        pid=int(pid)

        #根据父id查询区划信息
        arealist=Area.objects.filter(parentid=pid)

        #进行序列化
        jarealist=serialize('json',arealist)

        return JsonResponse({'jarealist':jarealist})
