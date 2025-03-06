from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('adminpannel/',views.adminpannel,name='adminpannel'),
     path('add-vehicle/', views.add_vehicle, name='add_vehicle'),
     path('edit-vehicle/<int:vehicle_id>/', views.edit_vehicle, name='edit_vehicle'),
   path('delete-vehicle/<int:vehicle_id>/', views.delete_vehicle, name='delete_vehicle'),
     path('delete-vehicle-image/<int:image_id>/', views.delete_vehicle_image, name='delete_vehicle_image'),
   path('add-package/', views.add_package, name='add_package'),
    path('edit-package/<int:package_id>/', views.edit_package, name='edit_package'),
    path('delete-package/<int:package_id>/', views.delete_package, name='delete_package'),
     path('add-testimonial/', views.add_testimonial, name='add_testimonial'),
      path('edit-testimonial/<int:testimonial_id>/', views.edit_testimonial, name='edit_testimonial'),
    path('delete-testimonial/<int:testimonial_id>/', views.delete_testimonial, name='delete_testimonial'),
    path("send-email/", views.send_email, name="send_email"),
    path('logout/', views.user_logout, name='user_logout'),
]