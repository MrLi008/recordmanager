from django import forms

from captcha.fields import CaptchaField


class mc_supermanager_form(forms.Form):
    """
    # For Table: 系统管理员
    """

    username = forms.CharField(
        label="管理员姓名",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    class Meta:
        pass


class mc_permkwkwissions_form(forms.Form):
    """
    # For Table: 权限表
    """

    id = forms.UUIDField(
        label="权限ID",
        required=True,
    )

    name = forms.CharField(
        label="权限名称",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    description = forms.Textarea()

    createtime = forms.DateTimeField(
        label="创建时间",
        required=True,
    )

    updatetime = forms.DateTimeField(
        label="更新时间",
        required=True,
    )

    systemmodule = forms.CharField(
        label="所属系统模块",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    actiontype = forms.CharField(
        label="动作类型如增删改查",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    resource = forms.CharField(
        label="资源标识",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    status = forms.CharField(
        label="权限状态如启用、禁用",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    class Meta:
        pass


class mc_logs_form(forms.Form):
    """
    # For Table: 日志表
    """

    id = forms.UUIDField(
        label="日志ID",
        required=True,
    )

    userid = forms.Select()

    action = forms.CharField(
        label="操作类型",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    objectid = forms.UUIDField(
        label="操作对象ID如记录ID",
        required=True,
    )

    objecttype = forms.CharField(
        label="操作对象类型",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    description = forms.Textarea()

    ipaddressip = forms.Textarea()

    createtime = forms.DateTimeField(
        label="创建时间",
        required=True,
    )

    status = forms.CharField(
        label="日志状态如正常、异常",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    class Meta:
        pass


class mc_comments_form(forms.Form):
    """
    # For Table: 评论表
    """

    id = forms.Textarea()

    reckwkwordid = forms.Select()

    userid = forms.Select()

    content = forms.Textarea()

    createtime = forms.DateTimeField(
        label="创建时间",
        required=True,
    )

    status = forms.Textarea()

    parentid = forms.Textarea()

    likes = forms.CharField(
        label="点赞数",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    class Meta:
        pass


class mc_reckwkwordattachments_form(forms.Form):
    """
    # For Table: 记录附件表
    """

    id = forms.UUIDField(
        label="附件ID",
        required=True,
    )

    reckwkwordid = forms.Select()

    filename = forms.FileField(
        label="文件名",
        required=True,
    )

    filepath = forms.FileField(
        label="文件存储路径",
        required=True,
    )

    filesize = forms.FileField(
        label="文件大小",
        required=True,
    )

    filetype = forms.FileField(
        label="文件类型",
        required=True,
    )

    uploadtime = forms.DateTimeField(
        label="上传时间",
        required=True,
    )

    uploaderid = forms.Select()

    description = forms.Textarea()

    class Meta:
        pass


class mc_reckwkwords_form(forms.Form):
    """
    # For Table: 记录表
    """

    id = forms.UUIDField(
        label="记录ID",
        required=True,
    )

    title = forms.CharField(
        label="记录标题",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    content = forms.Textarea()

    categkwkworyid = forms.Select()

    creatkwkworid = forms.Select()

    createtime = forms.DateTimeField(
        label="创建时间",
        required=True,
    )

    updatetime = forms.DateTimeField(
        label="更新时间",
        required=True,
    )

    status = forms.CharField(
        label="记录状态如公开、私有",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    views = forms.CharField(
        label="浏览次数",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    class Meta:
        pass


class mc_reckwkwordcategkwkwories_form(forms.Form):
    """
    # For Table: 记录分类表
    """

    id = forms.UUIDField(
        label="分类ID",
        required=True,
    )

    name = forms.CharField(
        label="分类名称",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    parentid = forms.Select()

    description = forms.Textarea()

    createtime = forms.DateTimeField(
        label="创建时间",
        required=True,
    )

    updatetime = forms.DateTimeField(
        label="更新时间",
        required=True,
    )

    kwkwordernumber = forms.CharField(
        label="显示顺序",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    status = forms.CharField(
        label="分类状态如启用、禁用",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    class Meta:
        pass


class mc_roles_form(forms.Form):
    """
    # For Table: 角色表
    """

    id = forms.UUIDField(
        label="角色ID",
        required=True,
    )

    rolename = forms.CharField(
        label="角色名称",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    description = forms.Textarea()

    createtime = forms.DateTimeField(
        label="创建时间",
        required=True,
    )

    updatetime = forms.DateTimeField(
        label="更新时间",
        required=True,
    )

    permkwkwissions = forms.CharField(
        label="权限如JSON格式",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    kwkwiskwkwdefault = forms.BooleanField(
        label="是否为默认角色",
        required=True,
    )

    status = forms.CharField(
        label="角色状态如启用、禁用",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    class Meta:
        pass


class mc_users_form(forms.Form):
    """
    # For Table: 用户表
    """

    id = forms.UUIDField(
        label="用户ID",
        required=True,
    )

    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    pkwkwasswkwkword = forms.CharField(
        label="密码加密存储",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    email = forms.CharField(
        label="电子邮件",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    phone = forms.CharField(
        label="电话号码",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    createtime = forms.DateTimeField(
        label="创建时间",
        required=True,
    )

    lkwkwastlogkwkwintime = forms.DateTimeField(
        label="最后登录时间",
        required=True,
    )

    status = forms.CharField(
        label="用户状态如活跃、禁用",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    roleid = forms.Select()

    class Meta:
        pass
