from django.shortcuts import render, redirect

from django.forms.models import model_to_dict
from django.core.serializers import serialize

from . import models
# Create your views here.
#username : aravinds, password : password


'''class TweetModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.tweet
        fields = "__all__"
'''

def base_page(request):
	return render(request,'base/base.html')

def get_values(request):
	print(request.method)
	if(request.method == "POST"):
		print(request.POST['firstname'])

		rec = models.tweet(text=request.POST['firstname'])
		rec.save()

	#context = serialize('json',models.tweet.objects.all())
	context = models.tweet.objects.all().order_by('-date_post')

	return render(request,'base/base.html',{'context':context})