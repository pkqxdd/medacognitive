"""medacognitive URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import home, hospital,patient_profile,doctor_patient,doctor_profile
from django.conf.urls.static import static
from .settings import DEBUG,BASE_DIR
import os


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hospital/', hospital),
    path('patient/',patient_profile),
    path('doctor/patient/',doctor_patient),
    path('doctor/',doctor_profile),
    path('',home)
] \
              + static('css/',document_root=os.path.join(BASE_DIR,'css')) \
              + static('fonts/',document_root=os.path.join(BASE_DIR,'fonts')) \
              + static('js/',document_root=os.path.join(BASE_DIR,'js'))\
              + static('img/',document_root=os.path.join(BASE_DIR,'img'))



