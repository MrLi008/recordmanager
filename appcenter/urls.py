from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="appcenter_views_index"),
    path("dump_config", views.dump_config, name="config_busi_view_dump_config"),
    path("load_config", views.load_config, name="config_busi_view_load_config"),
]
