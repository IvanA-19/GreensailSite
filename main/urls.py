from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('history/', views.history, name='history'),
    path('teachers/', views.teachers, name='teachers'),
    path('teachers/<int:teacher_id>', views.teacher, name='teacher'),
    path('news/', views.news, name='news'),
    path('mugs', views.mugs, name='mugs'),
    path('mugs/<int:mug_id>', views.mug, name='mug'),
    path('certificate/', views.certificate, name='certificate'),
    path('contests/', views.contests, name='contests'),
    path('contests/<int:contest_id>', views.contest, name='contest'),
    path('masterclasses/', views.masterclasses, name='masterclasses'),
    path('masterclasses/<int:masterclass_id>', views.masterclass, name='masterclass'),
    path('events/', views.events, name='events'),
    path('events/<int:event_id>', views.event, name='event'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

