from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Location, SafetyReport
from .serializers import LocationSerializer, SafetyReportSerializer
import math

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class SafetyReportViewSet(viewsets.ModelViewSet):
    queryset = SafetyReport.objects.all()
    serializer_class = SafetyReportSerializer


@api_view(['GET'])
def get_safety_score(request, location_id):
    try:
        location = Location.objects.get(id=location_id)
        reports = location.reports.all()

        score = 100

        for report in reports:
            if report.report_type == "HARASSMENT":
                score -= 25   # 👈 your logic
            elif report.report_type == "THEFT":
                score -= 10

            elif report.report_type == "FIGHT":
                score -= 30
            elif report.report_type == "CONFLICT":
                score -= 35
            elif report.report_type == "RIOT":
                score -= 50

            elif report.report_type == "NO_CROWD":
                score -= 8

            elif report.report_type == "POLICE_PATROL":
                score += 10
            elif report.report_type == "STREET_LIGHT":
                score += 5

        score = max(0, min(100, score))

        return Response({
            "location": location.name,
            "score": score,
            "total_reports": reports.count(),
        })

    except Location.DoesNotExist:
        return Response({"error": "Location not found"}, status=404)