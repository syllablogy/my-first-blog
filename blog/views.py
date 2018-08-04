from django.shortcuts import render
from .models import Post
def acceuil(request):
	return render(request,'blog/acceuil.html',{})
	
# Create your views here.

def liste_post(request):
	tous_les_postes = Post.objects.all ()
	return render(request,"blog/acceuil.html" , {"tous_les_postes": tous_les_postes})
