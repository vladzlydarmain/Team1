from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from osas3000.settings import EMAIL_HOST_USER


# Create your views here.
def showpage(request):
    movies = Movie.objects.all()
    context = {
        "movies":movies
    }
    
    if request.method == "POST":
        if "name" in request.POST:

            send_mail(
                "Recall",
                f"Клієнт {request.POST['name']} залишив свій відгук:{request.POST['review']}",
                EMAIL_HOST_USER,
                [EMAIL_HOST_USER],
                fail_silently=False
            )
    

    return render(request, "app3000/index.html", context=context)