from django.contrib import admin   

# Register your models here.
from cafe.models import Author, Genre, Book, BookInstance, Language


# Define the admin class
# genre 필드는 manytomanyfield여서 list_display에 직접 제시할수 없음
# 대신 정보를 문자로 제시 display_genre
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre') 


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')
    list_filter =('status', 'due_back')

    fieldsets = (
        (None, {'fields': ('book', 'imprint', 'id')}),
        ('Availability', {'fields': ('status', 'due_back')}),
    )


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

# Register the admin class with the associated model
# admin.site.register(Book)
# admin.site.register(BookInstance)
# admin.site.register(Author)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin) 
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Genre)
admin.site.register(Language)