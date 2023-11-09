from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path('authentication/', include("authentication.urls")),
    path('courses/', include("profile.urls")),
    path('checkout/', include("checkout.urls")),
    path('sadakah/',include("sadakah.urls")),
    path('dashboard/', include("additional.urls")),
    path('contact/', include("contact.urls")),
    path('settings/', include("settings.urls")),
    path('blog/', include("blog.urls"))

    
]+static(settings.MEDIA_URL,                          document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
