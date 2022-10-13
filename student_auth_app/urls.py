from . import views
from django.urls import path,include



urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('add_staff/',views.add_staff,name='add_staff'),
    path('admin_home/',views.admin_home,name="admin_home"),
    path('staff_home/',views.staff_home,name="staff_home"),
    path('user_login/',views.user_login,name="user_login"),
    path('course_load/',views.course_load,name="course_load"),
    path('add_course/',views.add_course,name="add_course"),
    path('add_stud/',views.add_stud,name="add_stud"),
    path('add_student/',views.add_student,name="add_student"),
    path('ad_show_students/',views.ad_show_students,name="ad_show_students"),
    path('st_show_students/',views.st_show_students,name="st_show_students"),
    path('edit_page/<int:pk>',views.edit_page,name='edit_page'),
    path('edit_stud/<int:pk>',views.edit_stud,name='edit_stud'),
    path('delete1/<int:pk>',views.delete1,name='delete1'),
    path('delete_staff/<int:pk>',views.delete_staff,name='delete_staff'),
    path('view_staff/',views.view_staff,name="view_staff"),
    path('view_profile/',views.view_profile,name="view_profile"),
    path('edit_staff/',views.edit_staff,name='edit_staff'),
    path('edit_profile/<int:pk>',views.edit_profile,name='edit_profile'),
    path('logout/',views.logout,name="logout")
]
