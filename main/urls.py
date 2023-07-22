# Imports
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("licenta-reproducere/", views.licenta_reproducere, name = "licenta-reproducere"),
    path("legislatie/", views.legislatie, name = "legislatie"),
    path("politica-de-confidentialitate/", views.privacy_policy, name = "privacy-policy"),
    path("termeni-si-conditii/", views.terms_and_conditions, name = "terms-and-conditions"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
