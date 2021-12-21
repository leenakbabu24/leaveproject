from django.contrib import admin
from. models import Login,Register,Task,Taskassign,Payroll,Salary,Leaveapply,Leaveapprove,Leavereject,Leavedetails
# Register your models here.
admin.site.register(Login)
admin.site.register(Register)
admin.site.register(Task)
admin.site.register(Taskassign)
admin.site.register(Payroll)
admin.site.register(Salary)
admin.site.register(Leaveapply)
admin.site.register(Leaveapprove)
admin.site.register(Leavereject)
admin.site.register(Leavedetails)