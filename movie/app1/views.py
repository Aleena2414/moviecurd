from django.shortcuts import render, redirect

from app1.models import Movie

from app1.forms import MovieForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# def home(request):
#     k=Movie.objects.all()
#     return render(request,'home.html',{'movie':k})
class Home(ListView):
    model = Movie
    template_name = "home.html"
    context_object_name = "movie"

    #get_query_set
    # def get_queryset(self):
    #     qs=super().get_queryset()
    #     queryset=qs.filter(title__icontains='a')
    #     return queryset

    # def get_queryset(self):
    #     qs=super().get_queryset()
    #     queryset=qs.filter(title='ARM')
    #     return queryset

    # def get_queryset(self):
    #     qs=super().get_queryset()
    #     queryset=qs.filter(year__gt=2023)
    #     return queryset

    # def get_queryset(self):
    #     qs=super().get_queryset()
    #     queryset=qs.filter(title__startswith='a')
    #     return queryset

    #get context_data
    # def get_context_data(self):
    #     context=super().get_context_data()
    #     context['name']='Ammu'
    #     context['age']=22
    #     return context
    extra_context = {'name':'arun','age':34}
# def addmovie1(request):#built in form
#     if(request.method=="POST",request.FILES):#AFTER FORM SUBMISSION
#         form=MovieForm(request.POST)#creates  form object using values that are passed through request.POST
#         if form.is_valid():#is_valid()built in function to check the values of form field
#             form.save()#save the form object in DB table
#             return redirect('home')#redirect to home page
#
#     form=MovieForm() #empty form object is created
#     context={'form':form}
#     return render(request,'add1.html',context)
class Addmovie1(CreateView):
    model = Movie
    fields = ['title','description','year','language','image']
    template_name = 'add1.html'
    success_url = reverse_lazy('app1:home')
# def addmovie(request):
#    if(request.method=='POST'):
#        t=request.POST['t']
#        d = request.POST['d']
#        y = request.POST['y']
#        l = request.POST['l']
#        i=request.FILES['i']
#
#        m=Movie.objects.create(title=t,description=d,year=y,language=l,image=i)
#        m.save()
#        return home(request)
#    return render(request,'add.html')
# def detail(request,i):
#     k=Movie.objects.get(id=i)
#     return render(request,'detail.html',{'movie':k})
class Detail(DetailView):
    model=Movie
    template_name = 'detail.html'
    context_object_name = 'movie'

# def edit(request,p):
#     k=Movie.objects.get(id=p)
#     if(request.method=="POST"):
#         k.title=request.POST['t']
#         k.description = request.POST['d']
#         k.year = request.POST['y']
#         k.language = request.POST['l']
#
#         if(request.FILES.get('i')==None):
#             k.save()
#         else:
#             k.image=request.FILES.get('i')
#         k.save()
#         return home(request)
#     return render(request, 'edit.html', {'movie': k})
class Edit(UpdateView):
        model = Movie
        fields = ['title', 'description', 'year', 'language', 'image']
        template_name = 'edit.html'
        success_url = reverse_lazy('app1:home')


# def delete(request,p):
#     k=Movie.objects.get(id=p)
#     k.delete( )
#     return home(request)
class Delete(DeleteView):
    model=Movie
    success_url = reverse_lazy('app1:home')
    template_name = 'delete.html'