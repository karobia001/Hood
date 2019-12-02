from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.index,name='index'),

    url(r'^profile/',views.profile,name='profile'),
    url(r'^edit/profile$',views.edit_profile,name='edit-profile'),
    # url(r'^update/profile/(?P<user_name>\w{0,50})',views.update_profile,name='update-profile'),
    url(r'^update/profile/(\d+)',views.update_profile,name='update-profile'),
    url(r'^new/comment$',views.new_comment,name='comment'),
    url(r'^comments$',views.comments,name='comments'),

    url(r'^update/neighborhood$',views.update_neighborhood,name='update-neighborhood'),
    url(r'^post/',views.post,name='post'),
    url(r'^business/',views.business,name='business'),
    url(r'^contacts/',views.contacts,name='contacts'),
    url(r'^neighbourhood/(\d+)',views.neighbourhood,name='neighbourhood'),



    url(r'^businessdetails/(\d+)',views.businessdetails,name ='businessdetails'),

    url(r'^search/', views.search_results, name='search_results'),
    url(r'^neighborhood/(\d+)',views.neighborhood,name='neighborhood'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
