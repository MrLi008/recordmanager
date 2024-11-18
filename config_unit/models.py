from django.db import models
from appcenter.models import *
from config_visual.models import *
from sys_user.models import *
from sys_user.func import *

all_tables = dict()
gl = dict()

# Create your models here.

all_tables = {
    "supermanager": mymeta(mc_supermanager),
    "permkwkwissions": mymeta(mc_permkwkwissions),
    "logs": mymeta(mc_logs),
    "comments": mymeta(mc_comments),
    "reckwkwordattachments": mymeta(mc_reckwkwordattachments),
    "reckwkwords": mymeta(mc_reckwkwords),
    "reckwkwordcategkwkwories": mymeta(mc_reckwkwordcategkwkwories),
    "roles": mymeta(mc_roles),
    "users": mymeta(mc_users),
}

# 所有用户表

all_tables_user = {
    "supermanager": mymeta(mc_supermanager),
    "users": mymeta(mc_users),
}
gl = {
    "supermanager": mc_supermanager,
    "permkwkwissions": mc_permkwkwissions,
    "logs": mc_logs,
    "comments": mc_comments,
    "reckwkwordattachments": mc_reckwkwordattachments,
    "reckwkwords": mc_reckwkwords,
    "reckwkwordcategkwkwories": mc_reckwkwordcategkwkwories,
    "roles": mc_roles,
    "users": mc_users,
}
