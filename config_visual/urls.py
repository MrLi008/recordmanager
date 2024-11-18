from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="config_visual_view_index"),
    path("bi", views.bi, name="config_visual_view_bi"),
    path("bi_level_2", views.bi_level_2, name="config_visual_view_bi_level_2"),
    path("bi_new", views.bi_new, name="config_visual_view_bi_new"),
    path("bi_v1", views.bi, name="config_visual_view_bi_v1"),
    path("bi_v2", views.bi, name="config_visual_view_bi_v2"),
    path("bi_v3", views.bi, name="config_visual_view_bi_v3"),
    path("bi_v4", views.bi, name="config_visual_view_bi_v4"),
    path("bi_v5", views.bi, name="config_visual_view_bi_v5"),
    #
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpsupermanager",
        views.view_supermanager,
        name="bi_tpsupermanager",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tppermkwkwissions",
        views.view_permkwkwissions,
        name="bi_tppermkwkwissions",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tplogs",
        views.view_logs,
        name="bi_tplogs",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpcomments",
        views.view_comments,
        name="bi_tpcomments",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpreckwkwordattachments",
        views.view_reckwkwordattachments,
        name="bi_tpreckwkwordattachments",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpreckwkwords",
        views.view_reckwkwords,
        name="bi_tpreckwkwords",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpreckwkwordcategkwkwories",
        views.view_reckwkwordcategkwkwories,
        name="bi_tpreckwkwordcategkwkwories",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tproles",
        views.view_roles,
        name="bi_tproles",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpusers",
        views.view_users,
        name="bi_tpusers",
    ),
]
