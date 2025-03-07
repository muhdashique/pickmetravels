from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Vehicle, VehicleImage, Package
from .forms import VehicleForm, VehicleImageForm

def index(request):
    vehicles = Vehicle.objects.prefetch_related("images").all()
    packages = Package.objects.all()
    testimonials = Testimonial.objects.all()
    return render(request, "index.html", {"vehicles": vehicles,'packages': packages,'testimonials': testimonials})

def adminpannel(request):
    return render(request, 'adminpannel.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('add_vehicle')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('/')


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Vehicle, VehicleImage
from .forms import VehicleForm, VehicleImageForm

def add_vehicle(request):
    if request.method == "POST":
        vehicle_form = VehicleForm(request.POST)
        image_form = VehicleImageForm(request.POST, request.FILES)

        if vehicle_form.is_valid() and image_form.is_valid():
            vehicle = vehicle_form.save()

            # Handle multiple image uploads
            images = request.FILES.getlist('images')  # Get all uploaded images
            for img in images:
                VehicleImage.objects.create(vehicle=vehicle, image=img)

            messages.success(request, 'Vehicle added successfully!')
            return redirect('add_vehicle')  # Redirect back to form

        else:
            messages.error(request, 'There was an error with your form submission.')

    else:
        vehicle_form = VehicleForm()
        image_form = VehicleImageForm()

    vehicles = Vehicle.objects.all()  # Fetch all vehicles for display

    return render(request, "add_vehicle.html", {
        'vehicle_form': vehicle_form,
        'image_form': image_form,
        'vehicles': vehicles  # Pass vehicles to template
    })




def edit_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)

    if request.method == "POST":
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vehicle updated successfully!')
            return redirect('add_vehicle')

    else:
        form = VehicleForm(instance=vehicle)

    return render(request, "edit_vehicle.html", {'form': form, 'vehicle': vehicle})




from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Vehicle  # Make sure to import the correct model

def delete_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    vehicle.delete()
    messages.success(request, 'Vehicle deleted successfully!')
    return redirect('add_vehicle')

from django.shortcuts import get_object_or_404, redirect
from .models import VehicleImage

def delete_vehicle_image(request, image_id):
    image = get_object_or_404(VehicleImage, id=image_id)
    image.delete()
    return redirect(request.META.get('HTTP_REFERER', 'add_vehicle'))




from django.shortcuts import render, redirect
from .models import Package
from .forms import PackageForm

def add_package(request):
    if request.method == "POST":
        form = PackageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_package')  # Stay on the same page after adding
    else:
        form = PackageForm()

    packages = Package.objects.all()  # Fetch all packages

    return render(request, 'add_package.html', {'form': form, 'packages': packages})






def edit_package(request, package_id):
    package = get_object_or_404(Package, id=package_id)
    if request.method == "POST":
        form = PackageForm(request.POST, request.FILES, instance=package)
        if form.is_valid():
            form.save()
            return redirect('add_package')  # Redirect back to package list
    else:
        form = PackageForm(instance=package)

    return render(request, 'edit_package.html', {'form': form, 'package': package})






def delete_package(request, package_id):
    package = get_object_or_404(Package, id=package_id)
    package.delete()
    return redirect('add_package')  # Redirect back to package list after deleting







from django.shortcuts import render, redirect
from .models import Testimonial
from .forms import TestimonialForm

def add_testimonial(request):
    testimonials = Testimonial.objects.all()  # Fetch all testimonials to display
    if request.method == "POST":
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_testimonial')  # Stay on the same page after submission
    else:
        form = TestimonialForm()
    
    return render(request, 'add_testimonial.html', {'form': form, 'testimonials': testimonials})





def edit_testimonial(request, testimonial_id):
    testimonial = get_object_or_404(Testimonial, id=testimonial_id)
    if request.method == "POST":
        form = TestimonialForm(request.POST, request.FILES, instance=testimonial)
        if form.is_valid():
            form.save()
            return redirect('add_testimonial')  # Redirect to testimonial page
    else:
        form = TestimonialForm(instance=testimonial)
    
    return render(request, 'edit_testimonial.html', {'form': form, 'testimonial': testimonial})

def delete_testimonial(request, testimonial_id):
    testimonial = get_object_or_404(Testimonial, id=testimonial_id)
    testimonial.delete()
    return redirect('add_testimonial')






from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages

def send_email(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]

        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            send_mail(
                subject,
                full_message,
                email,  # Sender's email (user's email)
                ["Picmetravels@gmail.com"],  # Replace with your email to receive messages
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully!")
        except Exception as e:
            messages.error(request, f"Error sending email: {e}")

        return redirect("/")  # Redirect back to the contact page

    return render(request, "index.html")



from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.views.decorators.cache import never_cache

@never_cache
def logout_view(request):
    logout(request)
    response = redirect('login')  # Redirect to login after logout
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response
