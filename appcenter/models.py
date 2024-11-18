from django.db import models


# Create your models here.

import json


class MyModal(models.Model):
    class Meta:
        abstract = True

    def __str__(
        self,
    ):
        s = json.dumps(self.toJson(), ensure_ascii=False, sort_keys=True, indent=4)
        return f"{self.__class__.__name__}:\n{s}\n"

    def toParams(self):
        """
        遍历属性名
        :return:
        """
        return self._meta.fields

    def toImplement(self):
        """用于接口开发"""
        return "<br/>".join(
            [f"{field.name}, {field.verbose_name}" for field in self._meta.fields]
        )

    def toParams_zh(self):
        return [field.verbose_name for field in self._meta.fields]

    def toParams_en(self):
        return [field.name for field in self._meta.fields]

    def toVue(self):
        res = {field.name: getattr(self, field.name, "") for field in self.toParams()}
        if res["id"] == "":
            del res["id"]
        return res

    def toValues(self):
        """
        遍历值
        :return:
        """
        return [getattr(self, field.name) for field in self._meta.fields]

    def toJson(self):
        return {
            field.name: value for field, value in zip(self.toParams(), self.toValues())
        }

    def fromDict(self, obj):
        if obj is None:
            return None
        flag = False
        for k in self.toParams_en():
            if k == "id":
                continue
            if k not in obj:
                continue
            if obj.get(k) in ["", None]:
                continue
            if isinstance(obj.get(k), list):
                pass 
            if isinstance(obj.get(k), dict):
                continue
            flag = True
            setattr(self, k, obj.get(k))
        if flag:
            return self
        return None

    def toMeta(self):
        return {
            "table": {
                "mctablenameen": self._meta.db_table,
                "mctablenamezh": self._meta.verbose_name,
            },
            "field": self.toParams(),
            "field_count": len(self.toParams()),
        }


class mc_supermanager(MyModal):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(
        verbose_name="管理员姓名",
        max_length=690,
        null=True,
        blank=True,
        unique=False,
    )

    class Meta:
        managed = True
        db_table = "supermanager"
        verbose_name = "系统管理员"
        verbose_name_plural = verbose_name


class mc_permkwkwissions(MyModal):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(
        verbose_name="权限名称",
        max_length=965,
        null=True,
        blank=True,
        unique=False,
    )
    description = models.TextField(
        verbose_name="描述",
        null=True,
        blank=True,
        unique=False,
    )
    createtime = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    updatetime = models.DateTimeField(
        verbose_name="更新时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    systemmodule = models.CharField(
        verbose_name="所属系统模块",
        max_length=685,
        null=True,
        blank=True,
        unique=False,
    )
    actiontype = models.CharField(
        verbose_name="动作类型如增删改查",
        max_length=605,
        null=True,
        blank=True,
        unique=False,
    )
    resource = models.CharField(
        verbose_name="资源标识",
        max_length=630,
        null=True,
        blank=True,
        unique=False,
    )
    status = models.CharField(
        verbose_name="权限状态如启用、禁用",
        max_length=980,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.id:
            res["id"] = str(self.id)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.createtime:
            res["createtime"] = str(self.createtime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.updatetime:
            res["updatetime"] = str(self.updatetime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        return res

    class Meta:
        managed = True
        db_table = "permkwkwissions"
        verbose_name = "权限表"
        verbose_name_plural = verbose_name


class mc_logs(MyModal):
    id = models.BigAutoField(primary_key=True)
    userid = models.CharField(
        verbose_name="用户ID关联到用户",
        max_length=580,
        null=True,
        blank=True,
        unique=False,
    )
    action = models.CharField(
        verbose_name="操作类型",
        max_length=980,
        null=True,
        blank=True,
        unique=False,
    )
    objectid = models.CharField(
        max_length=200,
        verbose_name="操作对象ID如记录ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    objecttype = models.CharField(
        verbose_name="操作对象类型",
        max_length=505,
        null=True,
        blank=True,
        unique=False,
    )
    description = models.TextField(
        verbose_name="描述",
        null=True,
        blank=True,
        unique=False,
    )
    ipaddressip = models.TextField(
        verbose_name="地址",
        null=True,
        blank=True,
        unique=False,
    )
    createtime = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    status = models.CharField(
        verbose_name="日志状态如正常、异常",
        max_length=550,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.id:
            res["id"] = str(self.id)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.objectid:
            res["objectid"] = str(self.objectid)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.createtime:
            res["createtime"] = str(self.createtime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        return res

    class Meta:
        managed = True
        db_table = "logs"
        verbose_name = "日志表"
        verbose_name_plural = verbose_name


class mc_comments(MyModal):
    id = models.BigAutoField(primary_key=True)
    reckwkwordid = models.CharField(
        verbose_name="记录ID关联到记录",
        max_length=505,
        null=True,
        blank=True,
        unique=False,
    )
    userid = models.CharField(
        verbose_name="用户ID关联到用户",
        max_length=460,
        null=True,
        blank=True,
        unique=False,
    )
    content = models.TextField(
        verbose_name="评论内容",
        null=True,
        blank=True,
        unique=False,
    )
    createtime = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    status = models.TextField(
        verbose_name="评论状态如审核通过、待审核、删除",
        null=True,
        blank=True,
        unique=False,
    )
    parentid = models.TextField(
        verbose_name="父评论ID用于构建评论树",
        null=True,
        blank=True,
        unique=False,
    )
    likes = models.CharField(
        verbose_name="点赞数",
        max_length=720,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.createtime:
            res["createtime"] = str(self.createtime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        return res

    class Meta:
        managed = True
        db_table = "comments"
        verbose_name = "评论表"
        verbose_name_plural = verbose_name


class mc_reckwkwordattachments(MyModal):
    id = models.BigAutoField(primary_key=True)
    reckwkwordid = models.CharField(
        verbose_name="记录ID关联到记录",
        max_length=975,
        null=True,
        blank=True,
        unique=False,
    )
    filename = models.FileField(
        verbose_name="文件名",
        upload_to="57561",
        null=True,
        blank=True,
        unique=False,
    )
    filepath = models.FileField(
        verbose_name="文件存储路径",
        upload_to="57562",
        null=True,
        blank=True,
        unique=False,
    )
    filesize = models.FileField(
        verbose_name="文件大小",
        upload_to="57563",
        null=True,
        blank=True,
        unique=False,
    )
    filetype = models.FileField(
        verbose_name="文件类型",
        upload_to="57564",
        null=True,
        blank=True,
        unique=False,
    )
    uploadtime = models.DateTimeField(
        verbose_name="上传时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    uploaderid = models.CharField(
        verbose_name="上传者ID关联到用户",
        max_length=510,
        null=True,
        blank=True,
        unique=False,
    )
    description = models.TextField(
        verbose_name="描述",
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.filename:
            res["filename"] = {
                "name": self.filename.name,
                "url": self.filename.url,
            }
        else:
            res["filename"] = None

        if self.filepath:
            res["filepath"] = {
                "name": self.filepath.name,
                "url": self.filepath.url,
            }
        else:
            res["filepath"] = None

        if self.filesize:
            res["filesize"] = {
                "name": self.filesize.name,
                "url": self.filesize.url,
            }
        else:
            res["filesize"] = None

        if self.filetype:
            res["filetype"] = {
                "name": self.filetype.name,
                "url": self.filetype.url,
            }
        else:
            res["filetype"] = None

        if self.id:
            res["id"] = str(self.id)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.uploadtime:
            res["uploadtime"] = str(self.uploadtime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        return res

    class Meta:
        managed = True
        db_table = "reckwkwordattachments"
        verbose_name = "记录附件表"
        verbose_name_plural = verbose_name


class mc_reckwkwords(MyModal):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(
        verbose_name="记录标题",
        max_length=685,
        null=True,
        blank=True,
        unique=False,
    )
    content = models.TextField(
        verbose_name="记录内容",
        null=True,
        blank=True,
        unique=False,
    )
    categkwkworyid = models.CharField(
        verbose_name="分类ID关联到记录分类",
        max_length=755,
        null=True,
        blank=True,
        unique=False,
    )
    creatkwkworid = models.CharField(
        verbose_name="创建者ID关联到用户",
        max_length=550,
        null=True,
        blank=True,
        unique=False,
    )
    createtime = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    updatetime = models.DateTimeField(
        verbose_name="更新时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    status = models.CharField(
        verbose_name="记录状态如公开、私有",
        max_length=685,
        null=True,
        blank=True,
        unique=False,
    )
    views = models.CharField(
        verbose_name="浏览次数",
        max_length=490,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.id:
            res["id"] = str(self.id)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.createtime:
            res["createtime"] = str(self.createtime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.updatetime:
            res["updatetime"] = str(self.updatetime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        return res

    class Meta:
        managed = True
        db_table = "reckwkwords"
        verbose_name = "记录表"
        verbose_name_plural = verbose_name


class mc_reckwkwordcategkwkwories(MyModal):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(
        verbose_name="分类名称",
        max_length=770,
        null=True,
        blank=True,
        unique=False,
    )
    parentid = models.CharField(
        verbose_name="关联父分类ID用于构建分类树",
        max_length=725,
        null=True,
        blank=True,
        unique=False,
    )
    description = models.TextField(
        verbose_name="描述",
        null=True,
        blank=True,
        unique=False,
    )
    createtime = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    updatetime = models.DateTimeField(
        verbose_name="更新时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    kwkwordernumber = models.CharField(
        verbose_name="显示顺序",
        max_length=550,
        null=True,
        blank=True,
        unique=False,
    )
    status = models.CharField(
        verbose_name="分类状态如启用、禁用",
        max_length=535,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.id:
            res["id"] = str(self.id)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.createtime:
            res["createtime"] = str(self.createtime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.updatetime:
            res["updatetime"] = str(self.updatetime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        return res

    class Meta:
        managed = True
        db_table = "reckwkwordcategkwkwories"
        verbose_name = "记录分类表"
        verbose_name_plural = verbose_name


class mc_roles(MyModal):
    id = models.BigAutoField(primary_key=True)
    rolename = models.CharField(
        verbose_name="角色名称",
        max_length=475,
        null=True,
        blank=True,
        unique=False,
    )
    description = models.TextField(
        verbose_name="描述",
        null=True,
        blank=True,
        unique=False,
    )
    createtime = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    updatetime = models.DateTimeField(
        verbose_name="更新时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    permkwkwissions = models.CharField(
        verbose_name="权限如JSON格式",
        max_length=880,
        null=True,
        blank=True,
        unique=False,
    )
    kwkwiskwkwdefault = models.BooleanField(
        verbose_name="是否为默认角色",
        null=True,
        blank=True,
        unique=False,
    )
    status = models.CharField(
        verbose_name="角色状态如启用、禁用",
        max_length=500,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.id:
            res["id"] = str(self.id)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.createtime:
            res["createtime"] = str(self.createtime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.updatetime:
            res["updatetime"] = str(self.updatetime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        return res

    class Meta:
        managed = True
        db_table = "roles"
        verbose_name = "角色表"
        verbose_name_plural = verbose_name


class mc_users(MyModal):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(
        verbose_name="用户名",
        max_length=870,
        null=True,
        blank=True,
        unique=False,
    )
    pkwkwasswkwkword = models.CharField(
        verbose_name="密码加密存储",
        max_length=430,
        null=True,
        blank=True,
        unique=False,
    )
    email = models.CharField(
        verbose_name="电子邮件",
        max_length=490,
        null=True,
        blank=True,
        unique=False,
    )
    phone = models.CharField(
        verbose_name="电话号码",
        max_length=965,
        null=True,
        blank=True,
        unique=False,
    )
    createtime = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    lkwkwastlogkwkwintime = models.DateTimeField(
        verbose_name="最后登录时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    status = models.CharField(
        verbose_name="用户状态如活跃、禁用",
        max_length=615,
        null=True,
        blank=True,
        unique=False,
    )
    roleid = models.CharField(
        verbose_name="角色ID关联到角色",
        max_length=865,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.id:
            res["id"] = str(self.id)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.createtime:
            res["createtime"] = str(self.createtime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.lkwkwastlogkwkwintime:
            res["lkwkwastlogkwkwintime"] = str(self.lkwkwastlogkwkwintime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        return res

    class Meta:
        managed = True
        db_table = "users"
        verbose_name = "用户表"
        verbose_name_plural = verbose_name
