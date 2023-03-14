 
from django.contrib import admin
from django.urls import path,include
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.add_show,name='addandShow'),
    path('delete/<int:id>',views.delete_data,name="deleteData"),
    path('update/<int:id>',views.update_data,name="updateData"),
    path('api/', include('enroll.api.urls')),

]