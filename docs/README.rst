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

:Description: Blank 
:Location: https://rxnav.nlm.nih.gov/REST/approximateTerm?term=value&maxEntries=yyy
:Method: GET
:Return: application/xml

---------------------

:Decription: Blank
:Location: https://rxnav.nlm.nih.gov/REST/interaction/list?rxcuis=value
:Method: GET
:Return: application/xml

---------------------

:Decription: Patient 
:Location: /patient/?name=PatientName
:Method: GET
:template: patient-landing.html
:Return: text/html

---------------------

:Decription: Doctor 
:Location: /doctor/?name=doctorName
:Method: GET
:template: hospital-landing.html
:Return: text/html

---------------------

:Decription: Doctor 
:Location: /doctor/patient/?name=PatientName
:Method: GET
:template: hospital-patient.html
:Return: text/html



