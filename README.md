# django-crud-test
# Django——应用app之增删改查

最近由于工作忙以及家庭琐事等原因，好久没写文章了。趁今天空闲之余，分享这篇初级Django的应用app入门文章，欢迎大家批评指正。话不多说，直接开始。
## 1.创建应用user
在项目下执行此命令
```
 (base) gn:fish wind$ python3 manage.py startapp user
```
然后在项目的settings.py文件里INSTALLED_APPS这项添加'user.apps.UserConfig'
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # myself app
    'blog.apps.BlogConfig',
    # add this line
    'user.apps.UserConfig'
]
```
### 2.迁移文件同步到数据库
然后执行这两条命令，同步文件到数据库
```
(base) gn:fish wind$ python3 manage.py makemigrations
(base) gn:fish wind$ python3 manage.py migrate
```
执行这些命令后，就会在项目下生成此user应用。
### 3.应用app结构
![应用结构.png](https://upload-images.jianshu.io/upload_images/13222032-af155e679e996c37.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### a).admin.py
如下图所示，此处注册你编写的数据model，可以单个也可以多个
```
from django.contrib import admin

# Register your models here.

from .models import User

admin.site.register([User])
```
#### b)apps.py
此处可以更改应用的名字
```
from django.apps import AppConfig

class UserConfig(AppConfig):
    name = 'user'
```
#### c)models.py
此处编写model，定义数据字段。如下示例，定义一个User数据，包含id，name，age，phone，address
```
from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.TextField()
    user_age = models.IntegerField()
    user_phone = models.TextField()
    user_address = models.TextField()

    def __str__(self):
        return self.user_name
```
#### d)test.py
测试文件，暂不编写
#### e)urls.py
定义路由名，如下所示。分别是查询用户列表、新增用户、编辑用户、删除用户、查询用户
```
from django.urls import path, include
import user.views

urlpatterns = [
    path('list', user.views.get_user_list),
    path('add', user.views.add_user),
    path('edit/<int:user_id>', user.views.edit_user),
    path('delete/<int:user_id>', user.views.delete_user),
    path('search/<int:user_id>', user.views.search_user),
]
```
#### f)views.py
编写具体的业务方法。
#### (1)导入文件
```
# -*-coding:utf-8 -*-

from django.http import JsonResponse

from user.models import User
```
#### (2）查询用户列表
```
# 获取用户列表
def get_user_list(requset):
    user_list = User.objects.all()
    list_rel = []
    for item in user_list:
        list_rel.append({
            'user_id': item.user_id,
            'user_name': item.user_name,
            'user_age': item.user_age,
            'user_phone': item.user_phone,
            'user_address': item.user_address,
        })
    return JsonResponse({"code": 200, "list": list_rel})
```
postman 调用结果：
![查询用户列表.png](https://upload-images.jianshu.io/upload_images/13222032-b6b6d776fbd23dd0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### (3)添加用户
```
# 添加用户
def add_user(request):
    if request.method == "POST":
        user_name = request.POST.get("user_name")
        user_age = request.POST.get("user_age")
        user_phone = request.POST.get("user_phone")
        user_address = request.POST.get("user_address")
        add_rel = User(user_name=user_name, user_age=user_age, user_phone=user_phone, user_address=user_address)
        add_rel.save()
        return JsonResponse({"code": 200, "msg": "success"})
    else:
        return JsonResponse({"code": 400, "msg": "error"})
```
postman调用结果：
![新增用户.png](https://upload-images.jianshu.io/upload_images/13222032-42aa2bef94286e28.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### (4)编辑用户
```
# 编辑用户
def edit_user(request, user_id):
    if request.method == "POST":
        try:
            user_name = request.POST.get("user_name")
            user_age = request.POST.get("user_age")
            user_phone = request.POST.get("user_phone")
            user_address = request.POST.get("user_address")
            sou_rel = User.objects.get(user_id=user_id)
            sou_rel.user_name = user_name
            sou_rel.user_age = user_age
            sou_rel.user_phone = user_phone
            sou_rel.user_address = user_address
            sou_rel.save()
            return JsonResponse({"code": 200, "msg": "success"})
        except User.DoesNotExist:
            return JsonResponse({"code": 400, "msg": "数据不存在"})
    else:
        return JsonResponse({"code": 400, "msg": "error"})
```
postman调用结果：
![编辑用户.png](https://upload-images.jianshu.io/upload_images/13222032-31b1a20c62c2445c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### (5)删除用户
```
# 删除用户
def delete_user(request, user_id):
    if request.method == "DELETE":
        try:
            sou_rel = User.objects.get(user_id=user_id)
            sou_rel.delete()
            return JsonResponse({"code": 200, "msg": "success"})
        except User.DoesNotExist:
            return JsonResponse({"code": 400, "msg": "数据不存在"})
```
postman调用结果：
![删除用户.png](https://upload-images.jianshu.io/upload_images/13222032-5265d1c2a12d5d7c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### (6）搜索用户
```
# 搜索用户
def search_user(request, user_id):
    if request.method == "GET":
        try:
            sou_rel = User.objects.get(user_id=user_id)
            rel = {}
            rel["user_id"] = sou_rel.user_id
            rel["user_name"] = sou_rel.user_name
            rel["user_phone"] = sou_rel.user_phone
            rel["user_age"] = sou_rel.user_age
            rel["user_address"] = sou_rel.user_address
            return JsonResponse({"code": 200, "data": rel})
        except User.DoesNotExist:
            return JsonResponse({"code": 400, "msg": "数据不存在"})
```
postman调用结果：
![查询用户.png](https://upload-images.jianshu.io/upload_images/13222032-c222d207e53e2499.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 补充说明：
要想接口跑通，还需在主项目urls.py文件下添加应用路由，如下所示：
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # add myself
    path('blog/', include('blog.urls')),

    # add this line
    path('user/', include('user.urls'))
]
```
最后执行如下命令，跑起项目，自己试试吧。如有问题，欢迎大家批评指正，共同交流学习。
```
python3 manage.py runserver
```
