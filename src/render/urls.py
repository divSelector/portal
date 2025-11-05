from . import views
from django_distill import distill_path

urlpatterns = [
    distill_path('', views.index, name='index'),
]