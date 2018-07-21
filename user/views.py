from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import DetailView ,UpdateView , View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


from .models import Users

# Create your views here.
def go_to_login(request):
    if request.user.is_authenticated:
        return redirect("/payam")
    else:
        return HttpResponseRedirect("/login/")


class ProfUpdate(LoginRequiredMixin,UpdateView):
    template_name="prof_update.html"
    model = Users
    fields = ['name','email','myfave','color']
    # success_url = "/login/"
    def get_context_data(self , *args,**kwargs):
        context = super(ProfUpdate , self).get_context_data(*args,**kwargs)
        follow_req = self.request.user
        is_following = False
        to_follow = context['object']
        if follow_req in to_follow.follower.all():
            is_following = True
        context['is_following'] = is_following
        x = Users.objects.get(user__username=to_follow)
        color = "#"+x.color
        print(color)
        context['color']=color
        return context

class Follow(View ,LoginRequiredMixin):
    def post(self ,request,*args,**kwrags):
        to_follow =request.POST.get("username")
        follower = request.user
        prof = Users.objects.get(user__username=to_follow)
        if follower in prof.follower.all():
            prof.follower.remove(follower)
        else:
            prof.follower.add(follower)
        return redirect(f"/update/{to_follow}")

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
