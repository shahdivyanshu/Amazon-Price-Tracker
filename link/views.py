from django.shortcuts import render,redirect

from .forms import AddLinkForm
# Create your views here.
from .models import Link
from django.views.generic import DeleteView
from django.urls import reverse_lazy

def home(request):
	no_discount=0;
	error=None

	form =AddLinkForm(request.POST or None)
	if request.method=="POST":
		try:
			if form.is_valid():
				form.save()

		except AttributeError:
			error="Could not Process your request"

	form = AddLinkForm()
	query=Link.objects.all()
	items=query.count()

	if items>0:
		discount_list=[]
		for item in query:
			if item.old_price>item.current_price:
				discount_list.append(item)

		total_discount=len(discount_list)

	context={
	"query":query,
	"items":items,
	"total_discount":total_discount,
	"error":error,
	"form":form,

	}
	return render(request,'index.html',context)



class LinkDeleteView(DeleteView):
	model=Link
	template_name='confirm_del.html'
	success_url=reverse_lazy("home")


def updateprice(request):
	Qs=Link.objects.all()
	for things in Qs:
		things.save()
	return redirect("/")