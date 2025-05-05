from django.db import models

#user model
class User(models.Model):
    userid=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50)
    userphone=models.BigIntegerField(unique=True)
    useremail=models.EmailField()
    userlocation=models.CharField(max_length=50)
    userage=models.IntegerField(default=18)
    userpassword=models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.username} : {self.userpassword}"
    
#Employee model
class Employee(models.Model):
    TYPE=(
        ('Manager','Manager'),
        ('Mechanic','Mechanic'),
        ('Parts','Parts')
    )
    SKILLS=(
        ('Manager','Manager'),
        ('TwoWheeler','TwoWheeler'),
        ('Auto','Auto'),
        ('Car','Car'),
        ('Truck','Truck'),
        ('Bus','Bus')
    )

    empid=models.AutoField(primary_key=True)
    empname=models.CharField(max_length=50)
    emphone=models.BigIntegerField()
    emplocation=models.CharField(max_length=50)
    emprofession=models.CharField(choices=TYPE, max_length=50)
    empskill=models.CharField(choices=SKILLS,max_length=50)
    empassword=models.IntegerField(default=1234)
    
    def __str__(self):
        return f"{self.empid} : {self.emprofession} : {self.empskill}"
    
#Vehicle model
class Vehicle(models.Model):
    TYPE=(
        ('TwoWheeler','TwoWheeler'),
        ('Auto','Auto'),
        ('Car','Car'),
        ('Truck','Truck'),
        ('Bus','Bus')
    )
    FUEL=(
        ('Petrol','Petrol'),
        ('Diesel','Diesel'),
        ('CNG','CNG'),
        ('Electric','Electric')
    )
    
    vehid=models.AutoField(primary_key=True)
    vehtype=models.CharField(choices=TYPE,max_length=50)
    vehbrand=models.CharField(max_length=50)
    vehmodel=models.CharField(max_length=50)
    vehfuel=models.CharField(choices=FUEL,max_length=50)
    
    def __str__(self):
        return f"{self.vehbrand} : {self.vehmodel} : {self.vehfuel}"
    
#User Vehicle model
class UserVehicle(models.Model):
    vehid=models.AutoField(primary_key=True)
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    vehreg=models.CharField(max_length=12)
    vehtype=models.CharField(max_length=50)
    vehbrand=models.CharField(max_length=50)
    vehmodel=models.CharField(max_length=50)
    vehfuel=models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.vehid} : {self.userid} : {self.vehreg}"

#Repair model
class Repair(models.Model):
    TYPE=(
        ('TwoWheeler','TwoWheeler'),
        ('Auto','Auto'),
        ('Car','Car'),
        ('Truck','Truck'),
        ('Bus','Bus')
    )
    
    repairid=models.AutoField(primary_key=True)
    repairdesc=models.CharField(max_length=50)
    vehtype=models.CharField(choices=TYPE,max_length=50)
    repaircost=models.IntegerField()
    
    def __str__(self):
        return f"{self.repairdesc} : {self.vehtype} : {self.repaircost}"

#Spares model
class Spares(models.Model):
    spareid=models.CharField(max_length=50)
    vehtype=models.CharField(max_length=50)
    vehbrand=models.CharField(max_length=50)
    vehmodel=models.CharField(max_length=50)
    vehfuel=models.CharField(max_length=50)
    sparestock=models.IntegerField()
    spareprice=models.IntegerField()
    
    def __str__(self):
        return f"{self.spareid} : {self.vehmodel}"
    
#Appoinment model
class Appoinments(models.Model):
    appoinmentid=models.AutoField(primary_key=True)
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    vehid=models.ForeignKey(UserVehicle,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.appoinmentid
    
#Service model
class Service(models.Model):
    serviceid=models.AutoField(primary_key=True)
    vehid=models.ForeignKey(UserVehicle,on_delete=models.CASCADE)
    empid=models.ForeignKey(Employee,on_delete=models.CASCADE)
    appoinmentid=models.ForeignKey(Appoinments,on_delete=models.CASCADE)
    repairids=models.CharField(max_length=250)
    partids=models.CharField(max_length=250)
    status=models.CharField(max_length=20,default="inservice")
    entrydate=models.DateField(auto_now_add=True)
    deliverydate=models.CharField(max_length=20)
    
    def __str__(self):
        return self.serviceid