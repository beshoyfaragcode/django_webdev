# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from pusher import Pusher
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

pusher = Pusher(app_id=u'501269', key=u'd5b0dd6e176ebb8783b9', secret=u'85b5a6f33e94fc7ac7f3')

def chatroom (request):
  return render (request,'chatroom/chatroom.html')
@csrf_exempt
def broadcast(request):
    pusher.trigger(u'a_channel', u'an_event', {u'name': request.user.username, u'message': request.POST['message']})
    return HttpResponse("done")