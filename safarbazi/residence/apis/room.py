from drf_spectacular.utils import extend_schema
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from safarbazi.residence.models import Room
from safarbazi.residence.selectors import get_residence
from safarbazi.residence.services import create_room


class RoomApi(APIView):
    class InputRoomSerializer(serializers.Serializer):
        residence = serializers.UUIDField(required=True)
        title = serializers.CharField(max_length=100, required=True)

    class OutPutRoomSerializer(serializers.ModelSerializer):
        class Meta:
            model = Room
            fields = '__all__'

    @extend_schema(request=InputRoomSerializer, responses=OutPutRoomSerializer)
    def post(self, request):
        serializer = self.InputRoomSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        residence = get_residence(residence_id=serializer.validated_data.get("residence"))

        try:
            room = create_room(
                title=serializer.validated_data.get("title"),
                residence=residence)
        except Exception as ex:
            return Response(data={'message': f"Database Error {ex}"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(self.OutPutRoomSerializer(room, context={"request": request}).data)
