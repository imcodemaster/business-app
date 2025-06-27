from django.contrib import admin
from .models import Post , PostComment ,  Ticket , order_list , myorder
from django.contrib.admin.options import ModelAdmin


# Register your models here.
class PostAdmin(ModelAdmin):
	list_display = ['subject','published']
	search_field = ['published']
	list_filter = [ 'subject' ,  'published']


admin.site.register(Post, PostAdmin)

#my_order_
class myorderAdmin(ModelAdmin):
	list_display = ['first_name','date' , 'item' , 'company', 'date']
	search_field = ['first_name','date' , 'item' ,]
	list_filter = [ 'first_name','date' , 'item' ,]


admin.site.register(myorder, myorderAdmin)

class PostCommentAdmin(ModelAdmin):
	list_display = ['user','post','published', 'comment_content']
	search_field = ['user','post',]
	list_filter = [ 'user', 'published' ,'post',]


admin.site.register(PostComment, PostCommentAdmin)

class TicketAdmin(ModelAdmin):
	list_display = ['subject', 'author']
	search_field =  ['subject', 'author']
	list_filter =  ['subject', 'author']

admin.site.register(Ticket, TicketAdmin)


class order_listAdmin(ModelAdmin):
	list_display = ['user', 'date'  ]
	search_field = ['user' , 'date'  ]
	list_filter = [ 'user' ,  'date' ]

admin.site.register(order_list, order_listAdmin)
