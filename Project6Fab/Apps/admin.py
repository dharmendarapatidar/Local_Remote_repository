from django.contrib import admin
from .models import HomeModel, CommentModel

# class HomeModelAdmin(admin.ModelAdmin):
#
#     list_display = ['Reg_No', 'Date ', 'Time', 'First_Name', 'Last_Name', 'Mobile', 'Country_Code'
#                     , 'Qualification', 'Gender', 'Email', 'Course_Opted', 'Refrence', 'User_Id',]

class CommentModelAdmin(admin.ModelAdmin):

    list_display = ['home', 'Comments', 'Email',]

admin.site.register(HomeModel)
admin.site.register(CommentModel, CommentModelAdmin)