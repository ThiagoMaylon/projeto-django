from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls'))
]

handler404 = 'core.views.handler404'
handler500 = 'core.views.handler500'