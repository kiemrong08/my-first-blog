from django.shortcuts import render
from django.http import HttpResponse

from rango.models import Category
# Create your views here.
def index(request):
	category_list = Category.objects.order_by('-likes')[:5]
	#return HttpResponse("Rango says: Hello world! <br/> <a href='/rango/about'>About</a>")
	#Xây dựng từ điển để truyền template engine như là context.
	#Chú ý khóa boldmessage giống hệt {{boldmessage}} trong template.
	context_dict={'categories': category_list,'boldmessage': category_list}

	#Trả lại phản hồi đã được render để gửi đến client.
	#Tạo một hàm shortcut để khiến dễ dàng hơn.
	#Tham số đầu tiên phải là template định dùng.
	return render(request, 'rango/index.html', context_dict)
def about(request):
	return HttpResponse("Trở về trang <a href='/rango/'>chủ</a>")

def about_phu(request):
	return render(request,'rango/about.html')
