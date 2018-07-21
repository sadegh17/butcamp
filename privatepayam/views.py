from django.shortcuts import render , redirect
from django.views.generic import ListView ,View ,DeleteView
from django.db.models import Q
from django.contrib.auth import get_user_model

from .models import Private
from .form import SendPV
# Create your views here.
karbar = get_user_model()

class PVList(ListView):
    template_name="pv_list.html"

    def get_queryset(self):
        maghsad = self.kwargs.get("slug")
        mabda = self.request.user.username
        qs = Private.objects.filter(Q(owner__username=mabda , dest__username=maghsad) |
                                    Q(owner__username=maghsad , dest__username=mabda)
                                    )[:10]

        update = Private.objects.filter(Q(owner__username=maghsad , dest__username=mabda)).update(read = True)

        return qs
    def get_context_data(self , *args,**kwargs):
        context = super(PVList , self).get_context_data(*args,**kwargs)
        context['maghsad']=self.kwargs.get("slug")
        matn = self.request.GET.get("q")
        slug=self.kwargs.get("slug")
        user=karbar.objects.get(username=slug)
        if matn :
            Private.objects.create(
                                    owner=self.request.user,
                                    dest=user,
                                    matn=matn)

        return context

class ListOfPV(View):
    def get(self ,request, *args,**kwargs):
        template_name="list_of_pv.html"
        mabda=request.user.username
        qs =[x.dest.username  for x in Private.objects.filter(
                                    Q(owner__username=mabda ) | Q(dest__username=mabda)
                                    ).order_by("time")]
        qs +=[x.owner.username  for x in Private.objects.filter(
                                    Q(owner__username=mabda ) | Q(dest__username=mabda)
                                    ).order_by("time")]
        withoutme=[x for x in qs if x != mabda]
        norepet=list(set(withoutme))
        newpv =[x.owner.username for x in Private.objects.filter(Q( dest__username=mabda , read=False))]
        context ={'list':norepet , 'new':newpv}
        return render(request,template_name,context)
#
# class RemovePVList(View):
#     def get(self ,request, *args,**kwargs):
#         maghsad = self.kwargs.get("slug")
#         mabda = self.request.user.username
#         Private.objects.filter(Q(owner__username=mabda , dest__username=maghsad) |
#                                     Q(owner__username=maghsad , dest__username=mabda)
#                                     ).delete()
#         return redirect("/pv/send")
