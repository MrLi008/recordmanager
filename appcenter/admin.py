from django.contrib import admin

from django.forms.widgets import Select

# Register your models here.

admin.site.site_header = "beta_基于django的记录管理系统"
admin.site.site_title = "beta_基于django的记录管理系统"
admin.site.index_title = "beta_基于django的记录管理系统"

from .models import *


class mc_supermanager_admin(admin.ModelAdmin):
    list_display = [
        "username",
    ]
    fields = [
        "username",
    ]
    
    search_fields = [
        "username",
    ]


admin.site.register(mc_supermanager, mc_supermanager_admin)


class mc_permkwkwissions_admin(admin.ModelAdmin):
    list_display = [
        "name",
        "systemmodule",
        "actiontype",
        "updatetime",
        "status",
        "resource",
        "id",
        "description",
        "createtime",
    ]
    fields = [
        "name",
        "systemmodule",
        "actiontype",
        "status",
        "resource",
        "description",
    ]


admin.site.register(mc_permkwkwissions, mc_permkwkwissions_admin)


class mc_logs_admin(admin.ModelAdmin):
    list_display = [
        "action",
        "objectid",
        "status",
        "ipaddressip",
        "id",
        "description",
        "userid_showmsg",
        "objecttype",
        "createtime",
    ]
    fields = [
        "action",
        "objectid",
        "status",
        "ipaddressip",
        "description",
        "userid",
        "objecttype",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["userid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.username),
                )
                for item in mc_users.objects.all()
            ]
        )

        return form

    def userid_showmsg(self, obj):
        showmsg_id = obj.userid
        try:
            label = mc_users.objects.get(id=showmsg_id).username
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    userid_showmsg.short_description = "用户ID关联到用户"


admin.site.register(mc_logs, mc_logs_admin)


class mc_comments_admin(admin.ModelAdmin):
    list_display = [
        "parentid",
        "status",
        "reckwkwordid_showmsg",
        "id",
        "userid_showmsg",
        "likes",
        "content",
        "createtime",
    ]
    fields = [
        "parentid",
        "status",
        "userid",
        "likes",
        "content",
        "reckwkwordid",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["reckwkwordid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.title),
                )
                for item in mc_reckwkwords.objects.all()
            ]
        )

        # :TODO
        form.base_fields["userid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.username),
                )
                for item in mc_users.objects.all()
            ]
        )

        return form

    def reckwkwordid_showmsg(self, obj):
        showmsg_id = obj.reckwkwordid
        try:
            label = mc_reckwkwords.objects.get(id=showmsg_id).title
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    reckwkwordid_showmsg.short_description = "记录ID关联到记录"

    def userid_showmsg(self, obj):
        showmsg_id = obj.userid
        try:
            label = mc_users.objects.get(id=showmsg_id).username
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    userid_showmsg.short_description = "用户ID关联到用户"


admin.site.register(mc_comments, mc_comments_admin)


class mc_reckwkwordattachments_admin(admin.ModelAdmin):
    list_display = [
        "uploaderid_showmsg",
        "filesize",
        "filetype",
        "reckwkwordid_showmsg",
        "id",
        "uploadtime",
        "description",
        "filepath",
        "filename",
    ]
    fields = [
        "filetype",
        "filesize",
        "uploaderid",
        "description",
        "filepath",
        "filename",
        "reckwkwordid",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["reckwkwordid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.title),
                )
                for item in mc_reckwkwords.objects.all()
            ]
        )

        # :TODO
        form.base_fields["uploaderid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.username),
                )
                for item in mc_users.objects.all()
            ]
        )

        return form

    def reckwkwordid_showmsg(self, obj):
        showmsg_id = obj.reckwkwordid
        try:
            label = mc_reckwkwords.objects.get(id=showmsg_id).title
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    reckwkwordid_showmsg.short_description = "记录ID关联到记录"

    def uploaderid_showmsg(self, obj):
        showmsg_id = obj.uploaderid
        try:
            label = mc_users.objects.get(id=showmsg_id).username
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    uploaderid_showmsg.short_description = "上传者ID关联到用户"


admin.site.register(mc_reckwkwordattachments, mc_reckwkwordattachments_admin)


class mc_reckwkwords_admin(admin.ModelAdmin):
    list_display = [
        "views",
        "updatetime",
        "status",
        "id",
        "content",
        "title",
        "creatkwkworid_showmsg",
        "categkwkworyid_showmsg",
        "createtime",
    ]
    fields = [
        "views",
        "status",
        "creatkwkworid",
        "content",
        "categkwkworyid",
        "title",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["categkwkworyid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.name),
                )
                for item in mc_reckwkwordcategkwkwories.objects.all()
            ]
        )

        # :TODO
        form.base_fields["creatkwkworid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.username),
                )
                for item in mc_users.objects.all()
            ]
        )

        return form

    def categkwkworyid_showmsg(self, obj):
        showmsg_id = obj.categkwkworyid
        try:
            label = mc_reckwkwordcategkwkwories.objects.get(id=showmsg_id).name
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    categkwkworyid_showmsg.short_description = "分类ID关联到记录分类"

    def creatkwkworid_showmsg(self, obj):
        showmsg_id = obj.creatkwkworid
        try:
            label = mc_users.objects.get(id=showmsg_id).username
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    creatkwkworid_showmsg.short_description = "创建者ID关联到用户"


admin.site.register(mc_reckwkwords, mc_reckwkwords_admin)


class mc_reckwkwordcategkwkwories_admin(admin.ModelAdmin):
    list_display = [
        "name",
        "updatetime",
        "status",
        "id",
        "description",
        "kwkwordernumber",
        "parentid_showmsg",
        "createtime",
    ]
    fields = [
        "name",
        "parentid",
        "status",
        "description",
        "kwkwordernumber",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["parentid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.name),
                )
                for item in mc_reckwkwordcategkwkwories.objects.all()
            ]
        )

        return form

    def parentid_showmsg(self, obj):
        showmsg_id = obj.parentid
        try:
            label = mc_reckwkwordcategkwkwories.objects.get(id=showmsg_id).name
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    parentid_showmsg.short_description = "关联父分类ID用于构建分类树"


admin.site.register(mc_reckwkwordcategkwkwories, mc_reckwkwordcategkwkwories_admin)


class mc_roles_admin(admin.ModelAdmin):
    list_display = [
        "rolename",
        "updatetime",
        "status",
        "kwkwiskwkwdefault",
        "id",
        "description",
        "permkwkwissions",
        "createtime",
    ]
    fields = [
        "rolename",
        "status",
        "kwkwiskwkwdefault",
        "permkwkwissions",
        "description",
    ]


admin.site.register(mc_roles, mc_roles_admin)


class mc_users_admin(admin.ModelAdmin):
    list_display = [
        "status",
        "email",
        "id",
        "username",
        "pkwkwasswkwkword",
        "roleid_showmsg",
        "phone",
        "lkwkwastlogkwkwintime",
        "createtime",
    ]
    fields = [
        "status",
        "email",
        "username",
        "pkwkwasswkwkword",
        "phone",
        "roleid",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["roleid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.rolename),
                )
                for item in mc_roles.objects.all()
            ]
        )

        return form

    def roleid_showmsg(self, obj):
        showmsg_id = obj.roleid
        try:
            label = mc_roles.objects.get(id=showmsg_id).rolename
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    roleid_showmsg.short_description = "角色ID关联到角色"


admin.site.register(mc_users, mc_users_admin)
