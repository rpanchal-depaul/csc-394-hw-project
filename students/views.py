from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.core import serializers

JSONSerializer = serializers.get_serializer("json")

json_serializer = JSONSerializer()




# Create your views here.

@login_required
def index(request):


    student_json = json_serializer.serialize(request.user.student)


    return render(request, student_json)