from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="config_busi_view_index"),
    # 如果用到预测算法,图像识别等单页面展示效果的算法去掉下方注释
    path("auto_detect", views.auto_detect, name="config_busi_view_auto_detect"),
    path("supermanager", views.view_supermanager, name="config_busi_view_supermanager"),
    path(
        "permkwkwissions",
        views.view_permkwkwissions,
        name="config_busi_view_permkwkwissions",
    ),
    path("logs", views.view_logs, name="config_busi_view_logs"),
    path("comments", views.view_comments, name="config_busi_view_comments"),
    path(
        "reckwkwordattachments",
        views.view_reckwkwordattachments,
        name="config_busi_view_reckwkwordattachments",
    ),
    path("reckwkwords", views.view_reckwkwords, name="config_busi_view_reckwkwords"),
    path(
        "reckwkwordcategkwkwories",
        views.view_reckwkwordcategkwkwories,
        name="config_busi_view_reckwkwordcategkwkwories",
    ),
    path("roles", views.view_roles, name="config_busi_view_roles"),
    path("users", views.view_users, name="config_busi_view_users"),
]
