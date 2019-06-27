# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import JsonResponse

from django.template import RequestContext
from django.shortcuts import render_to_response



def home(request):
	return render(request, "helloworld/index.html",{})