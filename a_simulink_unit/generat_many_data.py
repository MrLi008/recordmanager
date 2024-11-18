# coding=utf-8

"""
批量生成模拟数据
可在生成后删除.
"""
from datetime import datetime, timedelta
import os
import codecs
import time
import random

from faker import Faker
# from china_regions.data import provinces, get_cities_by_province, get_districts_by_city
import pandas
import numpy as np
import pandas as pd

def normal(size):
    arr = np.random.normal(size=size+1)
    arr = np.round(arr, decimals=2)
    return arr


def get(faker: Faker, mcfieldnamezh, mctablenamezh=''):
    """
    根据表字段的中文名修正为合适的生成方式
    扩展建议:
    根据字段名->实体名->枚举
    关联字段->同时生成多个字段
    """
    val = ''
    if 'ID' in mcfieldnamezh or '主键' in mcfieldnamezh or '唯一标识' in mcfieldnamezh:
        val = str(faker.uuid4())[:8]
        return val
    if '时间戳' == mcfieldnamezh:
        # val = str(int(time.mktime(faker.date_this_decade().timetuple())))
        # return val
        val = faker.date_between(
            start_date=datetime.now() - timedelta(days=3 * 4), end_date=datetime.now()
        )
        return val

    if '时间' in mcfieldnamezh:
        # 如果是创建时间，则应当小于修改时间，并且小于解析时间
        
        val = faker.date_between(start_date=datetime.now() - timedelta(days=3 * 4),
                                 end_date=datetime.now())
        return val
    if '日期' in mcfieldnamezh:
        val = faker.date_between(start_date=datetime.now() - timedelta(days=3 * 4),
                                 end_date=datetime.now())
        return val
    if '率' == mcfieldnamezh[-1]:
        val = int(normal(10)[faker.random.randint(0,10)])
        return val
    if '地点' in mcfieldnamezh:
        val = faker.address()
        return val
    # if '类型' in mcfieldnamezh or '类别' in mcfieldnamezh:
    #     val = faker.random.choice((
    #         # 根据文心一言/chatgpt/chatglm生产20个左右的类别即可.
    #     ))
    #     return val

        
    # 系统管理员
    
    # 系统管理员.管理员姓名 <CharField>
    # 
    if mcfieldnamezh == '管理员姓名':
        
        # 载入配置成功
        # 给出一些系统管理员表中管理员姓名的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '管理员姓名1', '管理员姓名2', '管理员姓名示例1', '管理员姓名2', 
    ))

        val = loadvalue
        
        return val
    
    
    # 权限表
    
    # 权限表.权限ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '权限ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 权限表.权限名称 <CharField>
    # 
    if mcfieldnamezh == '权限名称':
        
        # 载入配置成功
        # 给出一些权限表表中权限名称的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '读取权限', '写入权限', '编辑权限', '删除权限', '查看报告', '导出数据', '导入数据', '管理用户', '配置设置', '发送通知', '审核内容', '发布内容', '禁用账户', '启用账户', '重置密码', '访问后台', '查看日志', '下载文件', '上传文件', '执行命令', 
    ))

        val = loadvalue
        
        return val
    
    # 权限表.描述 <TextField>
    # 
    if mcfieldnamezh == '描述':
        
        # 载入配置成功
        # 给出一些权限表表中描述的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '字段1描述', '字段2描述', '字段3详细信息', '列4的用途', '数据5的含义', '特性6的说明', '属性7的注解', '值8的上下文', '列9的用途说明', '字段10的简短描述', '列11的详细解释', '数据12的用途', '特性13的简短说明', '属性14的详细描述', '值15的上下文解释', '字段16的用途', '列17的额外信息', '数据18的备注', '字段19的用途描述', '列20的简短注解', 
    ))

        val = loadvalue
        
        return val
    
    # 权限表.创建时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '创建时间':
        
        # 载入配置成功
        # 给出一些权限表表中创建时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23T09:15:30Z', '2023-10-22T14:45:12Z', '2023-10-21T21:30:00Z', '2023-10-20T12:15:45Z', '2023-10-19T08:30:15Z', '2023-10-18T17:00:00Z', '2023-10-17T10:45:30Z', '2023-10-16T15:15:15Z', '2023-10-15T22:00:00Z', '2023-10-14T11:30:45Z', '2023-10-13T06:45:15Z', '2023-10-12T19:00:00Z', '2023-10-11T13:15:30Z', '2023-10-10T07:45:12Z', '2023-10-09T20:30:00Z', '2023-10-08T11:15:45Z', '2023-10-07T05:00:15Z', '2023-10-06T18:30:00Z', '2023-10-05T12:45:30Z', '2023-10-04T09:15:15Z', 
    ))

        val = loadvalue
        
        return val
    
    # 权限表.更新时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '更新时间':
        
        # 载入配置成功
        # 给出一些权限表表中更新时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 09:00:00', '2023-10-23 10:15:30', '2023-10-23 11:30:45', '2023-10-23 12:45:15', '2023-10-23 14:00:00', '2023-10-23 15:15:30', '2023-10-23 16:30:45', '2023-10-23 17:45:15', '2023-10-24 08:00:00', '2023-10-24 09:15:30', '2023-10-24 10:30:45', '2023-10-24 11:45:15', '2023-10-24 13:00:00', '2023-10-24 14:15:30', '2023-10-24 15:30:45', '2023-10-24 16:45:15', '2023-10-25 07:00:00', '2023-10-25 08:15:30', '2023-10-25 09:30:45', 
    ))

        val = loadvalue
        
        return val
    
    # 权限表.所属系统模块 <CharField>
    # 
    if mcfieldnamezh == '所属系统模块':
        
        # 载入配置成功
        # 给出一些权限表表中所属系统模块的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue=faker.random.choice((
'',
))
        val = loadvalue
        
        return val
    
    # 权限表.动作类型如增删改查 <CharField>
    # 
    if mcfieldnamezh == '动作类型如增删改查':
        
        # 载入配置成功
        # 给出一些权限表表中动作类型如增删改查的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue=faker.random.choice((
'',
))
        val = loadvalue
        
        return val
    
    # 权限表.资源标识 <CharField>
    # 
    if mcfieldnamezh == '资源标识':
        
        # 载入配置成功
        # 给出一些权限表表中资源标识的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue=faker.random.choice((
'',
))
        val = loadvalue
        
        return val
    
    # 权限表.权限状态如启用、禁用 <CharField>
    # 
    if mcfieldnamezh == '权限状态如启用、禁用':
        
        # 载入配置成功
        # 给出一些权限表表中权限状态如启用、禁用的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '启用', '禁用', '半启用', '只读', '测试状态', '临时禁用', '维护中', '审核中', '待激活', '待审核', '已拒绝', '已过期', '即将过期', '特殊权限', '高级权限', '低级权限', '受限访问', '只读模式', '访客模式', '管理员模式', 
    ))

        val = loadvalue
        
        return val
    
    
    # 日志表
    
    # 日志表.日志ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '日志ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 日志表.用户ID关联到用户 <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '用户ID关联到用户':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 日志表.操作类型 <CharField>
    # 
    if mcfieldnamezh == '操作类型':
        
        # 载入配置成功
        # 给出一些日志表表中操作类型的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '创建', '更新', '删除', '查询', '导入', '导出', '备份', '恢复', '审核', '批准', '拒绝', '取消', '提交', '发布', '下架', '归档', '移动', '复制', '重命名', '修改权限', 
    ))

        val = loadvalue
        
        return val
    
    # 日志表.操作对象ID如记录ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '操作对象ID如记录ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 日志表.操作对象类型 <CharField>
    # 
    if mcfieldnamezh == '操作对象类型':
        
        # 载入配置成功
        # 给出一些日志表表中操作对象类型的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '用户', '订单', '产品', '库存', '评论', '支付', '退货', '优惠券', '活动', '消息', '通知', '日志', '客服', '供应商', '分类', '标签', '地址', '购物车', '发票', '收藏', 
    ))

        val = loadvalue
        
        return val
    
    # 日志表.描述 <TextField>
    # 
    if mcfieldnamezh == '描述':
        
        # 载入配置成功
        # 给出一些日志表表中描述的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '字段1描述', '字段2描述', '字段3详细信息', '列4的用途', '数据5的含义', '特性6的说明', '属性7的注解', '值8的上下文', '列9的用途说明', '字段10的简短描述', '列11的详细解释', '数据12的用途', '特性13的简短说明', '属性14的详细描述', '值15的上下文解释', '字段16的用途', '列17的额外信息', '数据18的备注', '字段19的用途描述', '列20的简短注解', 
    ))

        val = loadvalue
        
        return val
    
    # 日志表.地址 <TextField>
    # 
    if mcfieldnamezh == '地址':
        
        # 载入配置成功
        # 给出一些日志表表中地址的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '北京市朝阳区三里屯路1号', '上海市浦东新区世纪大道100号', '广州市天河区珠江新城华夏路8号', '深圳市福田区福华三路88号', '杭州市西湖区文三路478号', '成都市锦江区红星路二段99号', '重庆市渝中区解放碑步行街1号', '天津市和平区南京路123号', '北京市西城区金融大街1号', '上海市黄浦区南京东路200号', '广州市越秀区中山五路33号', '深圳市罗湖区深南东路5002号', '杭州市拱墅区莫干山路111号', '南京市秦淮区中山南路89号', '武汉市江汉区解放大道688号', '西安市碑林区南大街1号', '沈阳市和平区中山路123号', '长沙市天心区黄兴南路步行街88号', '青岛市市南区香港中路10号', '厦门市思明区中山路步行街1号', 
    ))

        val = loadvalue
        
        return val
    
    # 日志表.创建时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '创建时间':
        
        # 载入配置成功
        # 给出一些日志表表中创建时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23T09:15:30Z', '2023-10-22T14:45:12Z', '2023-10-21T21:30:00Z', '2023-10-20T12:15:45Z', '2023-10-19T08:30:15Z', '2023-10-18T17:00:00Z', '2023-10-17T10:45:30Z', '2023-10-16T15:15:15Z', '2023-10-15T22:00:00Z', '2023-10-14T11:30:45Z', '2023-10-13T06:45:15Z', '2023-10-12T19:00:00Z', '2023-10-11T13:15:30Z', '2023-10-10T07:45:12Z', '2023-10-09T20:30:00Z', '2023-10-08T11:15:45Z', '2023-10-07T05:00:15Z', '2023-10-06T18:30:00Z', '2023-10-05T12:45:30Z', '2023-10-04T09:15:15Z', 
    ))

        val = loadvalue
        
        return val
    
    # 日志表.日志状态如正常、异常 <CharField>
    # 
    if mcfieldnamezh == '日志状态如正常、异常':
        
        # 载入配置成功
        # 给出一些日志表表中日志状态如正常、异常的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue=faker.random.choice((
'',
))
        val = loadvalue
        
        return val
    
    
    # 评论表
    
    # 评论表.评论ID <TextField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '评论ID':
        
        # 载入配置成功
        # 给出一些评论表表中评论ID的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    'comment_id1', 'comment_id2', 'comment_id3', 'comment_id4', 'comment_id5', 'comment_id6', 'comment_id7', 'comment_id8', 'comment_id9', 'comment_id10', 'comment_id11', 'comment_id12', 'comment_id13', 'comment_id14', 'comment_id15', 'comment_id16', 'comment_id17', 'comment_id18', 'comment_id19', 'comment_id20', 
    ))

        val = loadvalue
        
        return val
    
    # 评论表.记录ID关联到记录 <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '记录ID关联到记录':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 评论表.用户ID关联到用户 <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '用户ID关联到用户':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 评论表.评论内容 <TextField>
    # 
    if mcfieldnamezh == '评论内容':
        
        # 载入配置成功
        # 给出一些评论表表中评论内容的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '这是一个很好的产品', '我喜欢这个设计', '功能很强大', '价格合理', '服务周到', '发货速度快', '非常满意', '期待下次购买', '质量不错', '颜色很好看', '推荐给大家', '性价比高', '使用很方便', '操作简单易懂', '非常满意的一次购物', '物流很快', '包装完好', '卖家态度好', '值得购买', '谢谢！'
    ))

        val = loadvalue
        
        return val
    
    # 评论表.创建时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '创建时间':
        
        # 载入配置成功
        # 给出一些评论表表中创建时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23T09:15:30Z', '2023-10-22T14:45:12Z', '2023-10-21T21:30:00Z', '2023-10-20T12:15:45Z', '2023-10-19T08:30:15Z', '2023-10-18T17:00:00Z', '2023-10-17T10:45:30Z', '2023-10-16T15:15:15Z', '2023-10-15T22:00:00Z', '2023-10-14T11:30:45Z', '2023-10-13T06:45:15Z', '2023-10-12T19:00:00Z', '2023-10-11T13:15:30Z', '2023-10-10T07:45:12Z', '2023-10-09T20:30:00Z', '2023-10-08T11:15:45Z', '2023-10-07T05:00:15Z', '2023-10-06T18:30:00Z', '2023-10-05T12:45:30Z', '2023-10-04T09:15:15Z', 
    ))

        val = loadvalue
        
        return val
    
    # 评论表.评论状态如审核通过、待审核、删除 <TextField>
    # 
    if mcfieldnamezh == '评论状态如审核通过、待审核、删除':
        
        # 载入配置成功
        # 给出一些评论表表中评论状态如审核通过、待审核、删除的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue=faker.random.choice((
'',
))
        val = loadvalue
        
        return val
    
    # 评论表.父评论ID用于构建评论树 <TextField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '父评论ID用于构建评论树':
        
        # 载入配置成功
        # 给出一些评论表表中父评论ID用于构建评论树的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue=faker.random.choice((
'',
))
        val = loadvalue
        
        return val
    
    # 评论表.点赞数 <CharField>
    # 
    if mcfieldnamezh == '点赞数':
        
        # 载入配置成功
        # 给出一些评论表表中点赞数的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '点赞数1', '点赞数2', '点赞数3', '点赞数4', '点赞数5', '点赞数6', '点赞数7', '点赞数8', '点赞数9', '点赞数10', '点赞数11', '点赞数12', '点赞数13', '点赞数14', '点赞数15', '点赞数16', '点赞数17', '点赞数18', '点赞数19', '点赞数20', 
    ))

        val = loadvalue
        
        return val
    
    
    # 记录附件表
    
    # 记录附件表.附件ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '附件ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 记录附件表.记录ID关联到记录 <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '记录ID关联到记录':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 记录附件表.文件名 <FileField>
    # 
    if mcfieldnamezh == '文件名':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 记录附件表.文件存储路径 <FileField>
    # 
    if mcfieldnamezh == '文件存储路径':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 记录附件表.文件大小 <FileField>
    # 
    if mcfieldnamezh == '文件大小':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 记录附件表.文件类型 <FileField>
    # 
    if mcfieldnamezh == '文件类型':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 记录附件表.上传时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '上传时间':
        
        # 载入配置成功
        # 给出一些记录附件表表中上传时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-03-15 09:00:00', '2023-03-15 10:15:30', '2023-03-15 11:30:45', '2023-03-15 12:45:15', '2023-03-15 14:00:00', '2023-03-15 15:15:30', '2023-03-15 16:30:45', '2023-03-15 17:45:15', '2023-03-16 08:00:00', '2023-03-16 09:15:30', '2023-03-16 10:30:45', '2023-03-16 11:45:15', '2023-03-16 13:00:00', '2023-03-16 14:15:30', '2023-03-16 15:30:45', '2023-03-16 16:45:15', '2023-03-17 07:00:00', '2023-03-17 08:15:30', '2023-03-17 09:30:45', '2023-03-17 10:45:15', 
    ))

        val = loadvalue
        
        return val
    
    # 记录附件表.上传者ID关联到用户 <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '上传者ID关联到用户':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 记录附件表.描述 <TextField>
    # 
    if mcfieldnamezh == '描述':
        
        # 载入配置成功
        # 给出一些记录附件表表中描述的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '字段1描述', '字段2描述', '字段3详细信息', '列4的用途', '数据5的含义', '特性6的说明', '属性7的注解', '值8的上下文', '列9的用途说明', '字段10的简短描述', '列11的详细解释', '数据12的用途', '特性13的简短说明', '属性14的详细描述', '值15的上下文解释', '字段16的用途', '列17的额外信息', '数据18的备注', '字段19的用途描述', '列20的简短注解', 
    ))

        val = loadvalue
        
        return val
    
    
    # 记录表
    
    # 记录表.记录ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '记录ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 记录表.记录标题 <CharField>
    # 
    if mcfieldnamezh == '记录标题':
        
        # 载入配置成功
        # 给出一些记录表表中记录标题的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue=faker.random.choice((
'',
))
        val = loadvalue
        
        return val
    
    # 记录表.记录内容 <TextField>
    # 
    if mcfieldnamezh == '记录内容':
        
        # 载入配置成功
        # 给出一些记录表表中记录内容的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue=faker.random.choice((
'',
))
        val = loadvalue
        
        return val
    
    # 记录表.分类ID关联到记录分类 <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '分类ID关联到记录分类':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 记录表.创建者ID关联到用户 <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '创建者ID关联到用户':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 记录表.创建时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '创建时间':
        
        # 载入配置成功
        # 给出一些记录表表中创建时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23T09:15:30Z', '2023-10-22T14:45:12Z', '2023-10-21T21:30:00Z', '2023-10-20T12:15:45Z', '2023-10-19T08:30:15Z', '2023-10-18T17:00:00Z', '2023-10-17T10:45:30Z', '2023-10-16T15:15:15Z', '2023-10-15T22:00:00Z', '2023-10-14T11:30:45Z', '2023-10-13T06:45:15Z', '2023-10-12T19:00:00Z', '2023-10-11T13:15:30Z', '2023-10-10T07:45:12Z', '2023-10-09T20:30:00Z', '2023-10-08T11:15:45Z', '2023-10-07T05:00:15Z', '2023-10-06T18:30:00Z', '2023-10-05T12:45:30Z', '2023-10-04T09:15:15Z', 
    ))

        val = loadvalue
        
        return val
    
    # 记录表.更新时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '更新时间':
        
        # 载入配置成功
        # 给出一些记录表表中更新时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 09:00:00', '2023-10-23 10:15:30', '2023-10-23 11:30:45', '2023-10-23 12:45:15', '2023-10-23 14:00:00', '2023-10-23 15:15:30', '2023-10-23 16:30:45', '2023-10-23 17:45:15', '2023-10-24 08:00:00', '2023-10-24 09:15:30', '2023-10-24 10:30:45', '2023-10-24 11:45:15', '2023-10-24 13:00:00', '2023-10-24 14:15:30', '2023-10-24 15:30:45', '2023-10-24 16:45:15', '2023-10-25 07:00:00', '2023-10-25 08:15:30', '2023-10-25 09:30:45', 
    ))

        val = loadvalue
        
        return val
    
    # 记录表.记录状态如公开、私有 <CharField>
    # 
    if mcfieldnamezh == '记录状态如公开、私有':
        
        # 载入配置成功
        # 给出一些记录表表中记录状态如公开、私有的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue=faker.random.choice((
'',
))
        val = loadvalue
        
        return val
    
    # 记录表.浏览次数 <CharField>
    # 
    if mcfieldnamezh == '浏览次数':
        
        # 载入配置成功
        # 给出一些记录表表中浏览次数的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '123', '456', '789', '101', '1234', '567', '890', '123', '45', '67', '89', '10', '111', '222', '333', '444', '555', '666', '777', '888', 
    ))

        val = loadvalue
        
        return val
    
    
    # 记录分类表
    
    # 记录分类表.分类ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '分类ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 记录分类表.分类名称 <CharField>
    # 
    if mcfieldnamezh == '分类名称':
        
        # 载入配置成功
        # 给出一些记录分类表表中分类名称的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '电子产品', '家用电器', '服装鞋帽', '食品饮料', '图书音像', '美妆护肤', '母婴用品', '家居家装', '运动户外', '汽车用品', '数码配件', '玩具乐器', '箱包配饰', '钟表眼镜', '珠宝首饰', '宠物用品', '文化娱乐', '办公用品', '厨具餐具', '礼品鲜花', 
    ))

        val = loadvalue
        
        return val
    
    # 记录分类表.关联父分类ID用于构建分类树 <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '关联父分类ID用于构建分类树':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 记录分类表.描述 <TextField>
    # 
    if mcfieldnamezh == '描述':
        
        # 载入配置成功
        # 给出一些记录分类表表中描述的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '字段1描述', '字段2描述', '字段3详细信息', '列4的用途', '数据5的含义', '特性6的说明', '属性7的注解', '值8的上下文', '列9的用途说明', '字段10的简短描述', '列11的详细解释', '数据12的用途', '特性13的简短说明', '属性14的详细描述', '值15的上下文解释', '字段16的用途', '列17的额外信息', '数据18的备注', '字段19的用途描述', '列20的简短注解', 
    ))

        val = loadvalue
        
        return val
    
    # 记录分类表.创建时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '创建时间':
        
        # 载入配置成功
        # 给出一些记录分类表表中创建时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23T09:15:30Z', '2023-10-22T14:45:12Z', '2023-10-21T21:30:00Z', '2023-10-20T12:15:45Z', '2023-10-19T08:30:15Z', '2023-10-18T17:00:00Z', '2023-10-17T10:45:30Z', '2023-10-16T15:15:15Z', '2023-10-15T22:00:00Z', '2023-10-14T11:30:45Z', '2023-10-13T06:45:15Z', '2023-10-12T19:00:00Z', '2023-10-11T13:15:30Z', '2023-10-10T07:45:12Z', '2023-10-09T20:30:00Z', '2023-10-08T11:15:45Z', '2023-10-07T05:00:15Z', '2023-10-06T18:30:00Z', '2023-10-05T12:45:30Z', '2023-10-04T09:15:15Z', 
    ))

        val = loadvalue
        
        return val
    
    # 记录分类表.更新时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '更新时间':
        
        # 载入配置成功
        # 给出一些记录分类表表中更新时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 09:00:00', '2023-10-23 10:15:30', '2023-10-23 11:30:45', '2023-10-23 12:45:15', '2023-10-23 14:00:00', '2023-10-23 15:15:30', '2023-10-23 16:30:45', '2023-10-23 17:45:15', '2023-10-24 08:00:00', '2023-10-24 09:15:30', '2023-10-24 10:30:45', '2023-10-24 11:45:15', '2023-10-24 13:00:00', '2023-10-24 14:15:30', '2023-10-24 15:30:45', '2023-10-24 16:45:15', '2023-10-25 07:00:00', '2023-10-25 08:15:30', '2023-10-25 09:30:45', 
    ))

        val = loadvalue
        
        return val
    
    # 记录分类表.显示顺序 <CharField>
    # 
    if mcfieldnamezh == '显示顺序':
        
        # 载入配置成功
        # 给出一些记录分类表表中显示顺序的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    'Field1', 'Field2', 'Field3', 'Field4', 'Field5', 'Field6', 'Field7', 'Field8', 'Field9', 'Field10', 'Field11', 'Field12', 'Field13', 'Field14', 'Field15', 'Field16', 'Field17', 'Field18', 'Field19', 'Field20', 'SELECT', 'Field1 AS Field1', 'Field2 AS Field2', 'Field3 AS Field3', '
        val = loadvalue
        
        return val
    
    # 记录分类表.分类状态如启用、禁用 <CharField>
    # 
    if mcfieldnamezh == '分类状态如启用、禁用':
        
        # 载入配置成功
        # 给出一些记录分类表表中分类状态如启用、禁用的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue=faker.random.choice((
'',
))
        val = loadvalue
        
        return val
    
    
    # 角色表
    
    # 角色表.角色ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '角色ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 角色表.角色名称 <CharField>
    # 
    if mcfieldnamezh == '角色名称':
        
        # 载入配置成功
        # 给出一些角色表表中角色名称的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '角色1', '角色2', '角色3', '角色4', '角色5', '角色6', '角色7', '角色8', '角色9', '角色10', '角色11', '角色12', '角色13', '角色14', '角色15', '角色16', '角色17', '角色18', '角色19', '角色20', 
    ))

        val = loadvalue
        
        return val
    
    # 角色表.描述 <TextField>
    # 
    if mcfieldnamezh == '描述':
        
        # 载入配置成功
        # 给出一些角色表表中描述的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '字段1描述', '字段2描述', '字段3详细信息', '列4的用途', '数据5的含义', '特性6的说明', '属性7的注解', '值8的上下文', '列9的用途说明', '字段10的简短描述', '列11的详细解释', '数据12的用途', '特性13的简短说明', '属性14的详细描述', '值15的上下文解释', '字段16的用途', '列17的额外信息', '数据18的备注', '字段19的用途描述', '列20的简短注解', 
    ))

        val = loadvalue
        
        return val
    
    # 角色表.创建时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '创建时间':
        
        # 载入配置成功
        # 给出一些角色表表中创建时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23T09:15:30Z', '2023-10-22T14:45:12Z', '2023-10-21T21:30:00Z', '2023-10-20T12:15:45Z', '2023-10-19T08:30:15Z', '2023-10-18T17:00:00Z', '2023-10-17T10:45:30Z', '2023-10-16T15:15:15Z', '2023-10-15T22:00:00Z', '2023-10-14T11:30:45Z', '2023-10-13T06:45:15Z', '2023-10-12T19:00:00Z', '2023-10-11T13:15:30Z', '2023-10-10T07:45:12Z', '2023-10-09T20:30:00Z', '2023-10-08T11:15:45Z', '2023-10-07T05:00:15Z', '2023-10-06T18:30:00Z', '2023-10-05T12:45:30Z', '2023-10-04T09:15:15Z', 
    ))

        val = loadvalue
        
        return val
    
    # 角色表.更新时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '更新时间':
        
        # 载入配置成功
        # 给出一些角色表表中更新时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 09:00:00', '2023-10-23 10:15:30', '2023-10-23 11:30:45', '2023-10-23 12:45:15', '2023-10-23 14:00:00', '2023-10-23 15:15:30', '2023-10-23 16:30:45', '2023-10-23 17:45:15', '2023-10-24 08:00:00', '2023-10-24 09:15:30', '2023-10-24 10:30:45', '2023-10-24 11:45:15', '2023-10-24 13:00:00', '2023-10-24 14:15:30', '2023-10-24 15:30:45', '2023-10-24 16:45:15', '2023-10-25 07:00:00', '2023-10-25 08:15:30', '2023-10-25 09:30:45', 
    ))

        val = loadvalue
        
        return val
    
    # 角色表.权限如JSON格式 <CharField>
    # 
    if mcfieldnamezh == '权限如JSON格式':
        
        # 载入配置成功
        # 给出一些角色表表中权限如JSON格式的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue=faker.random.choice((
'',
))
        val = loadvalue
        
        return val
    
    # 角色表.是否为默认角色 <BooleanField>
    # 
    if mcfieldnamezh == '是否为默认角色':
        
        val = faker.random.choice(('1', '0'))
        
        return val
    
    # 角色表.角色状态如启用、禁用 <CharField>
    # 
    if mcfieldnamezh == '角色状态如启用、禁用':
        
        # 载入配置成功
        # 给出一些角色表表中角色状态如启用、禁用的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue=faker.random.choice((
'',
))
        val = loadvalue
        
        return val
    
    
    # 用户表
    
    # 用户表.用户ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '用户ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 用户表.用户名 <CharField>
    # 
    if mcfieldnamezh == '用户名':
        
        # 载入配置成功
        # 给出一些用户表表中用户名的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry', 'Ivy', 'John', 'Kate', 'Larry', 'Mary', 'Nick', 'Olivia', 'Peter', 'Quincy', 'Rachel', 'Sam', 'Tom', 'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry', 'Ivy', 'John', 'Kate', 'Larry', 'Mary', 'Nick', 'Olivia', 'Peter', 'Quincy', 'Rachel', 'Sam', 'Tom', 
    ))

        val = loadvalue
        
        return val
    
    # 用户表.密码加密存储 <CharField>
    # 
    if mcfieldnamezh == '密码加密存储':
        
        # 载入配置成功
        # 给出一些用户表表中密码加密存储的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    'password_hash VARCHAR(255) NOT NULL', 'password_salt VARCHAR(255) NOT NULL', 'user_password_encrypted TEXT NOT NULL', 'account_pwd_secure VARCHAR(256) NOT NULL', 'secure_credential CHAR(60) NOT NULL', 'encrypted_pass BLOB NOT NULL', 'pwd_hash_value BINARY(64) NOT NULL', 'auth_token_encrypted TEXT NOT NULL', 'secure_pass_string VARCHAR(512) NOT NULL', 'pwd_encryption_key VARCHAR(128) NOT NULL', 'credential_secure_data TEXT NOT NULL', 'safe_password_storage TEXT NOT NULL', 'hash_of_password VARCHAR(255) NOT NULL', 'pwd_encryption_method VARCHAR(50) NOT NULL', 'password_protection TEXT NOT NULL', 'encrypted_credential_data BLOB NOT NULL', 'pwd_secure_string VARCHAR(512) NOT NULL', 'password_safe_hash VARCHAR(256) NOT NULL', 'secure_pwd_storage_field TEXT NOT NULL', 'encrypted_password_data TEXT NOT NULL', 
    ))

        val = loadvalue
        
        return val
    
    # 用户表.电子邮件 <CharField>
    # 
    if mcfieldnamezh == '电子邮件':
        
        # 载入配置成功
        # 给出一些用户表表中电子邮件的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    'example1@email.com', 'example2@email.com', 'example3@email.net', 'example4@domain.org', 'example5@company.com', 'example6@web.com', 'example7@mail.com', 'example8@info.net', 'example9@online.com', 'example10@contact.com', 'example11@address.com', 'example12@service.com', 'example13@support.org', 'example14@internet.com', 'example15@local.net', 'example16@user.com', 'example17@webmail.com', 'example18@inbox.org', 'example19@host.com', 'example20@email.org', 
    ))

        val = loadvalue
        
        return val
    
    # 用户表.电话号码 <CharField>
    # 
    if mcfieldnamezh == '电话号码':
        
        # 载入配置成功
        # 给出一些用户表表中电话号码的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '1234567890', '0987654321', '1112223334', '4445556667', '7778889990', '0001112223', '3334445556', '6667778889', '9990001112', '2223334445', '5556667778', '8889990001', '1357924680', '2468013579', '9876543210', '0123456789', '1029384756', '2130495867', '3241506978', '4352617089', 
    ))

        val = loadvalue
        
        return val
    
    # 用户表.创建时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '创建时间':
        
        # 载入配置成功
        # 给出一些用户表表中创建时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23T09:15:30Z', '2023-10-22T14:45:12Z', '2023-10-21T21:30:00Z', '2023-10-20T12:15:45Z', '2023-10-19T08:30:15Z', '2023-10-18T17:00:00Z', '2023-10-17T10:45:30Z', '2023-10-16T15:15:15Z', '2023-10-15T22:00:00Z', '2023-10-14T11:30:45Z', '2023-10-13T06:45:15Z', '2023-10-12T19:00:00Z', '2023-10-11T13:15:30Z', '2023-10-10T07:45:12Z', '2023-10-09T20:30:00Z', '2023-10-08T11:15:45Z', '2023-10-07T05:00:15Z', '2023-10-06T18:30:00Z', '2023-10-05T12:45:30Z', '2023-10-04T09:15:15Z', 
    ))

        val = loadvalue
        
        return val
    
    # 用户表.最后登录时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '最后登录时间':
        
        # 载入配置成功
        # 给出一些用户表表中最后登录时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 08:00:00', '2023-10-22 15:30:45', '2023-10-21 22:15:12', '2023-10-20 10:45:30', '2023-10-19 18:30:00', '2023-10-18 12:00:45', '2023-10-17 09:15:30', '2023-10-16 16:45:15', '2023-10-15 23:30:00', '2023-10-14 17:15:45', '2023-10-13 11:00:30', '2023-10-12 08:45:15', '2023-10-11 15:30:00', '2023-10-10 22:15:45', '2023-10-09 16:00:30', '2023-10-08 10:45:15', '2023-10-07 18:30:00', '2023-10-06 13:15:45', '2023-10-05 07:00:30', '2023-10-04 20:45:15', 
    ))

        val = loadvalue
        
        return val
    
    # 用户表.用户状态如活跃、禁用 <CharField>
    # 
    if mcfieldnamezh == '用户状态如活跃、禁用':
        
        # 载入配置成功
        # 给出一些用户表表中用户状态如活跃、禁用的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '活跃', '禁用', '待审核', '临时冻结', '已注销', '未知状态', 'VIP用户', '普通用户', '管理员', '实习生', '已离职', '已转正', '待支付', '已完成', '已取消', '已过期', '待激活', '已激活', '已锁定', '已解锁', 
    ))

        val = loadvalue
        
        return val
    
    # 用户表.角色ID关联到角色 <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '角色ID关联到角色':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    
    return val




# 系统管理员
def generate_supermanager(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='supermanager'
    fields_en = ['`username`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        # 管理员姓名 根据名称选择合适的函数来生成数据
        username = get(faker,'管理员姓名')
        values.append('\''+str(username)+'\'')
        
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 权限表
def generate_permkwkwissions(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='permkwkwissions'
    fields_en = ['`id`', '`name`', '`description`', '`createtime`', '`updatetime`', '`systemmodule`', '`actiontype`', '`resource`', '`status`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        
        
        
        
        # 权限名称 根据名称选择合适的函数来生成数据
        name = get(faker,'权限名称')
        values.append('\''+str(name)+'\'')
        
        
        
        
        # 描述 根据名称选择合适的函数来生成数据
        description = get(faker,'描述')
        values.append('\''+str(description)+'\'')
        
        
        
        
        # 创建时间 根据名称选择合适的函数来生成数据
        createtime = get(faker,'创建时间')
        values.append('\''+str(createtime)+'\'')
        
        
        
        
        # 更新时间 根据名称选择合适的函数来生成数据
        updatetime = get(faker,'更新时间')
        values.append('\''+str(updatetime)+'\'')
        
        
        
        
        # 所属系统模块 根据名称选择合适的函数来生成数据
        systemmodule = get(faker,'所属系统模块')
        values.append('\''+str(systemmodule)+'\'')
        
        
        
        
        # 动作类型如增删改查 根据名称选择合适的函数来生成数据
        actiontype = get(faker,'动作类型如增删改查')
        values.append('\''+str(actiontype)+'\'')
        
        
        
        
        # 资源标识 根据名称选择合适的函数来生成数据
        resource = get(faker,'资源标识')
        values.append('\''+str(resource)+'\'')
        
        
        
        
        # 权限状态如启用、禁用 根据名称选择合适的函数来生成数据
        status = get(faker,'权限状态如启用、禁用')
        values.append('\''+str(status)+'\'')
        
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 日志表
def generate_logs(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='logs'
    fields_en = ['`id`', '`userid`', '`action`', '`objectid`', '`objecttype`', '`description`', '`ipaddressip`', '`createtime`', '`status`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        
        
        
        
        # 本表字段：用户ID关联到用户--》关联表：57526--》字段：用户名
        if len(cache.get('用户ID关联到用户', [])) < 10:
            userid = str(len(cache.get('用户ID关联到用户', [])))
            # userid = get(faker,'用户ID关联到用户')
        else:
            userid = faker.random.choice(list(cache.get('用户ID关联到用户', )))
        
        
        # 用于外键补充 原字段：用户ID关联到用户【 57526 用户名 】
        if '用户ID关联到用户' not in cache:
            cache['用户ID关联到用户'] = set()
        cache['用户ID关联到用户'].add(userid)
        values.append('\''+str(userid)+'\'')
        
        
        
        # 操作类型 根据名称选择合适的函数来生成数据
        action = get(faker,'操作类型')
        values.append('\''+str(action)+'\'')
        
        
        
        
        # 操作对象ID如记录ID 根据名称选择合适的函数来生成数据
        objectid = get(faker,'操作对象ID如记录ID')
        values.append('\''+str(objectid)+'\'')
        
        
        
        
        # 操作对象类型 根据名称选择合适的函数来生成数据
        objecttype = get(faker,'操作对象类型')
        values.append('\''+str(objecttype)+'\'')
        
        
        
        
        # 描述 根据名称选择合适的函数来生成数据
        description = get(faker,'描述')
        values.append('\''+str(description)+'\'')
        
        
        
        
        # 地址 根据名称选择合适的函数来生成数据
        ipaddressip = get(faker,'地址')
        values.append('\''+str(ipaddressip)+'\'')
        
        
        
        
        # 创建时间 根据名称选择合适的函数来生成数据
        createtime = get(faker,'创建时间')
        values.append('\''+str(createtime)+'\'')
        
        
        
        
        # 日志状态如正常、异常 根据名称选择合适的函数来生成数据
        status = get(faker,'日志状态如正常、异常')
        values.append('\''+str(status)+'\'')
        
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 评论表
def generate_comments(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='comments'
    fields_en = ['`id`', '`reckwkwordid`', '`userid`', '`content`', '`createtime`', '`status`', '`parentid`', '`likes`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        
        
        
        
        # 本表字段：记录ID关联到记录--》关联表：57551--》字段：记录标题
        if len(cache.get('记录ID关联到记录', [])) < 10:
            reckwkwordid = str(len(cache.get('记录ID关联到记录', [])))
            # reckwkwordid = get(faker,'记录ID关联到记录')
        else:
            reckwkwordid = faker.random.choice(list(cache.get('记录ID关联到记录', )))
        
        
        # 用于外键补充 原字段：记录ID关联到记录【 57551 记录标题 】
        if '记录ID关联到记录' not in cache:
            cache['记录ID关联到记录'] = set()
        cache['记录ID关联到记录'].add(reckwkwordid)
        values.append('\''+str(reckwkwordid)+'\'')
        
        
        
        # 本表字段：用户ID关联到用户--》关联表：57526--》字段：用户名
        if len(cache.get('用户ID关联到用户', [])) < 10:
            userid = str(len(cache.get('用户ID关联到用户', [])))
            # userid = get(faker,'用户ID关联到用户')
        else:
            userid = faker.random.choice(list(cache.get('用户ID关联到用户', )))
        
        
        # 用于外键补充 原字段：用户ID关联到用户【 57526 用户名 】
        if '用户ID关联到用户' not in cache:
            cache['用户ID关联到用户'] = set()
        cache['用户ID关联到用户'].add(userid)
        values.append('\''+str(userid)+'\'')
        
        
        
        # 评论内容 根据名称选择合适的函数来生成数据
        content = get(faker,'评论内容')
        values.append('\''+str(content)+'\'')
        
        
        
        
        # 创建时间 根据名称选择合适的函数来生成数据
        createtime = get(faker,'创建时间')
        values.append('\''+str(createtime)+'\'')
        
        
        
        
        # 评论状态如审核通过、待审核、删除 根据名称选择合适的函数来生成数据
        status = get(faker,'评论状态如审核通过、待审核、删除')
        values.append('\''+str(status)+'\'')
        
        
        
        
        # 父评论ID用于构建评论树 根据名称选择合适的函数来生成数据
        parentid = get(faker,'父评论ID用于构建评论树')
        values.append('\''+str(parentid)+'\'')
        
        
        
        
        # 点赞数 根据名称选择合适的函数来生成数据
        likes = get(faker,'点赞数')
        values.append('\''+str(likes)+'\'')
        
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 记录附件表
def generate_reckwkwordattachments(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='reckwkwordattachments'
    fields_en = ['`id`', '`reckwkwordid`', '`filename`', '`filepath`', '`filesize`', '`filetype`', '`uploadtime`', '`uploaderid`', '`description`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        
        
        
        
        # 本表字段：记录ID关联到记录--》关联表：57551--》字段：记录标题
        if len(cache.get('记录ID关联到记录', [])) < 10:
            reckwkwordid = str(len(cache.get('记录ID关联到记录', [])))
            # reckwkwordid = get(faker,'记录ID关联到记录')
        else:
            reckwkwordid = faker.random.choice(list(cache.get('记录ID关联到记录', )))
        
        
        # 用于外键补充 原字段：记录ID关联到记录【 57551 记录标题 】
        if '记录ID关联到记录' not in cache:
            cache['记录ID关联到记录'] = set()
        cache['记录ID关联到记录'].add(reckwkwordid)
        values.append('\''+str(reckwkwordid)+'\'')
        
        
        
        # 文件名 根据名称选择合适的函数来生成数据
        filename = get(faker,'文件名')
        values.append('\''+str(filename)+'\'')
        
        
        
        
        # 文件存储路径 根据名称选择合适的函数来生成数据
        filepath = get(faker,'文件存储路径')
        values.append('\''+str(filepath)+'\'')
        
        
        
        
        # 文件大小 根据名称选择合适的函数来生成数据
        filesize = get(faker,'文件大小')
        values.append('\''+str(filesize)+'\'')
        
        
        
        
        # 文件类型 根据名称选择合适的函数来生成数据
        filetype = get(faker,'文件类型')
        values.append('\''+str(filetype)+'\'')
        
        
        
        
        # 上传时间 根据名称选择合适的函数来生成数据
        uploadtime = get(faker,'上传时间')
        values.append('\''+str(uploadtime)+'\'')
        
        
        
        
        # 本表字段：上传者ID关联到用户--》关联表：57526--》字段：用户名
        if len(cache.get('上传者ID关联到用户', [])) < 10:
            uploaderid = str(len(cache.get('上传者ID关联到用户', [])))
            # uploaderid = get(faker,'上传者ID关联到用户')
        else:
            uploaderid = faker.random.choice(list(cache.get('上传者ID关联到用户', )))
        
        
        # 用于外键补充 原字段：上传者ID关联到用户【 57526 用户名 】
        if '上传者ID关联到用户' not in cache:
            cache['上传者ID关联到用户'] = set()
        cache['上传者ID关联到用户'].add(uploaderid)
        values.append('\''+str(uploaderid)+'\'')
        
        
        
        # 描述 根据名称选择合适的函数来生成数据
        description = get(faker,'描述')
        values.append('\''+str(description)+'\'')
        
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 记录表
def generate_reckwkwords(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='reckwkwords'
    fields_en = ['`id`', '`title`', '`content`', '`categkwkworyid`', '`creatkwkworid`', '`createtime`', '`updatetime`', '`status`', '`views`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        
        
        
        
        # 记录标题 根据名称选择合适的函数来生成数据
        title = get(faker,'记录标题')
        values.append('\''+str(title)+'\'')
        
        
        
        
        # 记录内容 根据名称选择合适的函数来生成数据
        content = get(faker,'记录内容')
        values.append('\''+str(content)+'\'')
        
        
        
        
        # 本表字段：分类ID关联到记录分类--》关联表：57543--》字段：分类名称
        if len(cache.get('分类ID关联到记录分类', [])) < 10:
            categkwkworyid = str(len(cache.get('分类ID关联到记录分类', [])))
            # categkwkworyid = get(faker,'分类ID关联到记录分类')
        else:
            categkwkworyid = faker.random.choice(list(cache.get('分类ID关联到记录分类', )))
        
        
        # 用于外键补充 原字段：分类ID关联到记录分类【 57543 分类名称 】
        if '分类ID关联到记录分类' not in cache:
            cache['分类ID关联到记录分类'] = set()
        cache['分类ID关联到记录分类'].add(categkwkworyid)
        values.append('\''+str(categkwkworyid)+'\'')
        
        
        
        # 本表字段：创建者ID关联到用户--》关联表：57526--》字段：用户名
        if len(cache.get('创建者ID关联到用户', [])) < 10:
            creatkwkworid = str(len(cache.get('创建者ID关联到用户', [])))
            # creatkwkworid = get(faker,'创建者ID关联到用户')
        else:
            creatkwkworid = faker.random.choice(list(cache.get('创建者ID关联到用户', )))
        
        
        # 用于外键补充 原字段：创建者ID关联到用户【 57526 用户名 】
        if '创建者ID关联到用户' not in cache:
            cache['创建者ID关联到用户'] = set()
        cache['创建者ID关联到用户'].add(creatkwkworid)
        values.append('\''+str(creatkwkworid)+'\'')
        
        
        
        # 创建时间 根据名称选择合适的函数来生成数据
        createtime = get(faker,'创建时间')
        values.append('\''+str(createtime)+'\'')
        
        
        
        
        # 更新时间 根据名称选择合适的函数来生成数据
        updatetime = get(faker,'更新时间')
        values.append('\''+str(updatetime)+'\'')
        
        
        
        
        # 记录状态如公开、私有 根据名称选择合适的函数来生成数据
        status = get(faker,'记录状态如公开、私有')
        values.append('\''+str(status)+'\'')
        
        
        
        
        # 浏览次数 根据名称选择合适的函数来生成数据
        views = get(faker,'浏览次数')
        values.append('\''+str(views)+'\'')
        
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 记录分类表
def generate_reckwkwordcategkwkwories(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='reckwkwordcategkwkwories'
    fields_en = ['`id`', '`name`', '`parentid`', '`description`', '`createtime`', '`updatetime`', '`kwkwordernumber`', '`status`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        
        
        
        
        # 分类名称 根据名称选择合适的函数来生成数据
        name = get(faker,'分类名称')
        values.append('\''+str(name)+'\'')
        
        
        
        
        # 本表字段：关联父分类ID用于构建分类树--》关联表：57543--》字段：分类名称
        if len(cache.get('关联父分类ID用于构建分类树', [])) < 10:
            parentid = str(len(cache.get('关联父分类ID用于构建分类树', [])))
            # parentid = get(faker,'关联父分类ID用于构建分类树')
        else:
            parentid = faker.random.choice(list(cache.get('关联父分类ID用于构建分类树', )))
        
        
        # 用于外键补充 原字段：关联父分类ID用于构建分类树【 57543 分类名称 】
        if '关联父分类ID用于构建分类树' not in cache:
            cache['关联父分类ID用于构建分类树'] = set()
        cache['关联父分类ID用于构建分类树'].add(parentid)
        values.append('\''+str(parentid)+'\'')
        
        
        
        # 描述 根据名称选择合适的函数来生成数据
        description = get(faker,'描述')
        values.append('\''+str(description)+'\'')
        
        
        
        
        # 创建时间 根据名称选择合适的函数来生成数据
        createtime = get(faker,'创建时间')
        values.append('\''+str(createtime)+'\'')
        
        
        
        
        # 更新时间 根据名称选择合适的函数来生成数据
        updatetime = get(faker,'更新时间')
        values.append('\''+str(updatetime)+'\'')
        
        
        
        
        # 显示顺序 根据名称选择合适的函数来生成数据
        kwkwordernumber = get(faker,'显示顺序')
        values.append('\''+str(kwkwordernumber)+'\'')
        
        
        
        
        # 分类状态如启用、禁用 根据名称选择合适的函数来生成数据
        status = get(faker,'分类状态如启用、禁用')
        values.append('\''+str(status)+'\'')
        
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 角色表
def generate_roles(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='roles'
    fields_en = ['`id`', '`rolename`', '`description`', '`createtime`', '`updatetime`', '`permkwkwissions`', '`kwkwiskwkwdefault`', '`status`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        
        
        
        
        # 角色名称 根据名称选择合适的函数来生成数据
        rolename = get(faker,'角色名称')
        values.append('\''+str(rolename)+'\'')
        
        
        
        
        # 描述 根据名称选择合适的函数来生成数据
        description = get(faker,'描述')
        values.append('\''+str(description)+'\'')
        
        
        
        
        # 创建时间 根据名称选择合适的函数来生成数据
        createtime = get(faker,'创建时间')
        values.append('\''+str(createtime)+'\'')
        
        
        
        
        # 更新时间 根据名称选择合适的函数来生成数据
        updatetime = get(faker,'更新时间')
        values.append('\''+str(updatetime)+'\'')
        
        
        
        
        # 权限如JSON格式 根据名称选择合适的函数来生成数据
        permkwkwissions = get(faker,'权限如JSON格式')
        values.append('\''+str(permkwkwissions)+'\'')
        
        
        
        
        # 是否为默认角色 根据名称选择合适的函数来生成数据
        kwkwiskwkwdefault = get(faker,'是否为默认角色')
        values.append('\''+str(kwkwiskwkwdefault)+'\'')
        
        
        
        
        # 角色状态如启用、禁用 根据名称选择合适的函数来生成数据
        status = get(faker,'角色状态如启用、禁用')
        values.append('\''+str(status)+'\'')
        
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 用户表
def generate_users(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='users'
    fields_en = ['`id`', '`username`', '`pkwkwasswkwkword`', '`email`', '`phone`', '`createtime`', '`lkwkwastlogkwkwintime`', '`status`', '`roleid`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        
        
        
        
        # 用户名 根据名称选择合适的函数来生成数据
        username = get(faker,'用户名')
        values.append('\''+str(username)+'\'')
        
        
        
        
        # 密码加密存储 根据名称选择合适的函数来生成数据
        pkwkwasswkwkword = get(faker,'密码加密存储')
        values.append('\''+str(pkwkwasswkwkword)+'\'')
        
        
        
        
        # 电子邮件 根据名称选择合适的函数来生成数据
        email = get(faker,'电子邮件')
        values.append('\''+str(email)+'\'')
        
        
        
        
        # 电话号码 根据名称选择合适的函数来生成数据
        phone = get(faker,'电话号码')
        values.append('\''+str(phone)+'\'')
        
        
        
        
        # 创建时间 根据名称选择合适的函数来生成数据
        createtime = get(faker,'创建时间')
        values.append('\''+str(createtime)+'\'')
        
        
        
        
        # 最后登录时间 根据名称选择合适的函数来生成数据
        lkwkwastlogkwkwintime = get(faker,'最后登录时间')
        values.append('\''+str(lkwkwastlogkwkwintime)+'\'')
        
        
        
        
        # 用户状态如活跃、禁用 根据名称选择合适的函数来生成数据
        status = get(faker,'用户状态如活跃、禁用')
        values.append('\''+str(status)+'\'')
        
        
        
        
        # 本表字段：角色ID关联到角色--》关联表：57535--》字段：角色名称
        if len(cache.get('角色ID关联到角色', [])) < 10:
            roleid = str(len(cache.get('角色ID关联到角色', [])))
            # roleid = get(faker,'角色ID关联到角色')
        else:
            roleid = faker.random.choice(list(cache.get('角色ID关联到角色', )))
        
        
        # 用于外键补充 原字段：角色ID关联到角色【 57535 角色名称 】
        if '角色ID关联到角色' not in cache:
            cache['角色ID关联到角色'] = set()
        cache['角色ID关联到角色'].add(roleid)
        values.append('\''+str(roleid)+'\'')
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache


def generate():
    cache = dict()
    with codecs.open('faker.sql', 'w', encoding='utf-8') as out:
        sql = 'insert into {databasename}.{table} ({fields_en}) values({values});\r\n'
        faker = Faker('zh_CN')
        database = 'vm788_cb37c1767d7b256d'
        # 表名字符串,字段英文名

            
        # 系统管理员
        cache.update(generate_supermanager(faker, sql, out, database,cache=cache))
        
        # 权限表
        cache.update(generate_permkwkwissions(faker, sql, out, database,cache=cache))
        
        # 日志表
        cache.update(generate_logs(faker, sql, out, database,cache=cache))
        
        # 评论表
        cache.update(generate_comments(faker, sql, out, database,cache=cache))
        
        # 记录附件表
        cache.update(generate_reckwkwordattachments(faker, sql, out, database,cache=cache))
        
        # 记录表
        cache.update(generate_reckwkwords(faker, sql, out, database,cache=cache))
        
        # 记录分类表
        cache.update(generate_reckwkwordcategkwkwories(faker, sql, out, database,cache=cache))
        
        # 角色表
        cache.update(generate_roles(faker, sql, out, database,cache=cache))
        
        # 用户表
        cache.update(generate_users(faker, sql, out, database,cache=cache))
        

    from pymysql.connections import Connection
    from pymysql.cursors import DictCursor
    conn = Connection(port=3306, host='localhost', user='root', password=os.getenv('PM_UNIT_DATABASE_PSW', '123456'),
                      database='vm788_cb37c1767d7b256d')
    with codecs.open('faker.sql', 'r', encoding='utf-8') as ins:
        with conn.cursor(DictCursor) as cursor:
            count = 0
            for i, sql in enumerate(ins.readlines()):
                try:
                    cursor.execute(sql)
                    cursor.fetchall()
                except Exception as e:
                    print('error: ', e)
                    print(sql)
                    continue
                count += 1
                    
        conn.commit()
        print('Generate OK,Insert Total:', count, '个记录', i+1, '个sql')
    os.remove('faker.sql')


if __name__ == '__main__':
    generate()

