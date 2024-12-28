from django.shortcuts import render

from django.views.generic import View

from store.forms import Bookform

# Create your views here.

# BookCreateView
# url:localhost:8000/books/add
# method:
 
    #  GET:book_add.html,form
    # POST:create book object

class BookCreateView(View):
  
     def get(self,request,*args,**kwargs):

        form_instance=Bookform()

        return render(request,"book_create.html",{"forms":form_instance})


     def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=Bookform(form_data)


        if form_instance.is_valid():
            data=form_instance.cleaned_data

            Book.objects.create(
                title=data.get("title"),
                author=data.get("author"),
                price=data.get("price"),
                genre=data.get("genre"),
                language=data.get("language")

            )

