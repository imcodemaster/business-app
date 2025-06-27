from django.urls import path
from todo import views 
from .views import *

urlpatterns = [


    path('home/', views.home, name = 'home-todo'),
    path('task/' , TaskListView.as_view() , name = "task-list"),
    path('notes/' , NotesListView.as_view() , name = "notes-list"),
    path('task/<int:pk>/', TaskDetailView.as_view() , name = 'task-detail' ),
    path('weekproject/<int:pk>/', weekprojectDetailView.as_view() , name = 'weekproject-detail' ),
    path('task/new/', TaskCreateView.as_view() , name = 'task-create' ),
    path('notes/new/', NotesCreateView.as_view() , name = 'notes-create' ),
    path('task/<int:pk>/update/', TaskUpdateView.as_view() , name = 'task-update' ),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view() , name = 'task-delete' ),
    path('notes/<int:pk>/delete/', NotesDeleteView.as_view() , name = 'notes-delete' ),    
    path('task/<int:pk>/comment', TaskCommentCreateView.as_view() , name = 'task-comment' ),
    path('weekproject/' , weekprojectListView.as_view() , name = "weekproject-list"),
    path('weekproject/new/', weekprojectCreateView.as_view() , name = 'weekproject-create' ),
    path('weekproject/<int:pk>/update/', weekprojectUpdateView.as_view() , name = 'weekproject-update' ),
    path('weekproject/<int:pk>/delete/', weekprojectDeleteView.as_view() , name = 'weekproject-delete' ),
    path('event/new/', EventCreateView.as_view() , name = 'event-create' ),
    path('event/<int:pk>/update/', EventUpdateView.as_view() , name = 'event-update' ),
    path('event/<int:pk>/delete/', EventDeleteView.as_view() , name = 'event-delete' ),    
    path('event/<int:pk>/', EventDetailView.as_view() , name = 'event-detail' ),
    path('event/' , EventListView.as_view() , name = "event-list"),
    path('wallet/' , WalletListView.as_view() , name = "wallet-list"),
    path('wallet/<int:pk>/', WalletDetailView.as_view() , name = 'wallet-detail' ),
    path('wallet/new/', WalletCreateView.as_view() , name = 'wallet-create' ),
    path('wallet/<int:pk>/update/', WalletUpdateView.as_view() , name = 'wallet-update' ),
    path('wallet/<int:pk>/delete/', WalletDeleteView.as_view() , name = 'wallet-delete' ),
    path('wallet/<int:pk>/transistion', TransistionCreateView.as_view() , name = 'transistion' ),    

]




