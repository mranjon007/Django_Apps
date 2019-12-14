from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ajax_app/', include('ajax_app.urls'))
]
