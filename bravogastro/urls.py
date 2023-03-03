from unicodedata import name
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.views.generic import TemplateView
from django.http import FileResponse

from . import views

app_name = 'bravogastro'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('about/', views.about_dr_bravo, name='about'),
    path('services/', views.services, name='services'),
    path('hospitalAffiliations/', views.hospital_affiliations, name='hospitalAffiliations'),
    path('patientForms/', views.patient_forms, name='patientForms'),
    path('insurance/', views.insurance, name='insurance'),
    path('contactUs/', views.contact_us, name='contactUs'),
    path('staff/lettyRios/', views.staff_lettyRios, name='lettyRios'),
    path('staff/edgarOlivares/', views.staff_edgarOlivares, name='edgarOlivares'),
    path('staff/litzyGonzalez', views.staff_litzyGonzalez, name='litzyGonzalez'),
    path('staff/stephanieBenitez', views.staff_stephanieBenitez, name='stephanieBenitez'),
    path('boardCertified/drBravo/', views.boardCertified_drBravo, name='drBravo'),
    path('services/colonoscopy/', views.services_colonoscopy, name="colonoscopy"),
    path('services/bravopHMonitoring/', views.services_bravopHMonitoring, name="bravopHMonitoring"),
    path('services/upperEndoscopy/', views.services_upperEndoscopy, name="upperEndoscopy"),
    path('services/ercp/', views.services_ercp, name="ercp"),
    path('services/pillCam/', views.services_pillCam, name="pillCam"),
    path('areasOfExpertise/', views.areas_of_expertise, name="areasOfExpertise"),
    path('patientForms/Patient-Registration-Form.pdf/', views.patient_registration_Form, name='patientRegistrationForm'),
    path('patientForms/Patient-Information-Update.pdf/', views.patient_information_update, name='patientRegistrationUpdate'),
    path('patientForms/HIPPA.pdf/', views.hippa, name='hippa'),
    path('patientForms/Registro-de-Pacientes.pdf/', views.registro_de_pacientes, name='registro_de_pacientes'),
    path('patientForms/Aviso-del-paciente-sobre-las-prácticas-de-privacidad.pdf/', views.aviso_del_paciente, name='aviso_del_paciente'),
    path('areasOfExpertise/abdominalPainSyndrome', views.abdominal_pain, name="abdominal_pain"),
    path('areasOfExpertise/acidReflux', views.acid_reflux, name="acid_reflux"),
    path('areasOfExpertise/celiacDisease', views.celiac_disease, name="celiac_disease"),  
    path('areasOfExpertise/colonPolyps', views.colon_polyps, name="colon_polyps"),
    path('areasOfExpertise/colorectalCancer', views.colorectal_cancer, name="colorectal_cancer"),
    path('areasOfExpertise/crohnsDisease', views.crohns_disease, name="crohns_disease"),   
    path('areasOfExpertise/diarrhealDiseases', views.diarrheal_diseases, name="diarrheal_diseases"),
    path('areasOfExpertise/diverticulosisDiverticulitis', views.diverticulosis_diverticulitis, name="diverticulosis_diverticulitis"),
    path('areasOfExpertise/gallstones', views.gallstones, name="gallstones"),  
    path('areasOfExpertise/inflammatoryBowelDisease', views.inflammatory_bowel, name="inflammatory_bowel"),
    path('areasOfExpertise/pancreaticCancer', views.pancreatic_cancer, name="pancreatic_cancer"),
    path('areasOfExpertise/pancreatitis', views.pancreatitis, name="pancreatitis"),   
]