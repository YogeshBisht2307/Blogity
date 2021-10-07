
from django.urls import path, include
from django.views.generic import TemplateView

app_name = 'blog'

urlpatterns = [
    # route url for displaying the index.html file which is inside templates folder
    path('', TemplateView.as_view(template_name = "blog/index.html")),
]
