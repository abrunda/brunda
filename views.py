from django.http import HttpResponse
import datetime
from django.shortcuts import render_to_response

#...

def today_is(request):
    now = datetime.datetime.now()
    return render_to_response('blog/datetime.html', {'now': now })
