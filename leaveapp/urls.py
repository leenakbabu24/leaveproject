from django.urls import path
from django.conf import urls
from. import views


urlpatterns = [
    path('',views.home, name='login.html'),
    path('login',views.login,name='login.html'),
    path('emp',views.emp,name='aelog.html'),
    path('along',views.ad,name='aelog.html'),
    path('employee',views.employee,name='aelog.html'),
    path('task',views.task,name='task.html'),
    path('taskassign',views.taskassign,name='taskassign.html'),
    path('pay',views.pay,name='payroll.html'),
    path('sal',views.sal,name='salary.html'),
    path('empleave',views.empleave,name='leaveapply.html'),
    path('leavedetails',views.leavedetails,name='leavedetails'),
    path('leaveedit/<int:i>/',views.leaveedit,name='leaveedit'),
    path('leaveedit1/<int:i>/',views.leaveedit1,name='leaveedit1'),
    path('leaveapprove/<int:i>/',views.leaveapprove,name='leaveapprove'),
    path('leavereject/<int:i>/',views.leavereject,name='leavereject'),
    path('leavestatus',views.leavestatus,name='leavestatus'),
]