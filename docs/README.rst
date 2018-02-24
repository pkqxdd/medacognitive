Resources to check:

https://docs.djangoproject.com/en/2.0/topics/db/models/
https://docs.djangoproject.com/en/2.0/topics/auth/default/#user-objects

How to Run Server
=================

#. ``cd`` into the folder
#. :code:`$ ./manage.py runserver`
#. Goto 127.0.0.1:8000


API Docs
========

:Description: Get RXCUI from Medicine Name
:Location: https://rxnav.nlm.nih.gov/REST/rxcui?name=value&search=1
:Method: GET
:Return: application/xml

---------------------

:Description: Get interactions between Medicines
:Location: https://rxnav.nlm.nih.gov/REST/interaction/list?rxcuis=value+value+...
:Method: GET
:Return: application/xml

---------------------

:Description: Patient profile from a patient's view 
:Location: /patient/?id=patientID
:Method: GET
:template: patient-landing.html
:Return: text/html

---------------------

:Decription: Doctor's view
:Location: /doctor/?id=docotrID
:Method: GET
:template: hospital-landing.html
:Return: text/html

---------------------

:Decription: Patient profile from a doctor's view 
:Location: /doctor/patient/?patientID=patientID&doctorID=doctorID
:Method: GET
:template: hospital-profile.html
:Return: text/html

----------------------

:Description: Update a medicine. Replace whatever is in the database with the incoming data
:Location: /update
:Method: POST
:Accept: 
  :Type: application/json
  :Fields:
    :med: the data to be replaced with, see the format below
:Response:
  :Type: text/plain
  :Content: success



Patient Object
==============

:attributes:
  :id: ID of the patient, start from 0
  :first_name: str
  :last_name: str
  :med: A list of Medicine object, see below
:methods: None

Doctor Object
=============

:attributes:
  :id: ID of the patient, start from 0
  :first_name: str
  :last_name: str
  :patients: A list of Patient object, see above
:methods: None

Medicine Object
===============

:attributes:
  :rxcui: int, ID of the medicine
  :patient_id: int, ID of the patient
  :name: str, Name of the medicine
  :num_left: int, Number of doses left
  :dosage: str, dosage
  :last_taken_time: Datetime object, last time a patient took a medicine
  :next_take_time: Datetime object, next time a patient take a medicine
  :taken: boolean, if the patient took the medicine at last_time_taken
 
:methods:
  :to_string:
    :input: None
    :returns: a string 
  :from_string: 
    :input: A single string in JSON format, contains everything in attributes
    :returns: a Medicine object
:Sample String: {"patient_id":"1", "rxcui":"1", "name":"temp", "num_left":"3", "last_taken_time":"2002-03-11 00:00:00", "next_take_time":"2002-03-11 00:00:00", "taken":"1", "dosage":"3"}




