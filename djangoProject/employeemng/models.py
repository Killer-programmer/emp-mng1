from django.db import models


class EmpCategory(models.Model):
    category = models.CharField(max_length=20)
    def __str__(self):
        return self.category

class EmployeeAdd(models.Model):
    emp_name = models.CharField(max_length=50)
    emp_num = models.IntegerField(max_length=15)
    emp_category = models.ForeignKey(EmpCategory, on_delete=models.CASCADE)
    emp_rate = models.IntegerField(max_length=4, default=0)

    def __str__(self):
        return self.emp_name
