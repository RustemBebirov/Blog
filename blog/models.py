from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.


class Blog(models.Model):
    #relation
    category = models.ManyToManyField('Category', verbose_name=("Category"),related_name='category')
    
    
    description = models.TextField("Description")
    name = models.CharField(("Name"),max_length=127)
    image = models.ImageField(("Image"))
    createdAt = models.DateTimeField("Created Time",auto_now_add=True)

    def __str__(self):
        return self.name
    

class Category(models.Model):
    #relation
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    
    slug = models.SlugField(max_length=255, unique=True,null=True,blank=True)
    name = models.CharField(("Name"),max_length=50, unique=True)

    def __str__(self):
        return self.name

class Like(models.Model):
    #relation
    blog = models.ForeignKey(Blog, verbose_name=("Blog"), on_delete=models.CASCADE,related_name='likes')
    
    isLike = models.BooleanField(("Like"),default=False)
    createdAt = models.DateTimeField("Created Time",auto_now_add=True)

    def __str__(self):
        return self.blog.name
    

class Comment(models.Model):
    #relation
    user = models.ForeignKey(User, verbose_name=("user"), on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, verbose_name=("blog"), on_delete=models.CASCADE)


    comment = models.TextField(("Comment"))
    createdAt = models.DateTimeField("Created Time",auto_now_add=True) 

    def __str__(self):
        return f"{self.user.username} in {self.blog}-a commenti"


class About(models.Model):

    title = models.CharField(("Title"), max_length=127)
    text = models.TextField(("About Detail"))
    img = models.ImageField(("Image"), upload_to='about_images')

    def __str__(self):
        return self.title
    

class Contact(models.Model):

    address = models.CharField(("Address"), max_length=127,null=True,blank=True)
    phone = models.IntegerField(("Phone Number"),null=True,blank=True)
    mail = models.EmailField(("Email"), max_length=254,null=True,blank=True)

    def __str__(self):
        return self.mail
