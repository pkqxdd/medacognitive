from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from datetime import datetime
from doctors.models import Doctor
from patients.models import Patient
from django.views import View

class IterRegistry(type):
    def __iter__(cls):
        return iter(cls._registry)

class Med(object):
    __metaclass__ = IterRegistry
    _registry = []

    def __init__(self,patient_id:int,rxcui, name:str, num_left:int, dosage:int, last_taken_time:datetime, next_take_time:datetime, taken:bool):
        self.rxcui=rxcui
        self._registry.append(self)
        self.name = name+str(patient_id)
        self.num_left = num_left
        self.dosage = dosage
        self.last_taken_time = last_taken_time
        self.next_take_time = next_take_time
        self.taken = taken

    @classmethod
    def from_string(cls,s):
        for i in Med._registry:
            if i.name == s:
                return i

    def to_string(self):
        return self.name



def home(request):
    return HttpResponseRedirect('/hospital')


def hospital(request):
    return render(request,'hospital-landing.html')

def patient_profile(request):
    try:
        try:
            patient_id=int(request.GET['id'])
            patient=Patient.objects.get(id=patient_id)
        except Patient.DoesNotExist:
            return Http404("Patient record with ID %d does not exist"%patient_id)
    except:
        return Http404("Improperly formatted request")
    
    return render(request,'patient-profile.html',context={patient:patient})
