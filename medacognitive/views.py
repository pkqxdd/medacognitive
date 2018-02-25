from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from datetime import datetime
from doctors.models import Doctor
from patients.models import Patient,Med,Meds
from django.views import View



def home(request):
    return HttpResponseRedirect('/doctor/?id=1')


def doctor_profile(request):
    try:
        doctor_id = int(request.GET['id'])
        doctor = Doctor.objects.get(id=doctor_id)
    except Doctor.DoesNotExist:
        raise Http404("Doctor record with ID %d does not exist" % doctor_id)
    except Exception as msg:
        raise Http404("Improperly formatted request: %s" % msg)
    
    return render(request, 'hospital-landing.html', context={'doctor': doctor})

def doctor_patient(request):
    try:
        doctor_id = int(request.GET['id'])
        doctor = Doctor.objects.get(id=doctor_id)
    except Doctor.DoesNotExist:
        raise Http404("Doctor record with ID %d does not exist" % doctor_id)
    except Exception as msg:
        raise Http404("Improperly formatted request: %s" % msg)
    
    try:
        patient_id=int(request.GET['id'])
        patient=Patient.objects.get(id=patient_id)
    except Patient.DoesNotExist:
        raise Http404("Patient record with ID %d does not exist"%patient_id)
    except Exception as msg:
        raise Http404("Improperly formatted request: %s" % msg)

    return render(request,'hospital-profile.html',context={'doctor':doctor,'patient':patient})

def patient_profile(request):
    try:
        patient_id=int(request.GET['id'])
        patient=Patient.objects.get(id=patient_id)
    except Patient.DoesNotExist:
        raise Http404("Patient record with ID %d does not exist"%patient_id)
    except Exception as msg:
        raise Http404("Improperly formatted request: %s" % msg)
    
    return render(request,'patient-profile.html',context={'patient':patient})

def meds(request):
    try:
        patient_id=int(request.GET['id'])
        patient=Patient.objects.get(id=patient_id)
        m=patient.med
    except Patient.DoesNotExist:
        raise Http404("Patient record with ID %d does not exist"%patient_id)
    except Exception as msg:
        raise Http404("Improperly formatted request: %s" % msg)
    
    return HttpResponse(m,content_type='application/json')

def update(request):
    if request.method=='POST':
        try:
            patient_id=request.POST['id']
            m=Meds.from_string(request.POST["meds"]) #verify data
            patient=Patient.objects.get(id=patient_id)
            patient.med=m
            patient.save()
        except Exception as msg:
            raise Http404("Improperly formatted input: %s" % msg)
        return HttpResponse("Success")
    else:
        return HttpResponse("Please POST to this endpoint")

