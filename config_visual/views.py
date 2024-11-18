from datetime import datetime
import os
import time

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import login_required
from .form import *
from .models import *
from sys_user.func import *

# 词云

from a_simulink_unit.generate_wordcloud import generate_wordcloud_base64

# Create your views here.


def index(request):

    return render(request, "config_visual/index.html", locals())


"""

# 系统中所有数据表名/中英文+字段中英文
用于快速创建查询语句和分析
测试通过后删除此段.
__deprected__ mark_appcenter_views_all_tables_and_fields
__deprected__ mark_appcenter_views_all_tables_and__two_field_fields
# 根据需要按照表结构和csv文件依次导入数据库.
"""


def bi(request):
    if request.method == "GET":
        return HttpResponse(
            loader.get_template("config_visual/bi.html").render({}, request)
        )
    obj = mydict(request.POST)
    res = dict()

    # supermanager(系统管理员)->username(管理员姓名)

    if obj.get("optype") == "supermanager.username_pie":
        res = get_pie(
            "select username x,count(*) y from vm788_cb37c1767d7b256d.supermanager group by username order by x desc",
            "管理员姓名",
        )
    if obj.get("optype") == "supermanager.username_pie_v1":
        res = get_pie_v1(
            "select username x,count(*) y from vm788_cb37c1767d7b256d.supermanager group by username",
            "管理员姓名",
        )
    if obj.get("optype") == "supermanager.username_pie_v2":
        res = get_pie_v2(
            "select username x,count(*) y from vm788_cb37c1767d7b256d.supermanager group by username",
            "管理员姓名",
        )
    if obj.get("optype") == "supermanager.username_line":
        res = get_line(
            "select username x,count(*) y from vm788_cb37c1767d7b256d.supermanager group by username",
            "管理员姓名",
        )
    if obj.get("optype") == "supermanager.username_bar":
        res = get_bar(
            "select username x,count(*) y from vm788_cb37c1767d7b256d.supermanager group by username",
            "管理员姓名",
        )
    if obj.get("optype") == "supermanager.username_bar_v1":
        res = get_bar_v1(
            "select username x,count(*) y from vm788_cb37c1767d7b256d.supermanager group by username",
            "管理员姓名",
        )
    # permkwkwissions(权限表)->name(权限名称)

    if obj.get("optype") == "permkwkwissions.name_pie":
        res = get_pie(
            "select name x,count(*) y from vm788_cb37c1767d7b256d.permkwkwissions group by name order by x desc",
            "权限名称",
        )
    if obj.get("optype") == "permkwkwissions.name_pie_v1":
        res = get_pie_v1(
            "select name x,count(*) y from vm788_cb37c1767d7b256d.permkwkwissions group by name",
            "权限名称",
        )
    if obj.get("optype") == "permkwkwissions.name_pie_v2":
        res = get_pie_v2(
            "select name x,count(*) y from vm788_cb37c1767d7b256d.permkwkwissions group by name",
            "权限名称",
        )
    if obj.get("optype") == "permkwkwissions.name_line":
        res = get_line(
            "select name x,count(*) y from vm788_cb37c1767d7b256d.permkwkwissions group by name",
            "权限名称",
        )
    if obj.get("optype") == "permkwkwissions.name_bar":
        res = get_bar(
            "select name x,count(*) y from vm788_cb37c1767d7b256d.permkwkwissions group by name",
            "权限名称",
        )
    if obj.get("optype") == "permkwkwissions.name_bar_v1":
        res = get_bar_v1(
            "select name x,count(*) y from vm788_cb37c1767d7b256d.permkwkwissions group by name",
            "权限名称",
        )
    if obj.get("optype") == "permkwkwissions.description_wordcloud":
        textlist = get_data(
            "SELECT description result FROM vm788_cb37c1767d7b256d.permkwkwissions;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "permkwkwissions.createtime_line":
        res = get_line(
            "select createtime x,count(*) y from vm788_cb37c1767d7b256d.permkwkwissions group by createtime order by x",
            "创建时间",
        )
    if obj.get("optype") == "permkwkwissions.updatetime_line":
        res = get_line(
            "select updatetime x,count(*) y from vm788_cb37c1767d7b256d.permkwkwissions group by updatetime order by x",
            "更新时间",
        )
    # permkwkwissions(权限表)->systemmodule(所属系统模块)

    if obj.get("optype") == "permkwkwissions.systemmodule_pie":
        res = get_pie(
            "select systemmodule x,count(*) y from vm788_cb37c1767d7b256d.permkwkwissions group by systemmodule order by x desc",
            "所属系统模块",
        )
    if obj.get("optype") == "permkwkwissions.systemmodule_pie_v1":
        res = get_pie_v1(
            "select systemmodule x,count(*) y from vm788_cb37c1767d7b256d.permkwkwissions group by systemmodule",
            "所属系统模块",
        )
    if obj.get("optype") == "permkwkwissions.systemmodule_pie_v2":
        res = get_pie_v2(
            "select systemmodule x,count(*) y from vm788_cb37c1767d7b256d.permkwkwissions group by systemmodule",
            "所属系统模块",
        )
    if obj.get("optype") == "permkwkwissions.systemmodule_line":
        res = get_line(
            "select systemmodule x,count(*) y from vm788_cb37c1767d7b256d.permkwkwissions group by systemmodule",
            "所属系统模块",
        )
    if obj.get("optype") == "permkwkwissions.systemmodule_bar":
        res = get_bar(
            "select systemmodule x,count(*) y from vm788_cb37c1767d7b256d.permkwkwissions group by systemmodule",
            "所属系统模块",
        )
    if obj.get("optype") == "permkwkwissions.systemmodule_bar_v1":
        res = get_bar_v1(
            "select systemmodule x,count(*) y from vm788_cb37c1767d7b256d.permkwkwissions group by systemmodule",
            "所属系统模块",
        )
    # permkwkwissions(权限表)->actiontype(动作类型如增删改查)

    if obj.get("optype") == "permkwkwissions.actiontype_pie":
        res = get_pie(
            "select actiontype x,count(*) y from vm788_cb37c1767d7b256d.permkwkwissions group by actiontype order by x desc",
            "动作类型如增删改查",
        )
    if obj.get("optype") == "permkwkwissions.actiontype_pie_v1":
        res = get_pie_v1(
            "select actiontype x,count(*) y from vm788_cb37c1767d7b256d.permkwkwissions group by actiontype",
            "动作类型如增删改查",
        )
    if obj.get("optype") == "permkwkwissions.actiontype_pie_v2":
        res = get_pie_v2(
            "select actiontype x,count(*) y from vm788_cb37c1767d7b256d.permkwkwissions group by actiontype",
            "动作类型如增删改查",
        )
    if obj.get("optype") == "permkwkwissions.actiontype_line":
        res = get_line(
            "select actiontype x,count(*) y from vm788_cb37c1767d7b256d.permkwkwissions group by actiontype",
            "动作类型如增删改查",
        )
    if obj.get("optype") == "permkwkwissions.actiontype_bar":
        res = get_bar(
            "select actiontype x,count(*) y from vm788_cb37c1767d7b256d.permkwkwissions group by actiontype",
            "动作类型如增删改查",
        )
    if obj.get("optype") == "permkwkwissions.actiontype_bar_v1":
        res = get_bar_v1(
            "select actiontype x,count(*) y from vm788_cb37c1767d7b256d.permkwkwissions group by actiontype",
            "动作类型如增删改查",
        )
    # permkwkwissions(权限表)->resource(资源标识)

    if obj.get("optype") == "permkwkwissions.resource_pie":
        res = get_pie(
            "select resource x,count(*) y from vm788_cb37c1767d7b256d.permkwkwissions group by resource order by x desc",
            "资源标识",
        )
    if obj.get("optype") == "permkwkwissions.resource_pie_v1":
        res = get_pie_v1(
            "select resource x,count(*) y from vm788_cb37c1767d7b256d.permkwkwissions group by resource",
            "资源标识",
        )
    if obj.get("optype") == "permkwkwissions.resource_pie_v2":
        res = get_pie_v2(
            "select resource x,count(*) y from vm788_cb37c1767d7b256d.permkwkwissions group by resource",
            "资源标识",
        )
    if obj.get("optype") == "permkwkwissions.resource_line":
        res = get_line(
            "select resource x,count(*) y from vm788_cb37c1767d7b256d.permkwkwissions group by resource",
            "资源标识",
        )
    if obj.get("optype") == "permkwkwissions.resource_bar":
        res = get_bar(
            "select resource x,count(*) y from vm788_cb37c1767d7b256d.permkwkwissions group by resource",
            "资源标识",
        )
    if obj.get("optype") == "permkwkwissions.resource_bar_v1":
        res = get_bar_v1(
            "select resource x,count(*) y from vm788_cb37c1767d7b256d.permkwkwissions group by resource",
            "资源标识",
        )
    # permkwkwissions(权限表)->status(权限状态如启用、禁用)

    if obj.get("optype") == "permkwkwissions.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm788_cb37c1767d7b256d.permkwkwissions group by status order by x desc",
            "权限状态如启用、禁用",
        )
    if obj.get("optype") == "permkwkwissions.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm788_cb37c1767d7b256d.permkwkwissions group by status",
            "权限状态如启用、禁用",
        )
    if obj.get("optype") == "permkwkwissions.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm788_cb37c1767d7b256d.permkwkwissions group by status",
            "权限状态如启用、禁用",
        )
    if obj.get("optype") == "permkwkwissions.status_line":
        res = get_line(
            "select status x,count(*) y from vm788_cb37c1767d7b256d.permkwkwissions group by status",
            "权限状态如启用、禁用",
        )
    if obj.get("optype") == "permkwkwissions.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm788_cb37c1767d7b256d.permkwkwissions group by status",
            "权限状态如启用、禁用",
        )
    if obj.get("optype") == "permkwkwissions.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm788_cb37c1767d7b256d.permkwkwissions group by status",
            "权限状态如启用、禁用",
        )
    # logs(日志表)->userid(用户ID关联到用户)

    if obj.get("optype") == "logs.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm788_cb37c1767d7b256d.logs group by userid order by x desc",
            "用户ID关联到用户",
        )
    if obj.get("optype") == "logs.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm788_cb37c1767d7b256d.logs group by userid",
            "用户ID关联到用户",
        )
    if obj.get("optype") == "logs.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm788_cb37c1767d7b256d.logs group by userid",
            "用户ID关联到用户",
        )
    if obj.get("optype") == "logs.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm788_cb37c1767d7b256d.logs group by userid",
            "用户ID关联到用户",
        )
    if obj.get("optype") == "logs.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm788_cb37c1767d7b256d.logs group by userid",
            "用户ID关联到用户",
        )
    if obj.get("optype") == "logs.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm788_cb37c1767d7b256d.logs group by userid",
            "用户ID关联到用户",
        )
    # logs(日志表)->action(操作类型)

    if obj.get("optype") == "logs.action_pie":
        res = get_pie(
            "select action x,count(*) y from vm788_cb37c1767d7b256d.logs group by action order by x desc",
            "操作类型",
        )
    if obj.get("optype") == "logs.action_pie_v1":
        res = get_pie_v1(
            "select action x,count(*) y from vm788_cb37c1767d7b256d.logs group by action",
            "操作类型",
        )
    if obj.get("optype") == "logs.action_pie_v2":
        res = get_pie_v2(
            "select action x,count(*) y from vm788_cb37c1767d7b256d.logs group by action",
            "操作类型",
        )
    if obj.get("optype") == "logs.action_line":
        res = get_line(
            "select action x,count(*) y from vm788_cb37c1767d7b256d.logs group by action",
            "操作类型",
        )
    if obj.get("optype") == "logs.action_bar":
        res = get_bar(
            "select action x,count(*) y from vm788_cb37c1767d7b256d.logs group by action",
            "操作类型",
        )
    if obj.get("optype") == "logs.action_bar_v1":
        res = get_bar_v1(
            "select action x,count(*) y from vm788_cb37c1767d7b256d.logs group by action",
            "操作类型",
        )
    # logs(日志表)->objectid(操作对象ID如记录ID)

    if obj.get("optype") == "logs.objectid_pie":
        res = get_pie(
            "select objectid x,count(*) y from vm788_cb37c1767d7b256d.logs group by objectid order by x desc",
            "操作对象ID如记录ID",
        )
    if obj.get("optype") == "logs.objectid_pie_v1":
        res = get_pie_v1(
            "select objectid x,count(*) y from vm788_cb37c1767d7b256d.logs group by objectid",
            "操作对象ID如记录ID",
        )
    if obj.get("optype") == "logs.objectid_pie_v2":
        res = get_pie_v2(
            "select objectid x,count(*) y from vm788_cb37c1767d7b256d.logs group by objectid",
            "操作对象ID如记录ID",
        )
    if obj.get("optype") == "logs.objectid_line":
        res = get_line(
            "select objectid x,count(*) y from vm788_cb37c1767d7b256d.logs group by objectid",
            "操作对象ID如记录ID",
        )
    if obj.get("optype") == "logs.objectid_bar":
        res = get_bar(
            "select objectid x,count(*) y from vm788_cb37c1767d7b256d.logs group by objectid",
            "操作对象ID如记录ID",
        )
    if obj.get("optype") == "logs.objectid_bar_v1":
        res = get_bar_v1(
            "select objectid x,count(*) y from vm788_cb37c1767d7b256d.logs group by objectid",
            "操作对象ID如记录ID",
        )
    # logs(日志表)->objecttype(操作对象类型)

    if obj.get("optype") == "logs.objecttype_pie":
        res = get_pie(
            "select objecttype x,count(*) y from vm788_cb37c1767d7b256d.logs group by objecttype order by x desc",
            "操作对象类型",
        )
    if obj.get("optype") == "logs.objecttype_pie_v1":
        res = get_pie_v1(
            "select objecttype x,count(*) y from vm788_cb37c1767d7b256d.logs group by objecttype",
            "操作对象类型",
        )
    if obj.get("optype") == "logs.objecttype_pie_v2":
        res = get_pie_v2(
            "select objecttype x,count(*) y from vm788_cb37c1767d7b256d.logs group by objecttype",
            "操作对象类型",
        )
    if obj.get("optype") == "logs.objecttype_line":
        res = get_line(
            "select objecttype x,count(*) y from vm788_cb37c1767d7b256d.logs group by objecttype",
            "操作对象类型",
        )
    if obj.get("optype") == "logs.objecttype_bar":
        res = get_bar(
            "select objecttype x,count(*) y from vm788_cb37c1767d7b256d.logs group by objecttype",
            "操作对象类型",
        )
    if obj.get("optype") == "logs.objecttype_bar_v1":
        res = get_bar_v1(
            "select objecttype x,count(*) y from vm788_cb37c1767d7b256d.logs group by objecttype",
            "操作对象类型",
        )
    if obj.get("optype") == "logs.description_wordcloud":
        textlist = get_data(
            "SELECT description result FROM vm788_cb37c1767d7b256d.logs;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "logs.ipaddressip_wordcloud":
        textlist = get_data(
            "SELECT ipaddressip result FROM vm788_cb37c1767d7b256d.logs;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "logs.createtime_line":
        res = get_line(
            "select createtime x,count(*) y from vm788_cb37c1767d7b256d.logs group by createtime order by x",
            "创建时间",
        )
    # logs(日志表)->status(日志状态如正常、异常)

    if obj.get("optype") == "logs.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm788_cb37c1767d7b256d.logs group by status order by x desc",
            "日志状态如正常、异常",
        )
    if obj.get("optype") == "logs.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm788_cb37c1767d7b256d.logs group by status",
            "日志状态如正常、异常",
        )
    if obj.get("optype") == "logs.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm788_cb37c1767d7b256d.logs group by status",
            "日志状态如正常、异常",
        )
    if obj.get("optype") == "logs.status_line":
        res = get_line(
            "select status x,count(*) y from vm788_cb37c1767d7b256d.logs group by status",
            "日志状态如正常、异常",
        )
    if obj.get("optype") == "logs.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm788_cb37c1767d7b256d.logs group by status",
            "日志状态如正常、异常",
        )
    if obj.get("optype") == "logs.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm788_cb37c1767d7b256d.logs group by status",
            "日志状态如正常、异常",
        )
    # comments(评论表)->reckwkwordid(记录ID关联到记录)

    if obj.get("optype") == "comments.reckwkwordid_pie":
        res = get_pie(
            "select reckwkwordid x,count(*) y from vm788_cb37c1767d7b256d.comments group by reckwkwordid order by x desc",
            "记录ID关联到记录",
        )
    if obj.get("optype") == "comments.reckwkwordid_pie_v1":
        res = get_pie_v1(
            "select reckwkwordid x,count(*) y from vm788_cb37c1767d7b256d.comments group by reckwkwordid",
            "记录ID关联到记录",
        )
    if obj.get("optype") == "comments.reckwkwordid_pie_v2":
        res = get_pie_v2(
            "select reckwkwordid x,count(*) y from vm788_cb37c1767d7b256d.comments group by reckwkwordid",
            "记录ID关联到记录",
        )
    if obj.get("optype") == "comments.reckwkwordid_line":
        res = get_line(
            "select reckwkwordid x,count(*) y from vm788_cb37c1767d7b256d.comments group by reckwkwordid",
            "记录ID关联到记录",
        )
    if obj.get("optype") == "comments.reckwkwordid_bar":
        res = get_bar(
            "select reckwkwordid x,count(*) y from vm788_cb37c1767d7b256d.comments group by reckwkwordid",
            "记录ID关联到记录",
        )
    if obj.get("optype") == "comments.reckwkwordid_bar_v1":
        res = get_bar_v1(
            "select reckwkwordid x,count(*) y from vm788_cb37c1767d7b256d.comments group by reckwkwordid",
            "记录ID关联到记录",
        )
    # comments(评论表)->userid(用户ID关联到用户)

    if obj.get("optype") == "comments.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm788_cb37c1767d7b256d.comments group by userid order by x desc",
            "用户ID关联到用户",
        )
    if obj.get("optype") == "comments.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm788_cb37c1767d7b256d.comments group by userid",
            "用户ID关联到用户",
        )
    if obj.get("optype") == "comments.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm788_cb37c1767d7b256d.comments group by userid",
            "用户ID关联到用户",
        )
    if obj.get("optype") == "comments.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm788_cb37c1767d7b256d.comments group by userid",
            "用户ID关联到用户",
        )
    if obj.get("optype") == "comments.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm788_cb37c1767d7b256d.comments group by userid",
            "用户ID关联到用户",
        )
    if obj.get("optype") == "comments.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm788_cb37c1767d7b256d.comments group by userid",
            "用户ID关联到用户",
        )
    if obj.get("optype") == "comments.content_wordcloud":
        textlist = get_data(
            "SELECT content result FROM vm788_cb37c1767d7b256d.comments;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "comments.createtime_line":
        res = get_line(
            "select createtime x,count(*) y from vm788_cb37c1767d7b256d.comments group by createtime order by x",
            "创建时间",
        )
    if obj.get("optype") == "comments.status_wordcloud":
        textlist = get_data(
            "SELECT status result FROM vm788_cb37c1767d7b256d.comments;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "comments.parentid_wordcloud":
        textlist = get_data(
            "SELECT parentid result FROM vm788_cb37c1767d7b256d.comments;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # comments(评论表)->likes(点赞数)

    if obj.get("optype") == "comments.likes_pie":
        res = get_pie(
            "select likes x,count(*) y from vm788_cb37c1767d7b256d.comments group by likes order by x desc",
            "点赞数",
        )
    if obj.get("optype") == "comments.likes_pie_v1":
        res = get_pie_v1(
            "select likes x,count(*) y from vm788_cb37c1767d7b256d.comments group by likes",
            "点赞数",
        )
    if obj.get("optype") == "comments.likes_pie_v2":
        res = get_pie_v2(
            "select likes x,count(*) y from vm788_cb37c1767d7b256d.comments group by likes",
            "点赞数",
        )
    if obj.get("optype") == "comments.likes_line":
        res = get_line(
            "select likes x,count(*) y from vm788_cb37c1767d7b256d.comments group by likes",
            "点赞数",
        )
    if obj.get("optype") == "comments.likes_bar":
        res = get_bar(
            "select likes x,count(*) y from vm788_cb37c1767d7b256d.comments group by likes",
            "点赞数",
        )
    if obj.get("optype") == "comments.likes_bar_v1":
        res = get_bar_v1(
            "select likes x,count(*) y from vm788_cb37c1767d7b256d.comments group by likes",
            "点赞数",
        )
    # reckwkwordattachments(记录附件表)->reckwkwordid(记录ID关联到记录)

    if obj.get("optype") == "reckwkwordattachments.reckwkwordid_pie":
        res = get_pie(
            "select reckwkwordid x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordattachments group by reckwkwordid order by x desc",
            "记录ID关联到记录",
        )
    if obj.get("optype") == "reckwkwordattachments.reckwkwordid_pie_v1":
        res = get_pie_v1(
            "select reckwkwordid x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordattachments group by reckwkwordid",
            "记录ID关联到记录",
        )
    if obj.get("optype") == "reckwkwordattachments.reckwkwordid_pie_v2":
        res = get_pie_v2(
            "select reckwkwordid x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordattachments group by reckwkwordid",
            "记录ID关联到记录",
        )
    if obj.get("optype") == "reckwkwordattachments.reckwkwordid_line":
        res = get_line(
            "select reckwkwordid x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordattachments group by reckwkwordid",
            "记录ID关联到记录",
        )
    if obj.get("optype") == "reckwkwordattachments.reckwkwordid_bar":
        res = get_bar(
            "select reckwkwordid x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordattachments group by reckwkwordid",
            "记录ID关联到记录",
        )
    if obj.get("optype") == "reckwkwordattachments.reckwkwordid_bar_v1":
        res = get_bar_v1(
            "select reckwkwordid x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordattachments group by reckwkwordid",
            "记录ID关联到记录",
        )
    # reckwkwordattachments(记录附件表)->filename(文件名)

    if obj.get("optype") == "reckwkwordattachments.filename_pie":
        res = get_pie(
            "select filename x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordattachments group by filename order by x desc",
            "文件名",
        )
    if obj.get("optype") == "reckwkwordattachments.filename_pie_v1":
        res = get_pie_v1(
            "select filename x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordattachments group by filename",
            "文件名",
        )
    if obj.get("optype") == "reckwkwordattachments.filename_pie_v2":
        res = get_pie_v2(
            "select filename x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordattachments group by filename",
            "文件名",
        )
    if obj.get("optype") == "reckwkwordattachments.filename_line":
        res = get_line(
            "select filename x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordattachments group by filename",
            "文件名",
        )
    if obj.get("optype") == "reckwkwordattachments.filename_bar":
        res = get_bar(
            "select filename x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordattachments group by filename",
            "文件名",
        )
    if obj.get("optype") == "reckwkwordattachments.filename_bar_v1":
        res = get_bar_v1(
            "select filename x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordattachments group by filename",
            "文件名",
        )
    # reckwkwordattachments(记录附件表)->filepath(文件存储路径)

    if obj.get("optype") == "reckwkwordattachments.filepath_pie":
        res = get_pie(
            "select filepath x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordattachments group by filepath order by x desc",
            "文件存储路径",
        )
    if obj.get("optype") == "reckwkwordattachments.filepath_pie_v1":
        res = get_pie_v1(
            "select filepath x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordattachments group by filepath",
            "文件存储路径",
        )
    if obj.get("optype") == "reckwkwordattachments.filepath_pie_v2":
        res = get_pie_v2(
            "select filepath x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordattachments group by filepath",
            "文件存储路径",
        )
    if obj.get("optype") == "reckwkwordattachments.filepath_line":
        res = get_line(
            "select filepath x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordattachments group by filepath",
            "文件存储路径",
        )
    if obj.get("optype") == "reckwkwordattachments.filepath_bar":
        res = get_bar(
            "select filepath x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordattachments group by filepath",
            "文件存储路径",
        )
    if obj.get("optype") == "reckwkwordattachments.filepath_bar_v1":
        res = get_bar_v1(
            "select filepath x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordattachments group by filepath",
            "文件存储路径",
        )
    # reckwkwordattachments(记录附件表)->filesize(文件大小)

    if obj.get("optype") == "reckwkwordattachments.filesize_pie":
        res = get_pie(
            "select filesize x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordattachments group by filesize order by x desc",
            "文件大小",
        )
    if obj.get("optype") == "reckwkwordattachments.filesize_pie_v1":
        res = get_pie_v1(
            "select filesize x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordattachments group by filesize",
            "文件大小",
        )
    if obj.get("optype") == "reckwkwordattachments.filesize_pie_v2":
        res = get_pie_v2(
            "select filesize x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordattachments group by filesize",
            "文件大小",
        )
    if obj.get("optype") == "reckwkwordattachments.filesize_line":
        res = get_line(
            "select filesize x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordattachments group by filesize",
            "文件大小",
        )
    if obj.get("optype") == "reckwkwordattachments.filesize_bar":
        res = get_bar(
            "select filesize x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordattachments group by filesize",
            "文件大小",
        )
    if obj.get("optype") == "reckwkwordattachments.filesize_bar_v1":
        res = get_bar_v1(
            "select filesize x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordattachments group by filesize",
            "文件大小",
        )
    # reckwkwordattachments(记录附件表)->filetype(文件类型)

    if obj.get("optype") == "reckwkwordattachments.filetype_pie":
        res = get_pie(
            "select filetype x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordattachments group by filetype order by x desc",
            "文件类型",
        )
    if obj.get("optype") == "reckwkwordattachments.filetype_pie_v1":
        res = get_pie_v1(
            "select filetype x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordattachments group by filetype",
            "文件类型",
        )
    if obj.get("optype") == "reckwkwordattachments.filetype_pie_v2":
        res = get_pie_v2(
            "select filetype x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordattachments group by filetype",
            "文件类型",
        )
    if obj.get("optype") == "reckwkwordattachments.filetype_line":
        res = get_line(
            "select filetype x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordattachments group by filetype",
            "文件类型",
        )
    if obj.get("optype") == "reckwkwordattachments.filetype_bar":
        res = get_bar(
            "select filetype x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordattachments group by filetype",
            "文件类型",
        )
    if obj.get("optype") == "reckwkwordattachments.filetype_bar_v1":
        res = get_bar_v1(
            "select filetype x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordattachments group by filetype",
            "文件类型",
        )
    if obj.get("optype") == "reckwkwordattachments.uploadtime_line":
        res = get_line(
            "select uploadtime x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordattachments group by uploadtime order by x",
            "上传时间",
        )
    # reckwkwordattachments(记录附件表)->uploaderid(上传者ID关联到用户)

    if obj.get("optype") == "reckwkwordattachments.uploaderid_pie":
        res = get_pie(
            "select uploaderid x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordattachments group by uploaderid order by x desc",
            "上传者ID关联到用户",
        )
    if obj.get("optype") == "reckwkwordattachments.uploaderid_pie_v1":
        res = get_pie_v1(
            "select uploaderid x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordattachments group by uploaderid",
            "上传者ID关联到用户",
        )
    if obj.get("optype") == "reckwkwordattachments.uploaderid_pie_v2":
        res = get_pie_v2(
            "select uploaderid x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordattachments group by uploaderid",
            "上传者ID关联到用户",
        )
    if obj.get("optype") == "reckwkwordattachments.uploaderid_line":
        res = get_line(
            "select uploaderid x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordattachments group by uploaderid",
            "上传者ID关联到用户",
        )
    if obj.get("optype") == "reckwkwordattachments.uploaderid_bar":
        res = get_bar(
            "select uploaderid x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordattachments group by uploaderid",
            "上传者ID关联到用户",
        )
    if obj.get("optype") == "reckwkwordattachments.uploaderid_bar_v1":
        res = get_bar_v1(
            "select uploaderid x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordattachments group by uploaderid",
            "上传者ID关联到用户",
        )
    if obj.get("optype") == "reckwkwordattachments.description_wordcloud":
        textlist = get_data(
            "SELECT description result FROM vm788_cb37c1767d7b256d.reckwkwordattachments;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # reckwkwords(记录表)->title(记录标题)

    if obj.get("optype") == "reckwkwords.title_pie":
        res = get_pie(
            "select title x,count(*) y from vm788_cb37c1767d7b256d.reckwkwords group by title order by x desc",
            "记录标题",
        )
    if obj.get("optype") == "reckwkwords.title_pie_v1":
        res = get_pie_v1(
            "select title x,count(*) y from vm788_cb37c1767d7b256d.reckwkwords group by title",
            "记录标题",
        )
    if obj.get("optype") == "reckwkwords.title_pie_v2":
        res = get_pie_v2(
            "select title x,count(*) y from vm788_cb37c1767d7b256d.reckwkwords group by title",
            "记录标题",
        )
    if obj.get("optype") == "reckwkwords.title_line":
        res = get_line(
            "select title x,count(*) y from vm788_cb37c1767d7b256d.reckwkwords group by title",
            "记录标题",
        )
    if obj.get("optype") == "reckwkwords.title_bar":
        res = get_bar(
            "select title x,count(*) y from vm788_cb37c1767d7b256d.reckwkwords group by title",
            "记录标题",
        )
    if obj.get("optype") == "reckwkwords.title_bar_v1":
        res = get_bar_v1(
            "select title x,count(*) y from vm788_cb37c1767d7b256d.reckwkwords group by title",
            "记录标题",
        )
    if obj.get("optype") == "reckwkwords.content_wordcloud":
        textlist = get_data(
            "SELECT content result FROM vm788_cb37c1767d7b256d.reckwkwords;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # reckwkwords(记录表)->categkwkworyid(分类ID关联到记录分类)

    if obj.get("optype") == "reckwkwords.categkwkworyid_pie":
        res = get_pie(
            "select categkwkworyid x,count(*) y from vm788_cb37c1767d7b256d.reckwkwords group by categkwkworyid order by x desc",
            "分类ID关联到记录分类",
        )
    if obj.get("optype") == "reckwkwords.categkwkworyid_pie_v1":
        res = get_pie_v1(
            "select categkwkworyid x,count(*) y from vm788_cb37c1767d7b256d.reckwkwords group by categkwkworyid",
            "分类ID关联到记录分类",
        )
    if obj.get("optype") == "reckwkwords.categkwkworyid_pie_v2":
        res = get_pie_v2(
            "select categkwkworyid x,count(*) y from vm788_cb37c1767d7b256d.reckwkwords group by categkwkworyid",
            "分类ID关联到记录分类",
        )
    if obj.get("optype") == "reckwkwords.categkwkworyid_line":
        res = get_line(
            "select categkwkworyid x,count(*) y from vm788_cb37c1767d7b256d.reckwkwords group by categkwkworyid",
            "分类ID关联到记录分类",
        )
    if obj.get("optype") == "reckwkwords.categkwkworyid_bar":
        res = get_bar(
            "select categkwkworyid x,count(*) y from vm788_cb37c1767d7b256d.reckwkwords group by categkwkworyid",
            "分类ID关联到记录分类",
        )
    if obj.get("optype") == "reckwkwords.categkwkworyid_bar_v1":
        res = get_bar_v1(
            "select categkwkworyid x,count(*) y from vm788_cb37c1767d7b256d.reckwkwords group by categkwkworyid",
            "分类ID关联到记录分类",
        )
    # reckwkwords(记录表)->creatkwkworid(创建者ID关联到用户)

    if obj.get("optype") == "reckwkwords.creatkwkworid_pie":
        res = get_pie(
            "select creatkwkworid x,count(*) y from vm788_cb37c1767d7b256d.reckwkwords group by creatkwkworid order by x desc",
            "创建者ID关联到用户",
        )
    if obj.get("optype") == "reckwkwords.creatkwkworid_pie_v1":
        res = get_pie_v1(
            "select creatkwkworid x,count(*) y from vm788_cb37c1767d7b256d.reckwkwords group by creatkwkworid",
            "创建者ID关联到用户",
        )
    if obj.get("optype") == "reckwkwords.creatkwkworid_pie_v2":
        res = get_pie_v2(
            "select creatkwkworid x,count(*) y from vm788_cb37c1767d7b256d.reckwkwords group by creatkwkworid",
            "创建者ID关联到用户",
        )
    if obj.get("optype") == "reckwkwords.creatkwkworid_line":
        res = get_line(
            "select creatkwkworid x,count(*) y from vm788_cb37c1767d7b256d.reckwkwords group by creatkwkworid",
            "创建者ID关联到用户",
        )
    if obj.get("optype") == "reckwkwords.creatkwkworid_bar":
        res = get_bar(
            "select creatkwkworid x,count(*) y from vm788_cb37c1767d7b256d.reckwkwords group by creatkwkworid",
            "创建者ID关联到用户",
        )
    if obj.get("optype") == "reckwkwords.creatkwkworid_bar_v1":
        res = get_bar_v1(
            "select creatkwkworid x,count(*) y from vm788_cb37c1767d7b256d.reckwkwords group by creatkwkworid",
            "创建者ID关联到用户",
        )
    if obj.get("optype") == "reckwkwords.createtime_line":
        res = get_line(
            "select createtime x,count(*) y from vm788_cb37c1767d7b256d.reckwkwords group by createtime order by x",
            "创建时间",
        )
    if obj.get("optype") == "reckwkwords.updatetime_line":
        res = get_line(
            "select updatetime x,count(*) y from vm788_cb37c1767d7b256d.reckwkwords group by updatetime order by x",
            "更新时间",
        )
    # reckwkwords(记录表)->status(记录状态如公开、私有)

    if obj.get("optype") == "reckwkwords.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm788_cb37c1767d7b256d.reckwkwords group by status order by x desc",
            "记录状态如公开、私有",
        )
    if obj.get("optype") == "reckwkwords.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm788_cb37c1767d7b256d.reckwkwords group by status",
            "记录状态如公开、私有",
        )
    if obj.get("optype") == "reckwkwords.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm788_cb37c1767d7b256d.reckwkwords group by status",
            "记录状态如公开、私有",
        )
    if obj.get("optype") == "reckwkwords.status_line":
        res = get_line(
            "select status x,count(*) y from vm788_cb37c1767d7b256d.reckwkwords group by status",
            "记录状态如公开、私有",
        )
    if obj.get("optype") == "reckwkwords.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm788_cb37c1767d7b256d.reckwkwords group by status",
            "记录状态如公开、私有",
        )
    if obj.get("optype") == "reckwkwords.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm788_cb37c1767d7b256d.reckwkwords group by status",
            "记录状态如公开、私有",
        )
    # reckwkwords(记录表)->views(浏览次数)

    if obj.get("optype") == "reckwkwords.views_pie":
        res = get_pie(
            "select views x,count(*) y from vm788_cb37c1767d7b256d.reckwkwords group by views order by x desc",
            "浏览次数",
        )
    if obj.get("optype") == "reckwkwords.views_pie_v1":
        res = get_pie_v1(
            "select views x,count(*) y from vm788_cb37c1767d7b256d.reckwkwords group by views",
            "浏览次数",
        )
    if obj.get("optype") == "reckwkwords.views_pie_v2":
        res = get_pie_v2(
            "select views x,count(*) y from vm788_cb37c1767d7b256d.reckwkwords group by views",
            "浏览次数",
        )
    if obj.get("optype") == "reckwkwords.views_line":
        res = get_line(
            "select views x,count(*) y from vm788_cb37c1767d7b256d.reckwkwords group by views",
            "浏览次数",
        )
    if obj.get("optype") == "reckwkwords.views_bar":
        res = get_bar(
            "select views x,count(*) y from vm788_cb37c1767d7b256d.reckwkwords group by views",
            "浏览次数",
        )
    if obj.get("optype") == "reckwkwords.views_bar_v1":
        res = get_bar_v1(
            "select views x,count(*) y from vm788_cb37c1767d7b256d.reckwkwords group by views",
            "浏览次数",
        )
    # reckwkwordcategkwkwories(记录分类表)->name(分类名称)

    if obj.get("optype") == "reckwkwordcategkwkwories.name_pie":
        res = get_pie(
            "select name x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordcategkwkwories group by name order by x desc",
            "分类名称",
        )
    if obj.get("optype") == "reckwkwordcategkwkwories.name_pie_v1":
        res = get_pie_v1(
            "select name x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordcategkwkwories group by name",
            "分类名称",
        )
    if obj.get("optype") == "reckwkwordcategkwkwories.name_pie_v2":
        res = get_pie_v2(
            "select name x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordcategkwkwories group by name",
            "分类名称",
        )
    if obj.get("optype") == "reckwkwordcategkwkwories.name_line":
        res = get_line(
            "select name x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordcategkwkwories group by name",
            "分类名称",
        )
    if obj.get("optype") == "reckwkwordcategkwkwories.name_bar":
        res = get_bar(
            "select name x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordcategkwkwories group by name",
            "分类名称",
        )
    if obj.get("optype") == "reckwkwordcategkwkwories.name_bar_v1":
        res = get_bar_v1(
            "select name x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordcategkwkwories group by name",
            "分类名称",
        )
    # reckwkwordcategkwkwories(记录分类表)->parentid(关联父分类ID用于构建分类树)

    if obj.get("optype") == "reckwkwordcategkwkwories.parentid_pie":
        res = get_pie(
            "select parentid x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordcategkwkwories group by parentid order by x desc",
            "关联父分类ID用于构建分类树",
        )
    if obj.get("optype") == "reckwkwordcategkwkwories.parentid_pie_v1":
        res = get_pie_v1(
            "select parentid x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordcategkwkwories group by parentid",
            "关联父分类ID用于构建分类树",
        )
    if obj.get("optype") == "reckwkwordcategkwkwories.parentid_pie_v2":
        res = get_pie_v2(
            "select parentid x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordcategkwkwories group by parentid",
            "关联父分类ID用于构建分类树",
        )
    if obj.get("optype") == "reckwkwordcategkwkwories.parentid_line":
        res = get_line(
            "select parentid x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordcategkwkwories group by parentid",
            "关联父分类ID用于构建分类树",
        )
    if obj.get("optype") == "reckwkwordcategkwkwories.parentid_bar":
        res = get_bar(
            "select parentid x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordcategkwkwories group by parentid",
            "关联父分类ID用于构建分类树",
        )
    if obj.get("optype") == "reckwkwordcategkwkwories.parentid_bar_v1":
        res = get_bar_v1(
            "select parentid x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordcategkwkwories group by parentid",
            "关联父分类ID用于构建分类树",
        )
    if obj.get("optype") == "reckwkwordcategkwkwories.description_wordcloud":
        textlist = get_data(
            "SELECT description result FROM vm788_cb37c1767d7b256d.reckwkwordcategkwkwories;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "reckwkwordcategkwkwories.createtime_line":
        res = get_line(
            "select createtime x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordcategkwkwories group by createtime order by x",
            "创建时间",
        )
    if obj.get("optype") == "reckwkwordcategkwkwories.updatetime_line":
        res = get_line(
            "select updatetime x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordcategkwkwories group by updatetime order by x",
            "更新时间",
        )
    # reckwkwordcategkwkwories(记录分类表)->kwkwordernumber(显示顺序)

    if obj.get("optype") == "reckwkwordcategkwkwories.kwkwordernumber_pie":
        res = get_pie(
            "select kwkwordernumber x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordcategkwkwories group by kwkwordernumber order by x desc",
            "显示顺序",
        )
    if obj.get("optype") == "reckwkwordcategkwkwories.kwkwordernumber_pie_v1":
        res = get_pie_v1(
            "select kwkwordernumber x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordcategkwkwories group by kwkwordernumber",
            "显示顺序",
        )
    if obj.get("optype") == "reckwkwordcategkwkwories.kwkwordernumber_pie_v2":
        res = get_pie_v2(
            "select kwkwordernumber x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordcategkwkwories group by kwkwordernumber",
            "显示顺序",
        )
    if obj.get("optype") == "reckwkwordcategkwkwories.kwkwordernumber_line":
        res = get_line(
            "select kwkwordernumber x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordcategkwkwories group by kwkwordernumber",
            "显示顺序",
        )
    if obj.get("optype") == "reckwkwordcategkwkwories.kwkwordernumber_bar":
        res = get_bar(
            "select kwkwordernumber x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordcategkwkwories group by kwkwordernumber",
            "显示顺序",
        )
    if obj.get("optype") == "reckwkwordcategkwkwories.kwkwordernumber_bar_v1":
        res = get_bar_v1(
            "select kwkwordernumber x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordcategkwkwories group by kwkwordernumber",
            "显示顺序",
        )
    # reckwkwordcategkwkwories(记录分类表)->status(分类状态如启用、禁用)

    if obj.get("optype") == "reckwkwordcategkwkwories.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordcategkwkwories group by status order by x desc",
            "分类状态如启用、禁用",
        )
    if obj.get("optype") == "reckwkwordcategkwkwories.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordcategkwkwories group by status",
            "分类状态如启用、禁用",
        )
    if obj.get("optype") == "reckwkwordcategkwkwories.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordcategkwkwories group by status",
            "分类状态如启用、禁用",
        )
    if obj.get("optype") == "reckwkwordcategkwkwories.status_line":
        res = get_line(
            "select status x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordcategkwkwories group by status",
            "分类状态如启用、禁用",
        )
    if obj.get("optype") == "reckwkwordcategkwkwories.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordcategkwkwories group by status",
            "分类状态如启用、禁用",
        )
    if obj.get("optype") == "reckwkwordcategkwkwories.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm788_cb37c1767d7b256d.reckwkwordcategkwkwories group by status",
            "分类状态如启用、禁用",
        )
    # roles(角色表)->rolename(角色名称)

    if obj.get("optype") == "roles.rolename_pie":
        res = get_pie(
            "select rolename x,count(*) y from vm788_cb37c1767d7b256d.roles group by rolename order by x desc",
            "角色名称",
        )
    if obj.get("optype") == "roles.rolename_pie_v1":
        res = get_pie_v1(
            "select rolename x,count(*) y from vm788_cb37c1767d7b256d.roles group by rolename",
            "角色名称",
        )
    if obj.get("optype") == "roles.rolename_pie_v2":
        res = get_pie_v2(
            "select rolename x,count(*) y from vm788_cb37c1767d7b256d.roles group by rolename",
            "角色名称",
        )
    if obj.get("optype") == "roles.rolename_line":
        res = get_line(
            "select rolename x,count(*) y from vm788_cb37c1767d7b256d.roles group by rolename",
            "角色名称",
        )
    if obj.get("optype") == "roles.rolename_bar":
        res = get_bar(
            "select rolename x,count(*) y from vm788_cb37c1767d7b256d.roles group by rolename",
            "角色名称",
        )
    if obj.get("optype") == "roles.rolename_bar_v1":
        res = get_bar_v1(
            "select rolename x,count(*) y from vm788_cb37c1767d7b256d.roles group by rolename",
            "角色名称",
        )
    if obj.get("optype") == "roles.description_wordcloud":
        textlist = get_data(
            "SELECT description result FROM vm788_cb37c1767d7b256d.roles;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "roles.createtime_line":
        res = get_line(
            "select createtime x,count(*) y from vm788_cb37c1767d7b256d.roles group by createtime order by x",
            "创建时间",
        )
    if obj.get("optype") == "roles.updatetime_line":
        res = get_line(
            "select updatetime x,count(*) y from vm788_cb37c1767d7b256d.roles group by updatetime order by x",
            "更新时间",
        )
    # roles(角色表)->permkwkwissions(权限如JSON格式)

    if obj.get("optype") == "roles.permkwkwissions_pie":
        res = get_pie(
            "select permkwkwissions x,count(*) y from vm788_cb37c1767d7b256d.roles group by permkwkwissions order by x desc",
            "权限如JSON格式",
        )
    if obj.get("optype") == "roles.permkwkwissions_pie_v1":
        res = get_pie_v1(
            "select permkwkwissions x,count(*) y from vm788_cb37c1767d7b256d.roles group by permkwkwissions",
            "权限如JSON格式",
        )
    if obj.get("optype") == "roles.permkwkwissions_pie_v2":
        res = get_pie_v2(
            "select permkwkwissions x,count(*) y from vm788_cb37c1767d7b256d.roles group by permkwkwissions",
            "权限如JSON格式",
        )
    if obj.get("optype") == "roles.permkwkwissions_line":
        res = get_line(
            "select permkwkwissions x,count(*) y from vm788_cb37c1767d7b256d.roles group by permkwkwissions",
            "权限如JSON格式",
        )
    if obj.get("optype") == "roles.permkwkwissions_bar":
        res = get_bar(
            "select permkwkwissions x,count(*) y from vm788_cb37c1767d7b256d.roles group by permkwkwissions",
            "权限如JSON格式",
        )
    if obj.get("optype") == "roles.permkwkwissions_bar_v1":
        res = get_bar_v1(
            "select permkwkwissions x,count(*) y from vm788_cb37c1767d7b256d.roles group by permkwkwissions",
            "权限如JSON格式",
        )
    # roles(角色表)->kwkwiskwkwdefault(是否为默认角色)

    if obj.get("optype") == "roles.kwkwiskwkwdefault_pie":
        res = get_pie(
            "select kwkwiskwkwdefault x,count(*) y from vm788_cb37c1767d7b256d.roles group by kwkwiskwkwdefault order by x desc",
            "是否为默认角色",
        )
    if obj.get("optype") == "roles.kwkwiskwkwdefault_pie_v1":
        res = get_pie_v1(
            "select kwkwiskwkwdefault x,count(*) y from vm788_cb37c1767d7b256d.roles group by kwkwiskwkwdefault",
            "是否为默认角色",
        )
    if obj.get("optype") == "roles.kwkwiskwkwdefault_pie_v2":
        res = get_pie_v2(
            "select kwkwiskwkwdefault x,count(*) y from vm788_cb37c1767d7b256d.roles group by kwkwiskwkwdefault",
            "是否为默认角色",
        )
    if obj.get("optype") == "roles.kwkwiskwkwdefault_line":
        res = get_line(
            "select kwkwiskwkwdefault x,count(*) y from vm788_cb37c1767d7b256d.roles group by kwkwiskwkwdefault",
            "是否为默认角色",
        )
    if obj.get("optype") == "roles.kwkwiskwkwdefault_bar":
        res = get_bar(
            "select kwkwiskwkwdefault x,count(*) y from vm788_cb37c1767d7b256d.roles group by kwkwiskwkwdefault",
            "是否为默认角色",
        )
    if obj.get("optype") == "roles.kwkwiskwkwdefault_bar_v1":
        res = get_bar_v1(
            "select kwkwiskwkwdefault x,count(*) y from vm788_cb37c1767d7b256d.roles group by kwkwiskwkwdefault",
            "是否为默认角色",
        )
    # roles(角色表)->status(角色状态如启用、禁用)

    if obj.get("optype") == "roles.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm788_cb37c1767d7b256d.roles group by status order by x desc",
            "角色状态如启用、禁用",
        )
    if obj.get("optype") == "roles.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm788_cb37c1767d7b256d.roles group by status",
            "角色状态如启用、禁用",
        )
    if obj.get("optype") == "roles.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm788_cb37c1767d7b256d.roles group by status",
            "角色状态如启用、禁用",
        )
    if obj.get("optype") == "roles.status_line":
        res = get_line(
            "select status x,count(*) y from vm788_cb37c1767d7b256d.roles group by status",
            "角色状态如启用、禁用",
        )
    if obj.get("optype") == "roles.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm788_cb37c1767d7b256d.roles group by status",
            "角色状态如启用、禁用",
        )
    if obj.get("optype") == "roles.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm788_cb37c1767d7b256d.roles group by status",
            "角色状态如启用、禁用",
        )
    # users(用户表)->username(用户名)

    if obj.get("optype") == "users.username_pie":
        res = get_pie(
            "select username x,count(*) y from vm788_cb37c1767d7b256d.users group by username order by x desc",
            "用户名",
        )
    if obj.get("optype") == "users.username_pie_v1":
        res = get_pie_v1(
            "select username x,count(*) y from vm788_cb37c1767d7b256d.users group by username",
            "用户名",
        )
    if obj.get("optype") == "users.username_pie_v2":
        res = get_pie_v2(
            "select username x,count(*) y from vm788_cb37c1767d7b256d.users group by username",
            "用户名",
        )
    if obj.get("optype") == "users.username_line":
        res = get_line(
            "select username x,count(*) y from vm788_cb37c1767d7b256d.users group by username",
            "用户名",
        )
    if obj.get("optype") == "users.username_bar":
        res = get_bar(
            "select username x,count(*) y from vm788_cb37c1767d7b256d.users group by username",
            "用户名",
        )
    if obj.get("optype") == "users.username_bar_v1":
        res = get_bar_v1(
            "select username x,count(*) y from vm788_cb37c1767d7b256d.users group by username",
            "用户名",
        )
    # users(用户表)->pkwkwasswkwkword(密码加密存储)

    if obj.get("optype") == "users.pkwkwasswkwkword_pie":
        res = get_pie(
            "select pkwkwasswkwkword x,count(*) y from vm788_cb37c1767d7b256d.users group by pkwkwasswkwkword order by x desc",
            "密码加密存储",
        )
    if obj.get("optype") == "users.pkwkwasswkwkword_pie_v1":
        res = get_pie_v1(
            "select pkwkwasswkwkword x,count(*) y from vm788_cb37c1767d7b256d.users group by pkwkwasswkwkword",
            "密码加密存储",
        )
    if obj.get("optype") == "users.pkwkwasswkwkword_pie_v2":
        res = get_pie_v2(
            "select pkwkwasswkwkword x,count(*) y from vm788_cb37c1767d7b256d.users group by pkwkwasswkwkword",
            "密码加密存储",
        )
    if obj.get("optype") == "users.pkwkwasswkwkword_line":
        res = get_line(
            "select pkwkwasswkwkword x,count(*) y from vm788_cb37c1767d7b256d.users group by pkwkwasswkwkword",
            "密码加密存储",
        )
    if obj.get("optype") == "users.pkwkwasswkwkword_bar":
        res = get_bar(
            "select pkwkwasswkwkword x,count(*) y from vm788_cb37c1767d7b256d.users group by pkwkwasswkwkword",
            "密码加密存储",
        )
    if obj.get("optype") == "users.pkwkwasswkwkword_bar_v1":
        res = get_bar_v1(
            "select pkwkwasswkwkword x,count(*) y from vm788_cb37c1767d7b256d.users group by pkwkwasswkwkword",
            "密码加密存储",
        )
    # users(用户表)->email(电子邮件)

    if obj.get("optype") == "users.email_pie":
        res = get_pie(
            "select email x,count(*) y from vm788_cb37c1767d7b256d.users group by email order by x desc",
            "电子邮件",
        )
    if obj.get("optype") == "users.email_pie_v1":
        res = get_pie_v1(
            "select email x,count(*) y from vm788_cb37c1767d7b256d.users group by email",
            "电子邮件",
        )
    if obj.get("optype") == "users.email_pie_v2":
        res = get_pie_v2(
            "select email x,count(*) y from vm788_cb37c1767d7b256d.users group by email",
            "电子邮件",
        )
    if obj.get("optype") == "users.email_line":
        res = get_line(
            "select email x,count(*) y from vm788_cb37c1767d7b256d.users group by email",
            "电子邮件",
        )
    if obj.get("optype") == "users.email_bar":
        res = get_bar(
            "select email x,count(*) y from vm788_cb37c1767d7b256d.users group by email",
            "电子邮件",
        )
    if obj.get("optype") == "users.email_bar_v1":
        res = get_bar_v1(
            "select email x,count(*) y from vm788_cb37c1767d7b256d.users group by email",
            "电子邮件",
        )
    # users(用户表)->phone(电话号码)

    if obj.get("optype") == "users.phone_pie":
        res = get_pie(
            "select phone x,count(*) y from vm788_cb37c1767d7b256d.users group by phone order by x desc",
            "电话号码",
        )
    if obj.get("optype") == "users.phone_pie_v1":
        res = get_pie_v1(
            "select phone x,count(*) y from vm788_cb37c1767d7b256d.users group by phone",
            "电话号码",
        )
    if obj.get("optype") == "users.phone_pie_v2":
        res = get_pie_v2(
            "select phone x,count(*) y from vm788_cb37c1767d7b256d.users group by phone",
            "电话号码",
        )
    if obj.get("optype") == "users.phone_line":
        res = get_line(
            "select phone x,count(*) y from vm788_cb37c1767d7b256d.users group by phone",
            "电话号码",
        )
    if obj.get("optype") == "users.phone_bar":
        res = get_bar(
            "select phone x,count(*) y from vm788_cb37c1767d7b256d.users group by phone",
            "电话号码",
        )
    if obj.get("optype") == "users.phone_bar_v1":
        res = get_bar_v1(
            "select phone x,count(*) y from vm788_cb37c1767d7b256d.users group by phone",
            "电话号码",
        )
    if obj.get("optype") == "users.createtime_line":
        res = get_line(
            "select createtime x,count(*) y from vm788_cb37c1767d7b256d.users group by createtime order by x",
            "创建时间",
        )
    if obj.get("optype") == "users.lkwkwastlogkwkwintime_line":
        res = get_line(
            "select lkwkwastlogkwkwintime x,count(*) y from vm788_cb37c1767d7b256d.users group by lkwkwastlogkwkwintime order by x",
            "最后登录时间",
        )
    # users(用户表)->status(用户状态如活跃、禁用)

    if obj.get("optype") == "users.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm788_cb37c1767d7b256d.users group by status order by x desc",
            "用户状态如活跃、禁用",
        )
    if obj.get("optype") == "users.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm788_cb37c1767d7b256d.users group by status",
            "用户状态如活跃、禁用",
        )
    if obj.get("optype") == "users.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm788_cb37c1767d7b256d.users group by status",
            "用户状态如活跃、禁用",
        )
    if obj.get("optype") == "users.status_line":
        res = get_line(
            "select status x,count(*) y from vm788_cb37c1767d7b256d.users group by status",
            "用户状态如活跃、禁用",
        )
    if obj.get("optype") == "users.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm788_cb37c1767d7b256d.users group by status",
            "用户状态如活跃、禁用",
        )
    if obj.get("optype") == "users.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm788_cb37c1767d7b256d.users group by status",
            "用户状态如活跃、禁用",
        )
    # users(用户表)->roleid(角色ID关联到角色)

    if obj.get("optype") == "users.roleid_pie":
        res = get_pie(
            "select roleid x,count(*) y from vm788_cb37c1767d7b256d.users group by roleid order by x desc",
            "角色ID关联到角色",
        )
    if obj.get("optype") == "users.roleid_pie_v1":
        res = get_pie_v1(
            "select roleid x,count(*) y from vm788_cb37c1767d7b256d.users group by roleid",
            "角色ID关联到角色",
        )
    if obj.get("optype") == "users.roleid_pie_v2":
        res = get_pie_v2(
            "select roleid x,count(*) y from vm788_cb37c1767d7b256d.users group by roleid",
            "角色ID关联到角色",
        )
    if obj.get("optype") == "users.roleid_line":
        res = get_line(
            "select roleid x,count(*) y from vm788_cb37c1767d7b256d.users group by roleid",
            "角色ID关联到角色",
        )
    if obj.get("optype") == "users.roleid_bar":
        res = get_bar(
            "select roleid x,count(*) y from vm788_cb37c1767d7b256d.users group by roleid",
            "角色ID关联到角色",
        )
    if obj.get("optype") == "users.roleid_bar_v1":
        res = get_bar_v1(
            "select roleid x,count(*) y from vm788_cb37c1767d7b256d.users group by roleid",
            "角色ID关联到角色",
        )
    assert "title" in res
    return JsonResponse(res)


# __config_visual_views


def bi_level_2(request):
    if request.method == "GET":
        return HttpResponse(
            loader.get_template("config_visual/bi_level_2.html").render({}, request)
        )
    obj = mydict(request.POST)
    res = dict()

    return JsonResponse(res)


def bi_new(request):
    if request.method == "GET":
        return HttpResponse(loader.get_template("config_visual/bi_new.html").render())
    obj = mydict(request.POST)
    res = dict()

    # __mark_appcenter_views_all__level_new_bi

    return JsonResponse(res)


def view_supermanager(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpsupermanager.html", locals())


def view_permkwkwissions(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tppermkwkwissions.html", locals())


def view_logs(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tplogs.html", locals())


def view_comments(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpcomments.html", locals())


def view_reckwkwordattachments(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tpreckwkwordattachments.html", locals()
        )


def view_reckwkwords(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpreckwkwords.html", locals())


def view_reckwkwordcategkwkwories(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tpreckwkwordcategkwkwories.html", locals()
        )


def view_roles(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tproles.html", locals())


def view_users(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpusers.html", locals())
