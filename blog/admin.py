from django.contrib import admin

# Register your models here.
from .models import Blog,Category,Comment,Like,About,Contact

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(About)
admin.site.register(Contact)