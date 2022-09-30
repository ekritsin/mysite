from django.shortcuts import render
from django.http import HttpResponse, Http404


# Create your views here.
def index(request):
    return render(request, "singlepage/index.html")


texts = ["<b>Hi,</b><br> I am <strong>Ermioni</strong><br>and<br> I am a data scientist!",
        "Praesent euismod auctor quam, id congue tellus malesuada vitae. Ut sed lacinia quam. Sed vitae mattis metus, vel gravida ante. Praesent tincidunt nulla non sapien tincidunt, vitae semper diam faucibus. Nulla venenatis tincidunt efficitur. Integer justo nunc, egestas eget dignissim dignissim,  facilisis, dictum nunc ut, tincidunt diam.",
        "Morbi imperdiet nunc ac quam hendrerit faucibus. Morbi viverra justo est, ut bibendum lacus vehicula at. Fusce eget risus arcu. Quisque dictum porttitor nisl, eget condimentum leo mollis sed. Proin justo nisl, lacinia id erat in, suscipit ultrices nisi. Suspendisse placerat nulla at volutpat ultricies",
        " "]

def section(request, num):
    if 1 <= num <= 4:
        return HttpResponse(texts[num-1])
    else:
        raise Http404("No such section")