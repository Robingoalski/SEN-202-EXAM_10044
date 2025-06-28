from django.db import models

class StaffBase(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_joined = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

class Manager(StaffBase):
    department = models.CharField(max_length=100)
   
 has_company_card = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} (Manager)"

class Intern(StaffBase):
    mentor = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name='interns')
    internship_end = models.DateField()

    def __str__(self):
        return f"{self.name} (Intern)"