from django.contrib import admin
from .models import Teacher, Subject, Post, Category

admin.site.register(Post)

class TeacherAdmin(admin.ModelAdmin):
    filter_horizontal = ('subjects',)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'subjects':
            if request.user.is_superuser:
                # Superuser sees all subjects
                kwargs['queryset'] = Subject.objects.all()
            else:
                # Other users (teachers) see only their associated subjects
                teacher = Teacher.objects.get(teacher=request.user)
                kwargs['queryset'] = teacher.subjects.all()
        return super().formfield_for_manytomany(db_field, request, **kwargs)

admin.site.register(Teacher, TeacherAdmin )
admin.site.register(Subject)
admin.site.register(Category)
