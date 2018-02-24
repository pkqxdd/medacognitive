from django.db import models
import json,datetime



class Med:
    def __init__(self, med_no: int, patient_id: int, rxcui: str, name: str, num_left: int, dosage: str,
                 last_taken_time: datetime,
                 next_take_time: datetime, taken: bool):
        self.med_no = med_no
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
        med_no = data['med_no']
        
        return Med(med_no, patient_id, rxcui, name, num_left, dosage, last_taken_time, next_take_time, taken)
    
    def to_string(self):
        return json.dumps({
            "med_no": self.med_no,
            "patient_id": self.patient_id,
            "rxcui": self.rxcui,
            "name": self.name,
            "num_left": self.num_left,
            "dosage": self.dosage,
            "last_taken_time": self.last_taken_time.isoformat() if isinstance(self.last_taken_time,
                                                                              datetime.datetime) else self.last_taken_time,
            "next_take_time": self.next_take_time.isoformat() if isinstance(self.next_take_time,
                                                                            datetime.datetime) else self.next_take_time,
            "taken": self.taken,
        })
    
    def __str__(self):
        return self.to_string()


class Meds:
    def __init__(self, *meds):
        self.meds = meds
    
    def to_string(self):
        return json.dumps([m.to_string() for m in self.meds])
    
    @classmethod
    def from_string(cls, s):
        return cls(*[Med.from_string(s) for s in json.loads(s)])


class Patient(models.Model):
    first_name=models.CharField("First Name",max_length=30)
    last_name=models.CharField("Last Name",max_length=30)
    med = models.TextField("Medicine")
    
    def parse_meds(self):
        return Meds.from_string(self.med)
    
    def update_med(self,meds:Meds):
        self.med=meds.to_string()

class Survey(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    med_name = models.TextField("Med name")
    med_comment = models.TextField("Comment")
