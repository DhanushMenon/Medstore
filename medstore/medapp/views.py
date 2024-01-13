from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # Create UserProfile associated with the user
        user_profile = Profile(user=user, phone_number=phone)
        user_profile.save()

        return redirect('login_user')  # Redirect to your login view
    else:
        return render(request, 'register.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request,user)
            if user.username == "admin1":
                return redirect('admin_dashboard')
            else:
                return redirect('index')  # Redirect to your home page or any desired view
        else:
            messages.error(request, 'Invalid username or password. Please try again.')

    return render(request, 'login.html')



def logout_user(request):
    logout(request)
    return redirect('index') 


def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def admin_view(request):
    medicine = Medicine.objects.all()
    return render(request, 'admin_view.html',{'medicine':medicine})


# views.py
from django.shortcuts import render, redirect
from .models import Medicine

def upload_medicine(request):
    if request.method == 'POST':
        medicine_name = request.POST.get('medicineName')
        company_name = request.POST.get('companyName')
        image = request.FILES.get('medicineImage')
        expire_date = request.POST.get('expireDate')
        print(image)

        new_medicine = Medicine(
            medicine_name=medicine_name,
            company_name=company_name,
            image=image,
            expire_date=expire_date
        )
        new_medicine.save()

        return redirect('admin_dashboard')  # Redirect to the admin view page after uploading

    return render(request, 'admin_dashboard.html')
  # Redirect to the admin view page after uploading

    return render(request, 'admin_dashboard.html')


from django.shortcuts import render, get_object_or_404, redirect
from .models import Medicine


from django.shortcuts import render, get_object_or_404, redirect
from .models import Medicine

def update_medicine(request, medicine_id):
    medicine = get_object_or_404(Medicine, id=medicine_id)

    if request.method == 'POST':
        # Retrieve data from the form
        medicine_name = request.POST.get('medicineName')
        company_name = request.POST.get('companyName')
        expire_date = request.POST.get('expireDate')
        image = request.FILES.get('medicineImage')

        # Update the medicine object with the new data
        medicine.medicine_name = medicine_name
        medicine.company_name = company_name
        medicine.expire_date = expire_date

        if image:
            medicine.image = image

        # Save the updated medicine object
        medicine.save()

        # Redirect to the admin view page or any other page you prefer
        return redirect('admin_view')
    else:
        # Render the update form with the medicine details
        return render(request, 'update_medicine.html', {'medicine': medicine})

from django.shortcuts import get_object_or_404, redirect
from .models import Medicine

def delete_medicine(request, medicine_id):
    medicine = get_object_or_404(Medicine, id=medicine_id)
    medicine.delete()
    return redirect('admin_view')  # Redirect to the admin view page after deleting the medicine


def user(request):
    user = User.objects.all()
    return render(request,'user.html',{'user':user})

def details(request):
    medicine = Medicine.objects.all()
    return render(request,'details.html',{'medicine':medicine})





