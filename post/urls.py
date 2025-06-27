from django.urls import path
from post import views 
from .views import *

urlpatterns = [

    path('post/' , PostListView.as_view() , name = "post-list"),
    path('post/<int:pk>/', PostDetailView.as_view() , name = 'post-detail' ),
   	path('like/<int:pk>/', LikeView , name = 'post-like' ),
 	path('post/new/', PostCreateView.as_view() , name = 'post-create' ),
    path('order/new/', MyOrderView.as_view() , name = 'order-create' ),
    path('post/<int:pk>/update/', PostUpdateView.as_view() , name = 'post-update' ),
    path('post/<int:pk>/delete/', PostDeleteView.as_view() , name = 'post-delete' ),
    path('post/<int:pk>/comment', PostCommentCreateView.as_view() , name = 'post-comment' ),
    path('ticket/' , TicketListView.as_view() , name = "ticket-list"),
    path('ticket/new/', TicketCreateView.as_view() , name = 'ticket-create' ),
    path('ticket/<int:pk>/update/', TicketUpdateView.as_view() , name = 'ticket-update' ),
    path('ticket/<int:pk>/delete/', TicketDeleteView.as_view() , name = 'ticket-delete' ),
    path('order-list/', views.OrderList , name = 'order-report' ),
    path('order-list-pdf/', orderlistpdfView.as_view(), name = 'orderpdf'),
]





