from django.contrib import admin
from .models import Task , TaskComment , WeekProject , Event , Wallet , Transistion , Notes 
from django.contrib.admin.options import ModelAdmin


# Register your models here.
class TaskAdmin(ModelAdmin):
	list_display = ['taskname','author']
	search_field = ['author']
	list_filter = [ 'author', 'published']


admin.site.register(Task, TaskAdmin)


class NotesAdmin(ModelAdmin):
	list_display = ['note','published', 'author']
	search_field = ['author']
	list_filter = [ 'author', 'published']


admin.site.register(Notes, NotesAdmin)


class WalletAdmin(ModelAdmin):
	list_display = ['person_name','published', 'author']
	search_field = ['author']
	list_filter = [ 'author', 'published']


admin.site.register(Wallet, WalletAdmin)


class EventAdmin(ModelAdmin):
	list_display = ['eventname', 'eventon', 'published', 'author']
	search_field = ['author']
	list_filter = [ 'author', 'published']


admin.site.register(Event, EventAdmin)


class TaskCommentAdmin(ModelAdmin):
	list_display = ['author','task','published', 'comment_content']
	search_field = ['author','task',]
	list_filter = [ 'author', 'published' ,'task',]


admin.site.register(TaskComment, TaskCommentAdmin)

class WeekProjectAdmin(ModelAdmin):
	list_display = ['job', 'author','published']
	search_field = [ 'author', 'published']
	list_filter = ['author', 'published']

admin.site.register(WeekProject, WeekProjectAdmin)


class TransistionAdmin(ModelAdmin):
	list_display = ['author','published', 'payment_status' , 'payment_mode' , 'comment' , 'amount']
	search_field = [  'published' , 'author','published']
	list_filter = ['published', 'author','published']

admin.site.register(Transistion, TransistionAdmin)
