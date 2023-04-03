from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Message
# Create your views here.
def index(request):
    if request.method == "POST":
        message = request.POST.get("message")
        msg = Message(message=message, datetime=datetime.today())
        msg.save()
    return render(request, "index.html")