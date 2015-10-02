from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
	#return HttpResponse("Rango says: Hello world! <br/> <a href='/rango/about'>About</a>")
	#Xây dựng từ điển để truyền template engine như là context.
	#Chú ý khóa boldmessage giống hệt {{boldmessage}} trong template.
	context_dict={'boldmessage': "I am bold font from context"}

	#Trả lại phản hồi đã được render để gửi đến client.
	#Tạo một hàm shortcut để khiến dễ dàng hơn.
	#Tham số đầu tiên phải là template định dùng.
	return render(request, 'rango/index.html', context_dict)
def about(request):
	return HttpResponse("Rango says here is the <a href='/rango/'>Index</a> page.")