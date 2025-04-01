from django.contrib import admin
from django.urls import re_path
from .views import home_view, PestsView, PestDetailView

urlpatterns = [
    re_path(r'^$', home_view, name='home'),  # Matches root URL
    re_path(r'^pests/$', PestsView.as_view(), name='pests'),  # Matches /pests/
    re_path(r'^pest_detail/(?P<key>[a-zA-Z0-9_-]+)/$', PestDetailView.as_view(), name='pest_detail'),  # Matches e.g. /pest_detail/p1/
    re_path(r'^admin/', admin.site.urls),  # Matches /admin/
]
