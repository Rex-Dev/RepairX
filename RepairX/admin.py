from django.contrib import admin
from .models import User,Employee,Service,Repair,Spares,Vehicle,UserVehicle,Appoinments

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['userid','username','userphone','userlocation','userage']
    
    
    
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['empid','empname','emprofession','empskill','empassword']
    
    
    
@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display=['vehid','vehtype','vehbrand','vehmodel','vehfuel']
    
   
    
@admin.register(UserVehicle)
class UserVehicle(admin.ModelAdmin):
    list_display=['vehid','userid','vehreg','vehtype','vehbrand','vehmodel','vehfuel']
    
    
@admin.register(Repair)
class RepairAdmin(admin.ModelAdmin):
    list_display=['repairid','repairdesc','vehtype','repaircost']
    
    
    
@admin.register(Spares)
class SparesAdmin(admin.ModelAdmin):
    list_display=['spareid','vehtype','vehbrand','vehmodel','vehfuel','sparestock','spareprice']
    
    
    
@admin.register(Appoinments)
class AppoinmentsAdmin(admin.ModelAdmin):
    list_display=['appoinmentid','userid','vehid','date']
    
    
    
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display=['serviceid','vehid','empid','appoinmentid','repairids','partids','status','entrydate','deliverydate']
    
    