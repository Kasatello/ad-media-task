from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.views import APIView

from revenue.models import RevenueStatistic
from spend.models import SpendStatistic


class RevenueStatisticAPIView(APIView):

    def get(self, request):
        queryset = RevenueStatistic.objects.values("name", "date").annotate(
            total_revenue=Sum("revenue"),
        )

        for entry in queryset:
            spend_entry = SpendStatistic.objects.filter(
                name=entry["name"], date=entry["date"]
            ).aggregate(
                total_spend=Sum("spend"),
                total_impressions=Sum("impressions"),
                total_clicks=Sum("clicks"),
                total_conversion=Sum("conversion"),
            )
            entry.update(spend_entry)

        return Response(queryset)
