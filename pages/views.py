from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Article, Tag, ArticleTags, Sentence
from .smtpwrapper import SMTPWrapper
from django.conf import settings
from ratelimit.decorators import ratelimit


import random

# FBV 首页
def index(request):
    bloglist = Article.objects.order_by("-update_time").all()[:5]
    return render(
        request, 
        "../templates/derive/index.html",
        {
            "bloglist": bloglist,
        })

# FBV 文章列表
def blogList(request):
    """文章列表页面视图函数"""
    # if request.method == "get":
    pagesize = request.GET.get("pagesize", default=None)
    page = request.GET.get("page", default=1)
    tag = request.GET.get("tag", default=None)
    # 所有文章
    bloglist = Article.objects.all()
    if tag:
        bloglist = bloglist.filter(tags=Tag.objects.filter(name=tag).first())
        print(bloglist, "*" * 5)
    # 分页大小
    if not pagesize:
        pagesize = 5 
    print(len(bloglist) // pagesize )
    # 页码总数
    pagesum = len(bloglist) // pagesize + 1
    tags = Tag.objects.all()
    return render(request,
        "../templates/derive/list.html",
        {
            "bloglist": bloglist,
            "pagesize": pagesize,
            "pagesum": pagesum,
            "page": page,
            "tags": tags
        })

# FBV 文章详细
def blogDetail(request, article_id):
    """文章详细页面视图函数"""
    if not article_id:
        raise Http404("文章没有找到")
    else:
        blog = Article.objects.filter(id=article_id).first()
        return render(request, "../templates/derive/detail.html", {"blog": blog})


def me(request):
    """关于我页面视图函数"""
    rhesis = Sentence.objects.all()
    # 随机条数
    k = 3
    print(rhesis, "*" * 30, type(rhesis))
    if len(rhesis) > k: 
        # import ipdb as pdb ; pdb.set_trace()
        # 随机产生索引
        idx = random.sample([i for i in range(len(rhesis))], k=3)
        # 取出对应的句子
        rhesis = [rhesis[i] for i in idx]
            

        # t = [rhesis[idx] for idx in random.sample([i for i in range(len(rhesis))], k=3)]
        # rhesis = random.sample(rhesis, k=3)

    return render(request, 
        "../templates/me/me.html", 
        {
            "rhesis": rhesis
        })


def tome(request):
    """给我留言页面视图函数"""
    return render(request, "../templates/me/tome.html")

@ratelimit(key="ip", rate="3/h")
def tomeAjax(request):
    """给我留言AJax函数"""
    data = {}
    # 获取邮件内容
    subject = request.GET.get("subject", "未命令主题")
    msg = request.GET.get("msg", "没有获取到内容")
    sender = request.GET.get("sender", "没有预留联系方式")

    # 判断是否超过访问限制，未超过发送邮件
    limited = getattr(request, "limited")
    print(limited, subject, msg, "*" * 60)
    if not limited:
        # 设置邮箱配置
        mail = SMTPWrapper(**settings.SMTP_CONFIG)
        # 发送邮箱
        mail.send(
            "lan2e@qq.com", 
            message="".join([
            '<div style="padding:1em;">',
                '<p style="padding:0 30em;">',
                    msg,
                '</p>',
                '<p style="text-align: right;padding:0 30em;">',
                    '联系方式:　',
                    '<span style="color:skyblue">',
                        sender,
                    '</span>',
                '</p>',
            '</div>'
            ]), 
            subject=subject,
            html=True
        )
        print("发送了")
        data["send"] = 1
    else:
        print("发送失败")
        data["send"] = 0
    return JsonResponse(data)