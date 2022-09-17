from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200 , null=True , blank=True)
    gender=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Library(models.Model):
    booktitle=models.CharField(max_length=250)
    bookid=models.IntegerField(5 , null=True , blank=True)
    is_available=models.BooleanField(null=True , blank=True)

    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    image=models.FileField(upload_to="blog/app/media/Library",null=True,blank=True)

    def __str__(self):
        return self.booktitle




    
    


    

    