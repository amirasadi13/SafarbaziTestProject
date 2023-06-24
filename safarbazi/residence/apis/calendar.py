from datetime import timedelta

from drf_spectacular.utils import extend_schema
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from safarbazi.residence.models import Date
from safarbazi.residence.selectors import get_room, get_or_create_date
from safarbazi.residence.validators import valid_date, dates_validator

"""

    CalendarApi is an APIView class that provides a post method for creating a calendar for a room.
    
    The post method takes in a request with the following parameters:
        room: A UUID field that is required and specifies the room for which the calendar is being created.
        dates: A list of DateFields that are required and specify the dates for which the calendar is being created.
        status: A ChoiceField that specifies the status of the dates in the calendar.
        base_amount: An IntegerField that is required and specifies the base amount for the dates in the calendar.
        adult_extra_amount: An IntegerField that is required and specifies the extra amount for adults for the dates in the calendar.
        child_extra_amount: An IntegerField that is required and specifies the extra amount for children for the dates in the calendar.
        baby_extra_amount: An IntegerField that is required and specifies the extra amount for babies for the dates in the calendar.
    
    The post method returns a response with the following parameters:
        room: A UUID field that specifies the room for which the calendar was created.
        dates: A list of DateFields that specify the dates for which the calendar was created.
        status: A ChoiceField that specifies the status of the dates in the calendar.
        base_amount: An IntegerField that specifies the base amount for the dates in the calendar.
        adult_extra_amount: An IntegerField that specifies the extra amount for adults for the dates in the calendar.
        child_extra_amount: An IntegerField that specifies the extra amount for children for the dates in the calendar.
        baby_extra_amount: An IntegerField that specifies the extra amount for babies for the dates in the calendar.
    
    The post method first validates the request data using the InputCalendarSerializer. 
        If the data is valid, it then attempts to get the room specified in the request. 
        If the room does not exist, a response with an error message is returned.
        If the room exists, the post method then attempts to get or create a calendar for the room. 
        It then validates the dates in the request and creates a set of dates. 
        If there is only one date in the request, the post method calls the _get_or_create_date method to get or create the date. 
        If there are two dates in the request, the post method calls the _get_date_range method to get or create the dates in the range.
        Finally, the post method updates the best amount of the calendar if necessary and returns a response with the created dates.
    

"""


class CalendarApi(APIView):
    class InputCalendarSerializer(serializers.Serializer):
        room = serializers.UUIDField(required=True)
        dates = serializers.ListSerializer(child=serializers.DateField(validators=[
            valid_date
        ]), validators=[
            dates_validator
        ], required=True)
        status = serializers.ChoiceField(choices=Date.STATUS)
        base_amount = serializers.IntegerField(required=True)
        adult_extra_amount = serializers.IntegerField(required=True)
        child_extra_amount = serializers.IntegerField(required=True)
        baby_extra_amount = serializers.IntegerField(required=True)

    class OutPutCalendarSerializer(serializers.ModelSerializer):
        class Meta:
            model = Date
            fields = '__all__'

    @extend_schema(request=InputCalendarSerializer, responses=OutPutCalendarSerializer)
    def post(self, request):
        serializer = self.InputCalendarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        valid_dates = serializer.validated_data.get("dates")

        room = get_room(room_id=serializer.validated_data.get("room"))

        if len(valid_dates) == 1:
            self._get_or_create_single_date(date=valid_dates[0], room=room,
                                            validated_data=serializer.validated_data)
        else:
            self._get_date_range(start_date=valid_dates[0], end_date=valid_dates[1], room=room,
                                 validated_data=serializer.validated_data)

        return Response(data={'message': 'Successfully updated calendar'}, status=status.HTTP_200_OK)

    @staticmethod
    def _get_or_create_single_date(date, room, validated_data):
        return get_or_create_date(date=date,
                                  room=room,
                                  base_amount=validated_data.get("base_amount"),
                                  status=validated_data.get("status"),
                                  adult_extra_amount=validated_data.get("adult_extra_amount"),
                                  child_extra_amount=validated_data.get("child_extra_amount"),
                                  baby_extra_amount=validated_data.get("baby_extra_amount"))

    @staticmethod
    def _get_date_range(start_date, end_date, room, validated_data):
        for date in range(int((end_date - start_date).days) + 1):
            item = CalendarApi._get_or_create_single_date(date=start_date + timedelta(date), room=room,
                                                          validated_data=validated_data)
