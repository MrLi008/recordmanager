# 用于对标 config_unit 增删改查接口


import requests
from concurrent import futures
from concurrent.futures import ThreadPoolExecutor

url = "http://localhost:9100"


def csrf_token():
    session = requests.Session()
    response = session.get(f"{url}/config_unit/ucsrf")
    response.raise_for_status()
    print(response.json())
    csrf = response.json().get("csrfToken")
    return csrf, session


def register_manager(obj):
    """ """
    csrf, session = csrf_token()
    response = session.post(
        f"{url}/config_unit/register",
        data={
            "csrfmiddlewaretoken": csrf,
            **obj,
        },
    )
    response.raise_for_status()
    print(response.json())


def unit_post(tablename, optype, keys, item: dict):

    csrf, session = csrf_token()
    obj = dict()

    obj["optype"] = optype
    obj["csrfmiddlewaretoken"] = csrf

    for key in keys:
        obj[key] = item.get(key, "")
    print(obj)
    # 设置cookie csrftoken

    session.cookies.update({"csrftoken": csrf})

    response = session.post(f"{url}/config_unit/config_unit/{tablename}", data=obj)
    response.raise_for_status()
    return response.json()


# 并发-有序按顺序返回处理结果，会阻塞


def unit_post_concurrent(tablename, optype, keys, items: list):
    """
    批量提交
    :param tablename:
    :param optype:
    :param keys:
    :param items:
    :return:
    """

    def _unit_post(**kwargs):
        """
        kwargs: dict
            dict: {"tablename": tablename, "optype": optype, "keys": keys, "item": item}

        """
        keys = kwargs.get("keys")
        optype = kwargs.get("optype")

        obj = dict()

        obj["optype"] = optype
        obj["csrfmiddlewaretoken"] = csrf

        for key in keys:
            obj[key] = kwargs.get("item").get(key, "")
        print(obj)
        # 设置cookie csrftoken

        session.cookies.update({"csrftoken": csrf})

        response = session.post(f"{url}/config_unit/config_unit/{tablename}", data=obj)
        response.raise_for_status()
        return response.json()

    csrf, session = csrf_token()
    with ThreadPoolExecutor(max_workers=5) as executor:
        for future in [
            executor.submit(
                _unit_post, tablename=tablename, optype=optype, keys=keys, item=item
            )
            for item in items
        ]:
            try:
                res = future.result()
            except Exception as e:
                res = None
            yield res


# 并发-无序但知道第几个


def unit_post_concurrent(tablename, optype, keys, items: list):
    """
    批量提交
    :param tablename:
    :param optype:
    :param keys:
    :param items:
    :return:
    """

    def _unit_post(kwargs, index):
        """
        kwargs: dict
            dict: {"tablename": tablename, "optype": optype, "keys": keys, "item": item}
        index: int
        """
        keys = kwargs.get("keys")
        optype = kwargs.get("optype")

        obj = dict()

        obj["optype"] = optype
        obj["csrfmiddlewaretoken"] = csrf

        for key in keys:
            obj[key] = kwargs.get("item").get(key, "")
        print(obj)
        # 设置cookie csrftoken

        session.cookies.update({"csrftoken": csrf})

        response = session.post(f"{url}/config_unit/config_unit/{tablename}", data=obj)
        response.raise_for_status()
        return {"resp": response.json(), "seqnumber": index}

    csrf, session = csrf_token()
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures_list = [
            executor.submit(
                _unit_post,
                {"tablename": tablename, "optype": optype, "keys": keys, "item": item},
                index=index,
            )
            for index, item in enumerate(items)
        ]
        for future in futures.as_completed(futures_list):
            try:
                res = future.result()
            except Exception as e:
                res = None
            yield res


def unit_post_supermanager_add(item):
    """
    【系统管理员】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
        "username",  # 管理员姓名【CharField】  非外键
    ]
    return unit_post("supermanager", "add", keys, item)


def unit_post_supermanager_upd(item):
    """
    【系统管理员】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
        "username",  # 管理员姓名【CharField】  非外键
    ]
    return unit_post("supermanager", "upd", keys, item)


def unit_post_supermanager_del(item):
    """
    【系统管理员】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
        "_id",  # 使用记录的ID查询
    ]
    return unit_post("supermanager", "del", keys, item)


def unit_post_supermanager_get(item):
    """
    【系统管理员】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
        "_id",  # 使用记录的ID查询
    ]
    return unit_post("supermanager", "get", keys, item)


def unit_post_supermanager_filter(item):
    """
    【系统管理员】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
        "username",  # 管理员姓名【CharField】  非外键
    ]
    return unit_post("supermanager", "filter", keys, item)


def unit_post_supermanager_view(item):
    """
    【系统管理员】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
        "_id",  # 使用记录的ID查询
    ]
    return unit_post("supermanager", "view", keys, item)


def unit_post_supermanager_go_add(item):
    """
    【系统管理员】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
        {
            "form": {
                "id": "",
            }
        }
    ]
    return unit_post("supermanager", "go_add", keys, item)


def unit_post_supermanager_go_upd(item):
    """
    【系统管理员】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
        {
            "form": {
                "id": "",
            }
        }
    ]
    return unit_post("supermanager", "go_upd", keys, item)


def unit_post_permkwkwissions_add(item):
    """
    【权限表】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
        "id",  # 权限ID【UUIDField】  非外键
        "name",  # 权限名称【CharField】  非外键
        "description",  # 描述【TextField】  非外键
        "createtime",  # 创建时间【DateTimeField】  非外键
        "updatetime",  # 更新时间【DateTimeField】  非外键
        "systemmodule",  # 所属系统模块【CharField】  非外键
        "actiontype",  # 动作类型如增删改查【CharField】  非外键
        "resource",  # 资源标识【CharField】  非外键
        "status",  # 权限状态如启用、禁用【CharField】  非外键
    ]
    return unit_post("permkwkwissions", "add", keys, item)


def unit_post_permkwkwissions_upd(item):
    """
    【权限表】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
        "id",  # 权限ID【UUIDField】  非外键
        "name",  # 权限名称【CharField】  非外键
        "description",  # 描述【TextField】  非外键
        "createtime",  # 创建时间【DateTimeField】  非外键
        "updatetime",  # 更新时间【DateTimeField】  非外键
        "systemmodule",  # 所属系统模块【CharField】  非外键
        "actiontype",  # 动作类型如增删改查【CharField】  非外键
        "resource",  # 资源标识【CharField】  非外键
        "status",  # 权限状态如启用、禁用【CharField】  非外键
    ]
    return unit_post("permkwkwissions", "upd", keys, item)


def unit_post_permkwkwissions_del(item):
    """
    【权限表】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
        "_id",  # 使用记录的ID查询
    ]
    return unit_post("permkwkwissions", "del", keys, item)


def unit_post_permkwkwissions_get(item):
    """
    【权限表】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
        "_id",  # 使用记录的ID查询
    ]
    return unit_post("permkwkwissions", "get", keys, item)


def unit_post_permkwkwissions_filter(item):
    """
    【权限表】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
        "id",  # 权限ID【UUIDField】  非外键
        "name",  # 权限名称【CharField】  非外键
        "description",  # 描述【TextField】  非外键
        "createtime",  # 创建时间【DateTimeField】  非外键
        "updatetime",  # 更新时间【DateTimeField】  非外键
        "systemmodule",  # 所属系统模块【CharField】  非外键
        "actiontype",  # 动作类型如增删改查【CharField】  非外键
        "resource",  # 资源标识【CharField】  非外键
        "status",  # 权限状态如启用、禁用【CharField】  非外键
    ]
    return unit_post("permkwkwissions", "filter", keys, item)


def unit_post_permkwkwissions_view(item):
    """
    【权限表】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
        "_id",  # 使用记录的ID查询
    ]
    return unit_post("permkwkwissions", "view", keys, item)


def unit_post_permkwkwissions_go_add(item):
    """
    【权限表】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
        {
            "form": {
                "id": "",
            }
        }
    ]
    return unit_post("permkwkwissions", "go_add", keys, item)


def unit_post_permkwkwissions_go_upd(item):
    """
    【权限表】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
        {
            "form": {
                "id": "",
            }
        }
    ]
    return unit_post("permkwkwissions", "go_upd", keys, item)


def unit_post_logs_add(item):
    """
    【日志表】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
        "id",  # 日志ID【UUIDField】  非外键
        "userid",  # 用户ID关联到用户【SelectField】   users  username 【用户名】
        "action",  # 操作类型【CharField】  非外键
        "objectid",  # 操作对象ID如记录ID【UUIDField】  非外键
        "objecttype",  # 操作对象类型【CharField】  非外键
        "description",  # 描述【TextField】  非外键
        "ipaddressip",  # 地址【TextField】  非外键
        "createtime",  # 创建时间【DateTimeField】  非外键
        "status",  # 日志状态如正常、异常【CharField】  非外键
    ]
    return unit_post("logs", "add", keys, item)


def unit_post_logs_upd(item):
    """
    【日志表】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
        "id",  # 日志ID【UUIDField】  非外键
        "userid",  # 用户ID关联到用户【SelectField】   users  username 【用户名】
        "action",  # 操作类型【CharField】  非外键
        "objectid",  # 操作对象ID如记录ID【UUIDField】  非外键
        "objecttype",  # 操作对象类型【CharField】  非外键
        "description",  # 描述【TextField】  非外键
        "ipaddressip",  # 地址【TextField】  非外键
        "createtime",  # 创建时间【DateTimeField】  非外键
        "status",  # 日志状态如正常、异常【CharField】  非外键
    ]
    return unit_post("logs", "upd", keys, item)


def unit_post_logs_del(item):
    """
    【日志表】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
        "_id",  # 使用记录的ID查询
    ]
    return unit_post("logs", "del", keys, item)


def unit_post_logs_get(item):
    """
    【日志表】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
        "_id",  # 使用记录的ID查询
    ]
    return unit_post("logs", "get", keys, item)


def unit_post_logs_filter(item):
    """
    【日志表】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
        "id",  # 日志ID【UUIDField】  非外键
        "userid",  # 用户ID关联到用户【SelectField】   users  username 【用户名】
        "action",  # 操作类型【CharField】  非外键
        "objectid",  # 操作对象ID如记录ID【UUIDField】  非外键
        "objecttype",  # 操作对象类型【CharField】  非外键
        "description",  # 描述【TextField】  非外键
        "ipaddressip",  # 地址【TextField】  非外键
        "createtime",  # 创建时间【DateTimeField】  非外键
        "status",  # 日志状态如正常、异常【CharField】  非外键
    ]
    return unit_post("logs", "filter", keys, item)


def unit_post_logs_view(item):
    """
    【日志表】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
        "_id",  # 使用记录的ID查询
    ]
    return unit_post("logs", "view", keys, item)


def unit_post_logs_go_add(item):
    """
    【日志表】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
        {
            "form": {
                "id": "",
            }
        }
    ]
    return unit_post("logs", "go_add", keys, item)


def unit_post_logs_go_upd(item):
    """
    【日志表】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
        {
            "form": {
                "id": "",
            }
        }
    ]
    return unit_post("logs", "go_upd", keys, item)


def unit_post_comments_add(item):
    """
    【评论表】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
        "id",  # 评论ID【TextField】  非外键
        "reckwkwordid",  # 记录ID关联到记录【SelectField】   reckwkwords  title 【记录标题】
        "userid",  # 用户ID关联到用户【SelectField】   users  username 【用户名】
        "content",  # 评论内容【TextField】  非外键
        "createtime",  # 创建时间【DateTimeField】  非外键
        "status",  # 评论状态如审核通过、待审核、删除【TextField】  非外键
        "parentid",  # 父评论ID用于构建评论树【TextField】  非外键
        "likes",  # 点赞数【CharField】  非外键
    ]
    return unit_post("comments", "add", keys, item)


def unit_post_comments_upd(item):
    """
    【评论表】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
        "id",  # 评论ID【TextField】  非外键
        "reckwkwordid",  # 记录ID关联到记录【SelectField】   reckwkwords  title 【记录标题】
        "userid",  # 用户ID关联到用户【SelectField】   users  username 【用户名】
        "content",  # 评论内容【TextField】  非外键
        "createtime",  # 创建时间【DateTimeField】  非外键
        "status",  # 评论状态如审核通过、待审核、删除【TextField】  非外键
        "parentid",  # 父评论ID用于构建评论树【TextField】  非外键
        "likes",  # 点赞数【CharField】  非外键
    ]
    return unit_post("comments", "upd", keys, item)


def unit_post_comments_del(item):
    """
    【评论表】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
        "_id",  # 使用记录的ID查询
    ]
    return unit_post("comments", "del", keys, item)


def unit_post_comments_get(item):
    """
    【评论表】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
        "_id",  # 使用记录的ID查询
    ]
    return unit_post("comments", "get", keys, item)


def unit_post_comments_filter(item):
    """
    【评论表】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
        "id",  # 评论ID【TextField】  非外键
        "reckwkwordid",  # 记录ID关联到记录【SelectField】   reckwkwords  title 【记录标题】
        "userid",  # 用户ID关联到用户【SelectField】   users  username 【用户名】
        "content",  # 评论内容【TextField】  非外键
        "createtime",  # 创建时间【DateTimeField】  非外键
        "status",  # 评论状态如审核通过、待审核、删除【TextField】  非外键
        "parentid",  # 父评论ID用于构建评论树【TextField】  非外键
        "likes",  # 点赞数【CharField】  非外键
    ]
    return unit_post("comments", "filter", keys, item)


def unit_post_comments_view(item):
    """
    【评论表】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
        "_id",  # 使用记录的ID查询
    ]
    return unit_post("comments", "view", keys, item)


def unit_post_comments_go_add(item):
    """
    【评论表】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
        {
            "form": {
                "id": "",
            }
        }
    ]
    return unit_post("comments", "go_add", keys, item)


def unit_post_comments_go_upd(item):
    """
    【评论表】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
        {
            "form": {
                "id": "",
            }
        }
    ]
    return unit_post("comments", "go_upd", keys, item)


def unit_post_reckwkwordattachments_add(item):
    """
    【记录附件表】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
        "id",  # 附件ID【UUIDField】  非外键
        "reckwkwordid",  # 记录ID关联到记录【SelectField】   reckwkwords  title 【记录标题】
        "filename",  # 文件名【FileField】  非外键
        "filepath",  # 文件存储路径【FileField】  非外键
        "filesize",  # 文件大小【FileField】  非外键
        "filetype",  # 文件类型【FileField】  非外键
        "uploadtime",  # 上传时间【DateTimeField】  非外键
        "uploaderid",  # 上传者ID关联到用户【SelectField】   users  username 【用户名】
        "description",  # 描述【TextField】  非外键
    ]
    return unit_post("reckwkwordattachments", "add", keys, item)


def unit_post_reckwkwordattachments_upd(item):
    """
    【记录附件表】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
        "id",  # 附件ID【UUIDField】  非外键
        "reckwkwordid",  # 记录ID关联到记录【SelectField】   reckwkwords  title 【记录标题】
        "filename",  # 文件名【FileField】  非外键
        "filepath",  # 文件存储路径【FileField】  非外键
        "filesize",  # 文件大小【FileField】  非外键
        "filetype",  # 文件类型【FileField】  非外键
        "uploadtime",  # 上传时间【DateTimeField】  非外键
        "uploaderid",  # 上传者ID关联到用户【SelectField】   users  username 【用户名】
        "description",  # 描述【TextField】  非外键
    ]
    return unit_post("reckwkwordattachments", "upd", keys, item)


def unit_post_reckwkwordattachments_del(item):
    """
    【记录附件表】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
        "_id",  # 使用记录的ID查询
    ]
    return unit_post("reckwkwordattachments", "del", keys, item)


def unit_post_reckwkwordattachments_get(item):
    """
    【记录附件表】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
        "_id",  # 使用记录的ID查询
    ]
    return unit_post("reckwkwordattachments", "get", keys, item)


def unit_post_reckwkwordattachments_filter(item):
    """
    【记录附件表】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
        "id",  # 附件ID【UUIDField】  非外键
        "reckwkwordid",  # 记录ID关联到记录【SelectField】   reckwkwords  title 【记录标题】
        "filename",  # 文件名【FileField】  非外键
        "filepath",  # 文件存储路径【FileField】  非外键
        "filesize",  # 文件大小【FileField】  非外键
        "filetype",  # 文件类型【FileField】  非外键
        "uploadtime",  # 上传时间【DateTimeField】  非外键
        "uploaderid",  # 上传者ID关联到用户【SelectField】   users  username 【用户名】
        "description",  # 描述【TextField】  非外键
    ]
    return unit_post("reckwkwordattachments", "filter", keys, item)


def unit_post_reckwkwordattachments_view(item):
    """
    【记录附件表】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
        "_id",  # 使用记录的ID查询
    ]
    return unit_post("reckwkwordattachments", "view", keys, item)


def unit_post_reckwkwordattachments_go_add(item):
    """
    【记录附件表】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
        {
            "form": {
                "id": "",
            }
        }
    ]
    return unit_post("reckwkwordattachments", "go_add", keys, item)


def unit_post_reckwkwordattachments_go_upd(item):
    """
    【记录附件表】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
        {
            "form": {
                "id": "",
            }
        }
    ]
    return unit_post("reckwkwordattachments", "go_upd", keys, item)


def unit_post_reckwkwords_add(item):
    """
    【记录表】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
        "id",  # 记录ID【UUIDField】  非外键
        "title",  # 记录标题【CharField】  非外键
        "content",  # 记录内容【TextField】  非外键
        "categkwkworyid",  # 分类ID关联到记录分类【SelectField】   reckwkwordcategkwkwories  name 【分类名称】
        "creatkwkworid",  # 创建者ID关联到用户【SelectField】   users  username 【用户名】
        "createtime",  # 创建时间【DateTimeField】  非外键
        "updatetime",  # 更新时间【DateTimeField】  非外键
        "status",  # 记录状态如公开、私有【CharField】  非外键
        "views",  # 浏览次数【CharField】  非外键
    ]
    return unit_post("reckwkwords", "add", keys, item)


def unit_post_reckwkwords_upd(item):
    """
    【记录表】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
        "id",  # 记录ID【UUIDField】  非外键
        "title",  # 记录标题【CharField】  非外键
        "content",  # 记录内容【TextField】  非外键
        "categkwkworyid",  # 分类ID关联到记录分类【SelectField】   reckwkwordcategkwkwories  name 【分类名称】
        "creatkwkworid",  # 创建者ID关联到用户【SelectField】   users  username 【用户名】
        "createtime",  # 创建时间【DateTimeField】  非外键
        "updatetime",  # 更新时间【DateTimeField】  非外键
        "status",  # 记录状态如公开、私有【CharField】  非外键
        "views",  # 浏览次数【CharField】  非外键
    ]
    return unit_post("reckwkwords", "upd", keys, item)


def unit_post_reckwkwords_del(item):
    """
    【记录表】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
        "_id",  # 使用记录的ID查询
    ]
    return unit_post("reckwkwords", "del", keys, item)


def unit_post_reckwkwords_get(item):
    """
    【记录表】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
        "_id",  # 使用记录的ID查询
    ]
    return unit_post("reckwkwords", "get", keys, item)


def unit_post_reckwkwords_filter(item):
    """
    【记录表】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
        "id",  # 记录ID【UUIDField】  非外键
        "title",  # 记录标题【CharField】  非外键
        "content",  # 记录内容【TextField】  非外键
        "categkwkworyid",  # 分类ID关联到记录分类【SelectField】   reckwkwordcategkwkwories  name 【分类名称】
        "creatkwkworid",  # 创建者ID关联到用户【SelectField】   users  username 【用户名】
        "createtime",  # 创建时间【DateTimeField】  非外键
        "updatetime",  # 更新时间【DateTimeField】  非外键
        "status",  # 记录状态如公开、私有【CharField】  非外键
        "views",  # 浏览次数【CharField】  非外键
    ]
    return unit_post("reckwkwords", "filter", keys, item)


def unit_post_reckwkwords_view(item):
    """
    【记录表】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
        "_id",  # 使用记录的ID查询
    ]
    return unit_post("reckwkwords", "view", keys, item)


def unit_post_reckwkwords_go_add(item):
    """
    【记录表】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
        {
            "form": {
                "id": "",
            }
        }
    ]
    return unit_post("reckwkwords", "go_add", keys, item)


def unit_post_reckwkwords_go_upd(item):
    """
    【记录表】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
        {
            "form": {
                "id": "",
            }
        }
    ]
    return unit_post("reckwkwords", "go_upd", keys, item)


def unit_post_reckwkwordcategkwkwories_add(item):
    """
    【记录分类表】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
        "id",  # 分类ID【UUIDField】  非外键
        "name",  # 分类名称【CharField】  非外键
        "parentid",  # 关联父分类ID用于构建分类树【SelectField】   reckwkwordcategkwkwories  name 【分类名称】
        "description",  # 描述【TextField】  非外键
        "createtime",  # 创建时间【DateTimeField】  非外键
        "updatetime",  # 更新时间【DateTimeField】  非外键
        "kwkwordernumber",  # 显示顺序【CharField】  非外键
        "status",  # 分类状态如启用、禁用【CharField】  非外键
    ]
    return unit_post("reckwkwordcategkwkwories", "add", keys, item)


def unit_post_reckwkwordcategkwkwories_upd(item):
    """
    【记录分类表】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
        "id",  # 分类ID【UUIDField】  非外键
        "name",  # 分类名称【CharField】  非外键
        "parentid",  # 关联父分类ID用于构建分类树【SelectField】   reckwkwordcategkwkwories  name 【分类名称】
        "description",  # 描述【TextField】  非外键
        "createtime",  # 创建时间【DateTimeField】  非外键
        "updatetime",  # 更新时间【DateTimeField】  非外键
        "kwkwordernumber",  # 显示顺序【CharField】  非外键
        "status",  # 分类状态如启用、禁用【CharField】  非外键
    ]
    return unit_post("reckwkwordcategkwkwories", "upd", keys, item)


def unit_post_reckwkwordcategkwkwories_del(item):
    """
    【记录分类表】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
        "_id",  # 使用记录的ID查询
    ]
    return unit_post("reckwkwordcategkwkwories", "del", keys, item)


def unit_post_reckwkwordcategkwkwories_get(item):
    """
    【记录分类表】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
        "_id",  # 使用记录的ID查询
    ]
    return unit_post("reckwkwordcategkwkwories", "get", keys, item)


def unit_post_reckwkwordcategkwkwories_filter(item):
    """
    【记录分类表】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
        "id",  # 分类ID【UUIDField】  非外键
        "name",  # 分类名称【CharField】  非外键
        "parentid",  # 关联父分类ID用于构建分类树【SelectField】   reckwkwordcategkwkwories  name 【分类名称】
        "description",  # 描述【TextField】  非外键
        "createtime",  # 创建时间【DateTimeField】  非外键
        "updatetime",  # 更新时间【DateTimeField】  非外键
        "kwkwordernumber",  # 显示顺序【CharField】  非外键
        "status",  # 分类状态如启用、禁用【CharField】  非外键
    ]
    return unit_post("reckwkwordcategkwkwories", "filter", keys, item)


def unit_post_reckwkwordcategkwkwories_view(item):
    """
    【记录分类表】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
        "_id",  # 使用记录的ID查询
    ]
    return unit_post("reckwkwordcategkwkwories", "view", keys, item)


def unit_post_reckwkwordcategkwkwories_go_add(item):
    """
    【记录分类表】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
        {
            "form": {
                "id": "",
            }
        }
    ]
    return unit_post("reckwkwordcategkwkwories", "go_add", keys, item)


def unit_post_reckwkwordcategkwkwories_go_upd(item):
    """
    【记录分类表】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
        {
            "form": {
                "id": "",
            }
        }
    ]
    return unit_post("reckwkwordcategkwkwories", "go_upd", keys, item)


def unit_post_roles_add(item):
    """
    【角色表】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
        "id",  # 角色ID【UUIDField】  非外键
        "rolename",  # 角色名称【CharField】  非外键
        "description",  # 描述【TextField】  非外键
        "createtime",  # 创建时间【DateTimeField】  非外键
        "updatetime",  # 更新时间【DateTimeField】  非外键
        "permkwkwissions",  # 权限如JSON格式【CharField】  非外键
        "kwkwiskwkwdefault",  # 是否为默认角色【BooleanField】  非外键
        "status",  # 角色状态如启用、禁用【CharField】  非外键
    ]
    return unit_post("roles", "add", keys, item)


def unit_post_roles_upd(item):
    """
    【角色表】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
        "id",  # 角色ID【UUIDField】  非外键
        "rolename",  # 角色名称【CharField】  非外键
        "description",  # 描述【TextField】  非外键
        "createtime",  # 创建时间【DateTimeField】  非外键
        "updatetime",  # 更新时间【DateTimeField】  非外键
        "permkwkwissions",  # 权限如JSON格式【CharField】  非外键
        "kwkwiskwkwdefault",  # 是否为默认角色【BooleanField】  非外键
        "status",  # 角色状态如启用、禁用【CharField】  非外键
    ]
    return unit_post("roles", "upd", keys, item)


def unit_post_roles_del(item):
    """
    【角色表】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
        "_id",  # 使用记录的ID查询
    ]
    return unit_post("roles", "del", keys, item)


def unit_post_roles_get(item):
    """
    【角色表】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
        "_id",  # 使用记录的ID查询
    ]
    return unit_post("roles", "get", keys, item)


def unit_post_roles_filter(item):
    """
    【角色表】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
        "id",  # 角色ID【UUIDField】  非外键
        "rolename",  # 角色名称【CharField】  非外键
        "description",  # 描述【TextField】  非外键
        "createtime",  # 创建时间【DateTimeField】  非外键
        "updatetime",  # 更新时间【DateTimeField】  非外键
        "permkwkwissions",  # 权限如JSON格式【CharField】  非外键
        "kwkwiskwkwdefault",  # 是否为默认角色【BooleanField】  非外键
        "status",  # 角色状态如启用、禁用【CharField】  非外键
    ]
    return unit_post("roles", "filter", keys, item)


def unit_post_roles_view(item):
    """
    【角色表】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
        "_id",  # 使用记录的ID查询
    ]
    return unit_post("roles", "view", keys, item)


def unit_post_roles_go_add(item):
    """
    【角色表】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
        {
            "form": {
                "id": "",
            }
        }
    ]
    return unit_post("roles", "go_add", keys, item)


def unit_post_roles_go_upd(item):
    """
    【角色表】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
        {
            "form": {
                "id": "",
            }
        }
    ]
    return unit_post("roles", "go_upd", keys, item)


def unit_post_users_add(item):
    """
    【用户表】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
        "id",  # 用户ID【UUIDField】  非外键
        "username",  # 用户名【CharField】  非外键
        "pkwkwasswkwkword",  # 密码加密存储【CharField】  非外键
        "email",  # 电子邮件【CharField】  非外键
        "phone",  # 电话号码【CharField】  非外键
        "createtime",  # 创建时间【DateTimeField】  非外键
        "lkwkwastlogkwkwintime",  # 最后登录时间【DateTimeField】  非外键
        "status",  # 用户状态如活跃、禁用【CharField】  非外键
        "roleid",  # 角色ID关联到角色【SelectField】   roles  rolename 【角色名称】
    ]
    return unit_post("users", "add", keys, item)


def unit_post_users_upd(item):
    """
    【用户表】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
        "id",  # 用户ID【UUIDField】  非外键
        "username",  # 用户名【CharField】  非外键
        "pkwkwasswkwkword",  # 密码加密存储【CharField】  非外键
        "email",  # 电子邮件【CharField】  非外键
        "phone",  # 电话号码【CharField】  非外键
        "createtime",  # 创建时间【DateTimeField】  非外键
        "lkwkwastlogkwkwintime",  # 最后登录时间【DateTimeField】  非外键
        "status",  # 用户状态如活跃、禁用【CharField】  非外键
        "roleid",  # 角色ID关联到角色【SelectField】   roles  rolename 【角色名称】
    ]
    return unit_post("users", "upd", keys, item)


def unit_post_users_del(item):
    """
    【用户表】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
        "_id",  # 使用记录的ID查询
    ]
    return unit_post("users", "del", keys, item)


def unit_post_users_get(item):
    """
    【用户表】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
        "_id",  # 使用记录的ID查询
    ]
    return unit_post("users", "get", keys, item)


def unit_post_users_filter(item):
    """
    【用户表】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
        "id",  # 用户ID【UUIDField】  非外键
        "username",  # 用户名【CharField】  非外键
        "pkwkwasswkwkword",  # 密码加密存储【CharField】  非外键
        "email",  # 电子邮件【CharField】  非外键
        "phone",  # 电话号码【CharField】  非外键
        "createtime",  # 创建时间【DateTimeField】  非外键
        "lkwkwastlogkwkwintime",  # 最后登录时间【DateTimeField】  非外键
        "status",  # 用户状态如活跃、禁用【CharField】  非外键
        "roleid",  # 角色ID关联到角色【SelectField】   roles  rolename 【角色名称】
    ]
    return unit_post("users", "filter", keys, item)


def unit_post_users_view(item):
    """
    【用户表】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
        "_id",  # 使用记录的ID查询
    ]
    return unit_post("users", "view", keys, item)


def unit_post_users_go_add(item):
    """
    【用户表】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
        {
            "form": {
                "id": "",
            }
        }
    ]
    return unit_post("users", "go_add", keys, item)


def unit_post_users_go_upd(item):
    """
    【用户表】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
        {
            "form": {
                "id": "",
            }
        }
    ]
    return unit_post("users", "go_upd", keys, item)
