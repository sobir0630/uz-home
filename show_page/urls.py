from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static

from .views import PostsView, PostsDetail, detail_page, send_email_form, AccountView, PostDelete, PostUpdateView, EditProfile, TogglePostStatusView


urlpatterns = [
    path('account/', AccountView.as_view(), name="account"),
    path('edit-profile/', EditProfile.as_view(), name="edit-profile"),
    path('send-email/<int:pk>/', send_email_form, name='send_email'),
    path('show/detail_page/<slug:slug>/', detail_page, name='detail_page'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="update"),
    path('post/<int:pk>/delete/', PostDelete.as_view(), name="delete"),
    path('post/toggle/<int:pk>/', TogglePostStatusView.as_view(), name='post_toggle'),
    path('show_page/', PostsView.as_view(), name='show_page'),
    path('detail_page/<slug:slug>/', PostsDetail.as_view(), name="detail_page")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    


