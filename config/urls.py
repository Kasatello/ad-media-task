from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/ad/revenue_statistic/", include("revenue.urls")),
    path("api/ad/spend_statistic/", include("spend.urls")),
]
