from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static

from .views import PostsView, PostsDetail, AccountView, PostDelete, PostUpdateView


urlpatterns = [
    path('account/', AccountView.as_view(), name="account"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="update"),
    path('post/<int:pk>/delete/', PostDelete.as_view(), name="delete"),
    path('show_page/', PostsView.as_view(), name='show_page'),
    path('detail_page/<slug:slug>/', PostsDetail.as_view(), name="detail_page")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    


