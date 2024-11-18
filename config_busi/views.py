from datetime import datetime
import os
import time
import uuid

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import login_required
from .form import *
from .models import *
from appcenter.models import *
from sys_user.func import *


def resp(res, msg, url=None, **kwargs):
    return {"res": res, "msg": msg, "url": url, **kwargs}


# Create your views here.


def index(request):
    records = [
        {
            "id": 1,
        },
        {"id": 2},
    ]
    return render(request, "config_visual/index.html", locals())


@login_required
def view_supermanager(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 系统管理员 用户表(8341)

    if user_table_id == str(8341):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 管理员姓名

        mcauthfield_username = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 系统管理员 系统管理员(8349)

    if user_table_id == str(8349):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 管理员姓名

        mcauthfield_username = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_supermanager.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_supermanager().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_supermanager.objects.filter(**filter)
        else:
            records = mc_supermanager.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/supermanager.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_supermanager()

        # 管理员姓名

        if mcauthfield_username["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.username = obj.get("username")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_supermanager.objects.get(id=obj.get("_id_upd"))

        # 管理员姓名

        if mcauthfield_username["mcauthchange"]:

            # CharField

            ins_table_busi.username = obj.get("username")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_supermanager.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_supermanager.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/supermanager")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_permkwkwissions(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 权限表 用户表(8341)

    if user_table_id == str(8341):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 权限ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 权限名称

        mcauthfield_name = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 所属系统模块

        mcauthfield_systemmodule = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 动作类型如增删改查

        mcauthfield_actiontype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 资源标识

        mcauthfield_resource = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 权限状态如启用、禁用

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 权限表 系统管理员(8349)

    if user_table_id == str(8349):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 权限ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 权限名称

        mcauthfield_name = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 所属系统模块

        mcauthfield_systemmodule = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 动作类型如增删改查

        mcauthfield_actiontype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 资源标识

        mcauthfield_resource = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 权限状态如启用、禁用

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_permkwkwissions.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_permkwkwissions().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_permkwkwissions.objects.filter(**filter)
        else:
            records = mc_permkwkwissions.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/permkwkwissions.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_permkwkwissions()

        # 权限ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 权限名称

        if mcauthfield_name["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.name = obj.get("name")
        # 描述

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createtime = obj.get("createtime")
        # 更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatetime = obj.get("updatetime")
        # 所属系统模块

        if mcauthfield_systemmodule["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.systemmodule = obj.get("systemmodule")
        # 动作类型如增删改查

        if mcauthfield_actiontype["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.actiontype = obj.get("actiontype")
        # 资源标识

        if mcauthfield_resource["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.resource = obj.get("resource")
        # 权限状态如启用、禁用

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_permkwkwissions.objects.get(id=obj.get("_id_upd"))

        # 权限ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 权限名称

        if mcauthfield_name["mcauthchange"]:

            # CharField

            ins_table_busi.name = obj.get("name")
        # 描述

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createtime = obj.get("createtime")
        # 更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatetime = obj.get("updatetime")
        # 所属系统模块

        if mcauthfield_systemmodule["mcauthchange"]:

            # CharField

            ins_table_busi.systemmodule = obj.get("systemmodule")
        # 动作类型如增删改查

        if mcauthfield_actiontype["mcauthchange"]:

            # CharField

            ins_table_busi.actiontype = obj.get("actiontype")
        # 资源标识

        if mcauthfield_resource["mcauthchange"]:

            # CharField

            ins_table_busi.resource = obj.get("resource")
        # 权限状态如启用、禁用

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_permkwkwissions.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_permkwkwissions.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/permkwkwissions")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_logs(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 日志表 用户表(8341)

    if user_table_id == str(8341):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 日志ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 用户ID关联到用户

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 操作类型

        mcauthfield_action = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 操作对象ID如记录ID

        mcauthfield_objectid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 操作对象类型

        mcauthfield_objecttype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 地址

        mcauthfield_ipaddressip = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 日志状态如正常、异常

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 日志表 系统管理员(8349)

    if user_table_id == str(8349):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 日志ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 用户ID关联到用户

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 操作类型

        mcauthfield_action = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 操作对象ID如记录ID

        mcauthfield_objectid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 操作对象类型

        mcauthfield_objecttype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 地址

        mcauthfield_ipaddressip = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 日志状态如正常、异常

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_logs.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_logs().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_logs.objects.filter(**filter)
        else:
            records = mc_logs.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_users_57577 = []
        for m in mc_users.objects.all():
            mobj = m.toJson()
            data_mc_users_57577.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        return render(request, "config_busi/logs.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_logs()

        # 日志ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 用户ID关联到用户

        if mcauthfield_userid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.userid = obj.get("userid")
        # 操作类型

        if mcauthfield_action["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.action = obj.get("action")
        # 操作对象ID如记录ID

        if mcauthfield_objectid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.objectid = str(uuid.uuid4())
        # 操作对象类型

        if mcauthfield_objecttype["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.objecttype = obj.get("objecttype")
        # 描述

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        # 地址

        if mcauthfield_ipaddressip["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.ipaddressip = obj.get("ipaddressip")
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createtime = obj.get("createtime")
        # 日志状态如正常、异常

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_logs.objects.get(id=obj.get("_id_upd"))

        # 日志ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 用户ID关联到用户

        if mcauthfield_userid["mcauthchange"]:

            # SelectField

            ins_table_busi.userid = obj.get("userid")
        # 操作类型

        if mcauthfield_action["mcauthchange"]:

            # CharField

            ins_table_busi.action = obj.get("action")
        # 操作对象ID如记录ID

        if mcauthfield_objectid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.objectid = str(uuid.uuid4())

            ins_table_busi.objectid = str(ins_table_busi.objectid)
        # 操作对象类型

        if mcauthfield_objecttype["mcauthchange"]:

            # CharField

            ins_table_busi.objecttype = obj.get("objecttype")
        # 描述

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        # 地址

        if mcauthfield_ipaddressip["mcauthchange"]:

            # TextField

            ins_table_busi.ipaddressip = obj.get("ipaddressip")
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createtime = obj.get("createtime")
        # 日志状态如正常、异常

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_logs.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_logs.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/logs")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_comments(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 评论表 用户表(8341)

    if user_table_id == str(8341):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 评论ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 记录ID关联到记录

        mcauthfield_reckwkwordid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 用户ID关联到用户

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 评论内容

        mcauthfield_content = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 评论状态如审核通过、待审核、删除

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 父评论ID用于构建评论树

        mcauthfield_parentid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 点赞数

        mcauthfield_likes = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 评论表 系统管理员(8349)

    if user_table_id == str(8349):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 评论ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 记录ID关联到记录

        mcauthfield_reckwkwordid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 用户ID关联到用户

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 评论内容

        mcauthfield_content = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 评论状态如审核通过、待审核、删除

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 父评论ID用于构建评论树

        mcauthfield_parentid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 点赞数

        mcauthfield_likes = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_comments.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_comments().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_comments.objects.filter(**filter)
        else:
            records = mc_comments.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_reckwkwords_57569 = []
        for m in mc_reckwkwords.objects.all():
            mobj = m.toJson()
            data_mc_reckwkwords_57569.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("title"),
                }
            )
        data_mc_users_57570 = []
        for m in mc_users.objects.all():
            mobj = m.toJson()
            data_mc_users_57570.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        return render(request, "config_busi/comments.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_comments()

        # 评论ID

        if mcauthfield_id["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 记录ID关联到记录

        if mcauthfield_reckwkwordid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.reckwkwordid = obj.get("reckwkwordid")
        # 用户ID关联到用户

        if mcauthfield_userid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.userid = obj.get("userid")
        # 评论内容

        if mcauthfield_content["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.content = obj.get("content")
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createtime = obj.get("createtime")
        # 评论状态如审核通过、待审核、删除

        if mcauthfield_status["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        # 父评论ID用于构建评论树

        if mcauthfield_parentid["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.parentid = obj.get("parentid")
        # 点赞数

        if mcauthfield_likes["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.likes = obj.get("likes")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_comments.objects.get(id=obj.get("_id_upd"))

        # 评论ID

        if mcauthfield_id["mcauthchange"]:

            # TextField

            ins_table_busi.id = obj.get("id")
        # 记录ID关联到记录

        if mcauthfield_reckwkwordid["mcauthchange"]:

            # SelectField

            ins_table_busi.reckwkwordid = obj.get("reckwkwordid")
        # 用户ID关联到用户

        if mcauthfield_userid["mcauthchange"]:

            # SelectField

            ins_table_busi.userid = obj.get("userid")
        # 评论内容

        if mcauthfield_content["mcauthchange"]:

            # TextField

            ins_table_busi.content = obj.get("content")
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createtime = obj.get("createtime")
        # 评论状态如审核通过、待审核、删除

        if mcauthfield_status["mcauthchange"]:

            # TextField

            ins_table_busi.status = obj.get("status")
        # 父评论ID用于构建评论树

        if mcauthfield_parentid["mcauthchange"]:

            # TextField

            ins_table_busi.parentid = obj.get("parentid")
        # 点赞数

        if mcauthfield_likes["mcauthchange"]:

            # CharField

            ins_table_busi.likes = obj.get("likes")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_comments.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_comments.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/comments")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_reckwkwordattachments(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 记录附件表 用户表(8341)

    if user_table_id == str(8341):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 附件ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 记录ID关联到记录

        mcauthfield_reckwkwordid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 文件名

        mcauthfield_filename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 文件存储路径

        mcauthfield_filepath = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 文件大小

        mcauthfield_filesize = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 文件类型

        mcauthfield_filetype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 上传时间

        mcauthfield_uploadtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 上传者ID关联到用户

        mcauthfield_uploaderid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 记录附件表 系统管理员(8349)

    if user_table_id == str(8349):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 附件ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 记录ID关联到记录

        mcauthfield_reckwkwordid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 文件名

        mcauthfield_filename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 文件存储路径

        mcauthfield_filepath = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 文件大小

        mcauthfield_filesize = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 文件类型

        mcauthfield_filetype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 上传时间

        mcauthfield_uploadtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 上传者ID关联到用户

        mcauthfield_uploaderid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_reckwkwordattachments.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_reckwkwordattachments().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_reckwkwordattachments.objects.filter(**filter)
        else:
            records = mc_reckwkwordattachments.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_reckwkwords_57560 = []
        for m in mc_reckwkwords.objects.all():
            mobj = m.toJson()
            data_mc_reckwkwords_57560.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("title"),
                }
            )
        data_mc_users_57566 = []
        for m in mc_users.objects.all():
            mobj = m.toJson()
            data_mc_users_57566.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        return render(request, "config_busi/reckwkwordattachments.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_reckwkwordattachments()

        # 附件ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 记录ID关联到记录

        if mcauthfield_reckwkwordid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.reckwkwordid = obj.get("reckwkwordid")
        # 文件名

        if mcauthfield_filename["mcauthchange"]:

            # Save FileFileField 若上传了文件

            if "filename" in request.FILES:
                ins_table_busi.filename = request.FILES["filename"]
        # 文件存储路径

        if mcauthfield_filepath["mcauthchange"]:

            # Save FileFileField 若上传了文件

            if "filepath" in request.FILES:
                ins_table_busi.filepath = request.FILES["filepath"]
        # 文件大小

        if mcauthfield_filesize["mcauthchange"]:

            # Save FileFileField 若上传了文件

            if "filesize" in request.FILES:
                ins_table_busi.filesize = request.FILES["filesize"]
        # 文件类型

        if mcauthfield_filetype["mcauthchange"]:

            # Save FileFileField 若上传了文件

            if "filetype" in request.FILES:
                ins_table_busi.filetype = request.FILES["filetype"]
        # 上传时间

        if mcauthfield_uploadtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.uploadtime = obj.get("uploadtime")
        # 上传者ID关联到用户

        if mcauthfield_uploaderid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.uploaderid = obj.get("uploaderid")
        # 描述

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_reckwkwordattachments.objects.get(id=obj.get("_id_upd"))

        # 附件ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 记录ID关联到记录

        if mcauthfield_reckwkwordid["mcauthchange"]:

            # SelectField

            ins_table_busi.reckwkwordid = obj.get("reckwkwordid")
        # 文件名

        if mcauthfield_filename["mcauthchange"]:

            # Save File FileField

            if "filename" in request.FILES:
                ins_table_busi.filename = request.FILES["filename"]
        # 文件存储路径

        if mcauthfield_filepath["mcauthchange"]:

            # Save File FileField

            if "filepath" in request.FILES:
                ins_table_busi.filepath = request.FILES["filepath"]
        # 文件大小

        if mcauthfield_filesize["mcauthchange"]:

            # Save File FileField

            if "filesize" in request.FILES:
                ins_table_busi.filesize = request.FILES["filesize"]
        # 文件类型

        if mcauthfield_filetype["mcauthchange"]:

            # Save File FileField

            if "filetype" in request.FILES:
                ins_table_busi.filetype = request.FILES["filetype"]
        # 上传时间

        if mcauthfield_uploadtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.uploadtime = obj.get("uploadtime")
        # 上传者ID关联到用户

        if mcauthfield_uploaderid["mcauthchange"]:

            # SelectField

            ins_table_busi.uploaderid = obj.get("uploaderid")
        # 描述

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_reckwkwordattachments.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_reckwkwordattachments.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/reckwkwordattachments")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_reckwkwords(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 记录表 用户表(8341)

    if user_table_id == str(8341):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 记录ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 记录标题

        mcauthfield_title = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 记录内容

        mcauthfield_content = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 分类ID关联到记录分类

        mcauthfield_categkwkworyid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建者ID关联到用户

        mcauthfield_creatkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 记录状态如公开、私有

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 浏览次数

        mcauthfield_views = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 记录表 系统管理员(8349)

    if user_table_id == str(8349):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 记录ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 记录标题

        mcauthfield_title = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 记录内容

        mcauthfield_content = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 分类ID关联到记录分类

        mcauthfield_categkwkworyid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建者ID关联到用户

        mcauthfield_creatkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 记录状态如公开、私有

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 浏览次数

        mcauthfield_views = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_reckwkwords.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_reckwkwords().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_reckwkwords.objects.filter(**filter)
        else:
            records = mc_reckwkwords.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_reckwkwordcategkwkwories_57553 = []
        for m in mc_reckwkwordcategkwkwories.objects.all():
            mobj = m.toJson()
            data_mc_reckwkwordcategkwkwories_57553.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("name"),
                }
            )
        data_mc_users_57554 = []
        for m in mc_users.objects.all():
            mobj = m.toJson()
            data_mc_users_57554.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        return render(request, "config_busi/reckwkwords.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_reckwkwords()

        # 记录ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 记录标题

        if mcauthfield_title["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.title = obj.get("title")
        # 记录内容

        if mcauthfield_content["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.content = obj.get("content")
        # 分类ID关联到记录分类

        if mcauthfield_categkwkworyid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.categkwkworyid = obj.get("categkwkworyid")
        # 创建者ID关联到用户

        if mcauthfield_creatkwkworid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.creatkwkworid = obj.get("creatkwkworid")
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createtime = obj.get("createtime")
        # 更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatetime = obj.get("updatetime")
        # 记录状态如公开、私有

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        # 浏览次数

        if mcauthfield_views["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.views = obj.get("views")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_reckwkwords.objects.get(id=obj.get("_id_upd"))

        # 记录ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 记录标题

        if mcauthfield_title["mcauthchange"]:

            # CharField

            ins_table_busi.title = obj.get("title")
        # 记录内容

        if mcauthfield_content["mcauthchange"]:

            # TextField

            ins_table_busi.content = obj.get("content")
        # 分类ID关联到记录分类

        if mcauthfield_categkwkworyid["mcauthchange"]:

            # SelectField

            ins_table_busi.categkwkworyid = obj.get("categkwkworyid")
        # 创建者ID关联到用户

        if mcauthfield_creatkwkworid["mcauthchange"]:

            # SelectField

            ins_table_busi.creatkwkworid = obj.get("creatkwkworid")
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createtime = obj.get("createtime")
        # 更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatetime = obj.get("updatetime")
        # 记录状态如公开、私有

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        # 浏览次数

        if mcauthfield_views["mcauthchange"]:

            # CharField

            ins_table_busi.views = obj.get("views")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_reckwkwords.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_reckwkwords.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/reckwkwords")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_reckwkwordcategkwkwories(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 记录分类表 用户表(8341)

    if user_table_id == str(8341):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 分类ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 分类名称

        mcauthfield_name = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 关联父分类ID用于构建分类树

        mcauthfield_parentid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 显示顺序

        mcauthfield_kwkwordernumber = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 分类状态如启用、禁用

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 记录分类表 系统管理员(8349)

    if user_table_id == str(8349):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 分类ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 分类名称

        mcauthfield_name = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 关联父分类ID用于构建分类树

        mcauthfield_parentid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 显示顺序

        mcauthfield_kwkwordernumber = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 分类状态如启用、禁用

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_reckwkwordcategkwkwories.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_reckwkwordcategkwkwories().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_reckwkwordcategkwkwories.objects.filter(**filter)
        else:
            records = mc_reckwkwordcategkwkwories.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_reckwkwordcategkwkwories_57544 = []
        for m in mc_reckwkwordcategkwkwories.objects.all():
            mobj = m.toJson()
            data_mc_reckwkwordcategkwkwories_57544.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("name"),
                }
            )
        return render(request, "config_busi/reckwkwordcategkwkwories.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_reckwkwordcategkwkwories()

        # 分类ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 分类名称

        if mcauthfield_name["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.name = obj.get("name")
        # 关联父分类ID用于构建分类树

        if mcauthfield_parentid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.parentid = obj.get("parentid")
        # 描述

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createtime = obj.get("createtime")
        # 更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatetime = obj.get("updatetime")
        # 显示顺序

        if mcauthfield_kwkwordernumber["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.kwkwordernumber = obj.get("kwkwordernumber")
        # 分类状态如启用、禁用

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_reckwkwordcategkwkwories.objects.get(id=obj.get("_id_upd"))

        # 分类ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 分类名称

        if mcauthfield_name["mcauthchange"]:

            # CharField

            ins_table_busi.name = obj.get("name")
        # 关联父分类ID用于构建分类树

        if mcauthfield_parentid["mcauthchange"]:

            # SelectField

            ins_table_busi.parentid = obj.get("parentid")
        # 描述

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createtime = obj.get("createtime")
        # 更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatetime = obj.get("updatetime")
        # 显示顺序

        if mcauthfield_kwkwordernumber["mcauthchange"]:

            # CharField

            ins_table_busi.kwkwordernumber = obj.get("kwkwordernumber")
        # 分类状态如启用、禁用

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_reckwkwordcategkwkwories.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_reckwkwordcategkwkwories.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/reckwkwordcategkwkwories")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_roles(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 角色表 用户表(8341)

    if user_table_id == str(8341):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 角色ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 角色名称

        mcauthfield_rolename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 权限如JSON格式

        mcauthfield_permkwkwissions = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 是否为默认角色

        mcauthfield_kwkwiskwkwdefault = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 角色状态如启用、禁用

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 角色表 系统管理员(8349)

    if user_table_id == str(8349):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 角色ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 角色名称

        mcauthfield_rolename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 权限如JSON格式

        mcauthfield_permkwkwissions = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 是否为默认角色

        mcauthfield_kwkwiskwkwdefault = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 角色状态如启用、禁用

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_roles.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_roles().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_roles.objects.filter(**filter)
        else:
            records = mc_roles.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/roles.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_roles()

        # 角色ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 角色名称

        if mcauthfield_rolename["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.rolename = obj.get("rolename")
        # 描述

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createtime = obj.get("createtime")
        # 更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatetime = obj.get("updatetime")
        # 权限如JSON格式

        if mcauthfield_permkwkwissions["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.permkwkwissions = obj.get("permkwkwissions")
        # 是否为默认角色

        if mcauthfield_kwkwiskwkwdefault["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.kwkwiskwkwdefault = obj.get("kwkwiskwkwdefault")
        # 角色状态如启用、禁用

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_roles.objects.get(id=obj.get("_id_upd"))

        # 角色ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 角色名称

        if mcauthfield_rolename["mcauthchange"]:

            # CharField

            ins_table_busi.rolename = obj.get("rolename")
        # 描述

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createtime = obj.get("createtime")
        # 更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatetime = obj.get("updatetime")
        # 权限如JSON格式

        if mcauthfield_permkwkwissions["mcauthchange"]:

            # CharField

            ins_table_busi.permkwkwissions = obj.get("permkwkwissions")
        # 是否为默认角色

        if mcauthfield_kwkwiskwkwdefault["mcauthchange"]:

            # BooleanField

            ins_table_busi.kwkwiskwkwdefault = obj.get("kwkwiskwkwdefault")
        # 角色状态如启用、禁用

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_roles.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_roles.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/roles")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_users(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 用户表 用户表(8341)

    if user_table_id == str(8341):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 用户ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 用户名

        mcauthfield_username = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 密码加密存储

        mcauthfield_pkwkwasswkwkword = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 电子邮件

        mcauthfield_email = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 电话号码

        mcauthfield_phone = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 最后登录时间

        mcauthfield_lkwkwastlogkwkwintime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 用户状态如活跃、禁用

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 角色ID关联到角色

        mcauthfield_roleid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 用户表 系统管理员(8349)

    if user_table_id == str(8349):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 用户ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 用户名

        mcauthfield_username = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 密码加密存储

        mcauthfield_pkwkwasswkwkword = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 电子邮件

        mcauthfield_email = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 电话号码

        mcauthfield_phone = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 最后登录时间

        mcauthfield_lkwkwastlogkwkwintime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 用户状态如活跃、禁用

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 角色ID关联到角色

        mcauthfield_roleid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_users.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_users().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_users.objects.filter(**filter)
        else:
            records = mc_users.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_roles_57533 = []
        for m in mc_roles.objects.all():
            mobj = m.toJson()
            data_mc_roles_57533.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("rolename"),
                }
            )
        return render(request, "config_busi/users.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_users()

        # 用户ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 用户名

        if mcauthfield_username["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.username = obj.get("username")
        # 密码加密存储

        if mcauthfield_pkwkwasswkwkword["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.pkwkwasswkwkword = obj.get("pkwkwasswkwkword")
        # 电子邮件

        if mcauthfield_email["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.email = obj.get("email")
        # 电话号码

        if mcauthfield_phone["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.phone = obj.get("phone")
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createtime = obj.get("createtime")
        # 最后登录时间

        if mcauthfield_lkwkwastlogkwkwintime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.lkwkwastlogkwkwintime = obj.get("lkwkwastlogkwkwintime")
        # 用户状态如活跃、禁用

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        # 角色ID关联到角色

        if mcauthfield_roleid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.roleid = obj.get("roleid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_users.objects.get(id=obj.get("_id_upd"))

        # 用户ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 用户名

        if mcauthfield_username["mcauthchange"]:

            # CharField

            ins_table_busi.username = obj.get("username")
        # 密码加密存储

        if mcauthfield_pkwkwasswkwkword["mcauthchange"]:

            # CharField

            ins_table_busi.pkwkwasswkwkword = obj.get("pkwkwasswkwkword")
        # 电子邮件

        if mcauthfield_email["mcauthchange"]:

            # CharField

            ins_table_busi.email = obj.get("email")
        # 电话号码

        if mcauthfield_phone["mcauthchange"]:

            # CharField

            ins_table_busi.phone = obj.get("phone")
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createtime = obj.get("createtime")
        # 最后登录时间

        if mcauthfield_lkwkwastlogkwkwintime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.lkwkwastlogkwkwintime = obj.get("lkwkwastlogkwkwintime")
        # 用户状态如活跃、禁用

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        # 角色ID关联到角色

        if mcauthfield_roleid["mcauthchange"]:

            # SelectField

            ins_table_busi.roleid = obj.get("roleid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_users.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_users.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/users")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


def auto_detect(request):
    if request.method == "GET":
        detect = False

        return render(request, "config_algorithm/auto_detect.html", locals())
    obj = mydict(request.POST)

    if "img" not in request.FILES:
        return HttpResponse("请上传图片")
    img = request.FILES["img"]
    # mc_

    detect = True

    detect_result = "算法结果展示"

    # 保存提交的内容
    # 保存分析的结果
    # 若源码中缺少需要的表和字段.联系 qq952934650

    return render(request, "config_algorithm/auto_detect.html", locals())
