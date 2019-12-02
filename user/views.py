# -*-coding:utf-8 -*-

from django.http import JsonResponse

from user.models import User


# Create your views here.

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

# 删除用户
def delete_user(request, user_id):
    if request.method == "DELETE":
        try:
            sou_rel = User.objects.get(user_id=user_id)
            sou_rel.delete()
            return JsonResponse({"code": 200, "msg": "success"})
        except User.DoesNotExist:
            return JsonResponse({"code": 400, "msg": "数据不存在"})

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
