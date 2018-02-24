from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from datetime import datetime
from doctors.models import Doctor
from patients.models import Patient
from django.views import View
import json

class Med(object):

    def __init__(self, patient_id: int, rxcui, name: str, num_left: int, dosage: int, last_taken_time: datetime,
                 next_take_time: datetime, taken: bool):
        self.patient_id = patient_id
        self.rxcui = rxcui
        self.name = name
        self.num_left = num_left
        self.dosage = dosage
        self.last_taken_time = last_taken_time
        self.next_take_time = next_take_time
        self.taken = taken


    # format = {patient_id:"patient_id", rxcui:"rxcui", name:"name",num_left:"num_left",dosage:"dosage", last_taken_time:"last_taken_time", next_take_time:"next_take_time", taken:"taken"]}
    @classmethod
    def from_string(cls, s):
        data = json.loads(s)
        patient_id = data['patient_id']
        rxcui = data['rxcui']
        name = data['name']
        num_left = data['num_left']
        dosage = data['dosage']
        last_taken_time = data['last_taken_time']
        next_take_time = data['next_take_time']
        taken = data['taken']

        tempMed = Med(patient_id, rxcui, name, num_left, dosage, last_taken_time, next_take_time, taken)
        return tempMed


    def to_string(self):
        return '{\"patient_id\":\"'+str(self.patient_id)+"\", \"rxcui\":\""+str(self.rxcui)+"\", \"name\":\""+self.name+"\", \"num_left\":\""+\
               str(self.num_left)+"\", \"last_taken_time\":\""+str(self.last_taken_time)+"\", \"next_take_time\":\""+str(self.next_take_time)+"\", \"taken\":\""+str(self.taken)+"\", \"dosage\":\""+str(self.dosage)+"\"}"



def home(request):
    return HttpResponseRedirect('/hospital')

def hospital(request):
    return render(request,'hospital-landing.html')

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
