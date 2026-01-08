from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Mission, Target
from .serializers import MissionSerializer, TargetSerializer
from rest_framework.decorators import action


class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    def destroy(self, request, *args, **kwargs):
        mission = self.get_object()
        if mission.cat:
            return Response(
                {"error": "Cannot delete a mission assigned to a cat"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().destroy(request, *args, **kwargs)
    
    @action(detail=True, methods=["post"])
    def assign_cat(self, request, pk=None):
        mission = self.get_object()
        cat_id = request.data.get("cat_id")

        if Mission.objects.filter(cat_id=cat_id).exists():
            return Response(
                {"error": "Cat already has a mission"},
                status=400
            )

        mission.cat_id = cat_id
        mission.save()
        return Response({"status": "cat assigned"})


class TargetViewSet(viewsets.ModelViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer

    def partial_update(self, request, *args, **kwargs):
        target = self.get_object()
        if target.is_completed or target.mission.is_completed:
            return Response(
                {"error": "Cannot update notes, target or mission is completed"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().partial_update(request, *args, **kwargs)
