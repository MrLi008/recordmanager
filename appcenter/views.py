from datetime import datetime
import os
import time

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as django_default_login
from django.contrib.auth.views import login_required
from django.contrib.auth.models import User
from .form import *
from .models import *
from sys_user.func import *

from config_unit.models import all_tables, gl


def index(request):
    if request.method == "GET":
        return HttpResponse(loader.get_template("appcenter/index.html"), locals())
    return HttpResponse(loader.get_template("appcenter/index.html"), locals())


import json


def dump_config(request):
    if request.method == "GET":
        return render(request, "config_algorithm/dump_config.html", locals())
    obj = mydict(request.POST)
    optype = obj.get("optype")

    # 查询所有配置数据并保存为json来下载

    if optype == "all":
        data = {
            name: [m.toJson() for m in gl[name].objects.all()]
            for name in gl
        }
        if not os.path.exists("media/config_algorithm"):
            os.mkdir("media/config_algorithm")
        json.dump(data,
            open("media/config_algorithm/config.json", "w", encoding="utf-8"),
            ensure_ascii=False,
            indent=4,
        )
        jsonfile = "media/config_algorithm/config.json"
        return render(request, "config_algorithm/dump_config.html", locals())


def load_config(request):
    if request.method == "GET":
        return render(request, "config_algorithm/load_config.html", locals())
    obj = mydict(request.POST)
    if "file" in request.FILES:
        config_json = json.loads(request.FILES["file"].read())
        show_msg = list()
        ok_count = 0
        for name, records in config_json.items():
            for record in records:
                ins = gl[name]()
                record = {name: record[name] for name in ins.toParams_en()
                          if name not in ['id', 'createtime', 'updatetime']}
                tmp = ins.fromDict(record)
                if tmp:
                    tmp.save()
                    ok_count += 1
            show_msg.append({
                'tablename': name,
                'count': len(records),
                'ok_count': ok_count
            })
        return render(request, "config_algorithm/load_config.html", locals())
