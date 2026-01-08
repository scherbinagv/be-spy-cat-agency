from rest_framework import serializers
from .models import Mission, Target


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = "__all__"
        read_only_fields = ("mission",)

    def validate(self, attrs):
        instance = self.instance
        if instance:
            if instance.is_completed or instance.mission.is_completed:
                raise serializers.ValidationError(
                    "Cannot update notes of a completed target or mission"
                )
        return attrs

class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True)

    class Meta:
        model = Mission
        fields = ("id", "cat", "is_completed", "targets")

    def create(self, validated_data):
        targets_data = validated_data.pop("targets")

        if not (1 <= len(targets_data) <= 3):
            raise serializers.ValidationError("Mission must have 1–3 targets")

        mission = Mission.objects.create(**validated_data)

        for t in targets_data:
            Target.objects.create(mission=mission, **t)

        return mission

    def update(self, instance, validated_data):
        # Обновление миссии
        targets_data = validated_data.pop("targets", [])
        instance.cat = validated_data.get("cat", instance.cat)
        instance.is_completed = validated_data.get("is_completed", instance.is_completed)
        instance.save()

        for t_data in targets_data:
            t_id = t_data.get("id")
            if t_id:
                target = Target.objects.get(id=t_id, mission=instance)
                if target.is_completed or instance.is_completed:
                    continue  # Заморожено
                for key, value in t_data.items():
                    setattr(target, key, value)
                target.save()
        return instance



