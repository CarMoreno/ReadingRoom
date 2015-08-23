from django.conf.urls import include, url
from django.views.generic.base import RedirectView
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', RedirectView.as_view(url='/biblioteca/'), name='index'),#Esta linea me redirige de la raiz (localhost:8000) a sitiolectura (localhost:8000/sitiolectura), en dicho folder debra de haber una url que coincida con el patron
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sitiolectura/', include('biblioteca.urls', namespace='sitio')),
]
