from django.contrib import admin

from django.db import models
from martor.widgets import AdminMartorWidget
from .models import Article, Tag, ArticleTags, Sentence


class TagsInlineAdmin(admin.StackedInline):
    # 在models中找到关联
    model = Article.tags.through
    # 默认有五个，去掉多余的
    extra = 0 # 去掉空行
    # 让文章关联的标签可以移除
    can_delete = True 

class ArticleAdmin(admin.ModelAdmin):
    # save_on_top = True
    fieldsets = [
        (None, {'fields': ['title', 'content', 'create_time', 'update_time']}),
    ]
    # 只读字段
    readonly_fields = ['create_time', 'update_time']
    # show_change_link = True
    # 文章修改页面引入Tag模型
    inlines = (TagsInlineAdmin,)
    formfield_overrides = {
        models.TextField: {
            'widget': AdminMartorWidget
        }
    }

admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)
admin.site.register(Sentence)