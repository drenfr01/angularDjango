from django.contrib import admin
from interests.models import Subject
from interests.models import Book
from interests.models import Membership

admin.site.register(Subject)
admin.site.register(Book)
admin.site.register(Membership)
