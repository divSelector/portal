from django.urls import path, include

urlpatterns = [
    path('', include('render.urls'))
]
