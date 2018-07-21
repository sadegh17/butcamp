from django.shortcuts import render
from django.views.generic import ListView , DeleteView
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.db.models import Q


from .models import Payam
from user.models import Users
from .form import PayamForm
from privatepayam.models import Private
# Create your views here.
karbar = get_user_model()

class DeleteMessage(DeleteView):
    template_name = "delete_message.html"
    model = Payam
    success_url = "/payam"

class FollowingsView(ListView):
    template_name="followings.html"
    def get_queryset(self):
        slug =self.kwargs.get("slug")
        # user=self.request.user
        user=karbar.objects.get(username=slug)
        queryset = user.is_follow.all()
        return queryset

class FollowersView(ListView):
    template_name="followers.html"
    def get_queryset(self):
        slug =self.kwargs.get("slug")
        user=Users.objects.get(user__username=slug)
        queryset = user.follower.all()
        return queryset

def message_list(request):
    template_name="message_list.html"
    form = PayamForm()
    query=request.GET.get("q")

    prof =[x.user.id for x in request.user.is_follow.all()]
    prof.append(request.user.id)
    qs = Payam.objects.filter(owner__id__in=prof)
    context = {"form" :form , "object_list": qs}
    if query :
        context['search']=True
        context['object_list'] = karbar.objects.filter(username=query)
    if request.method == "POST":
        form = PayamForm(request.POST)
        if form.is_valid():
        	Payam.objects.create(
        		message=form.cleaned_data.get("message"),
                owner = request.user
        	)
        return HttpResponseRedirect("/payam")
    mabda=request.user.username
    newpv = Private.objects.filter(Q( dest__username=mabda , read=False))
    context['newpv']=newpv.exists()

    return render(request , template_name , context)
