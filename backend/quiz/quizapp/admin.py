from django.contrib import admin
from .models import Quiz, Answer, Question

admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Quiz)
