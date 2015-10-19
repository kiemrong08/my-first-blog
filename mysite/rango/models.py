from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)

	def __str__(self):
		return self.name #nếu gọi tên class thì sẽ trả lại name

class Page(models.Model):
	category = models.ForeignKey(Category) #khóa ngoại đến bảng category
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)

	def __str__(self):
		return self.title
