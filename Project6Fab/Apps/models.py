from django.db import models


class HomeModel(models.Model):
    Reg_No = models.IntegerField(primary_key=True)
    Date = models.DateField()
    Time = models.TimeField()
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    Mobile = models.IntegerField()
    Country_Code = models.IntegerField()
    Qualification = models.CharField(max_length=20)
    Gender = models.CharField(max_length=10)
    Email = models.EmailField()
    # Course_Opted = models.CharField(max_length=30)
    Refrence = models.CharField(max_length=10)
    User_Id = models.IntegerField()
    Password = models.CharField(max_length=10 )

    def __str__(self):

        return self.First_Name

class CommentModel(models.Model):

    home = models.ForeignKey(HomeModel,on_delete=models.CASCADE)
    Comments = models.TextField(max_length=100)
    Email = models.EmailField()
    Course_Opted = models.CharField(max_length=20)
    def __str__(self):

        return self.Email
# class Class_Detail_Course(models.Model):
#     Course_Name = models.CharField(max_length=20)
#     def __str__(self):
#
#         return self.Course_Name
#
#
# class Class_Detail_Date(models.Model):
#     courseName = models.ForeignKey(Class_Detail_Course,on_delete=models.CASCADE)
#     From_Date = models.DateField()
#     Batch_Time = models.TimeField()


class Note(models.Model):
    home = models.ForeignKey(HomeModel, on_delete= models.CASCADE)
    Note = models.CharField(max_length=300)
