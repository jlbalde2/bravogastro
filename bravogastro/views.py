from unicodedata import name
from django.shortcuts import render
from .models import Category, Product
from django.http import FileResponse


def all_products(request):
    products = Product.objects.all()
    return render(request, 'bravogastro/home.html', {'products': products})

def about_dr_bravo(request):
    return render(request, 'bravogastro/about.html')

def services(request):
    return render(request, "bravogastro/services.html")

def hospital_affiliations(request):
    return render(request, "bravogastro/hospitalAffiliations.html")

def patient_forms(request):
    return render(request, "bravogastro/patientForms.html")

def insurance(request):
    return render(request, "bravogastro/insurance.html")

def contact_us(request):
    return render(request, "bravogastro/contactUs.html")

def boardCertified_drBravo(request):
    return render(request, "boardCertified/drBravo.html")

def staff_lettyRios(request):
    return render(request, "staff/lettyRios.html")

def staff_edgarOlivares(request):
    return render(request, "staff/edgarOlivares.html")

def staff_litzyGonzalez(request):
    return render(request, "staff/litzyGonzalez.html")

def staff_nellyEsparza(request):
    return render(request, "staff/nellyEsparza.html")

def staff_stephanieBenitez(request):
    return render(request, "staff/stephanieBenitez.html")

def services_bravopHMonitoring(request):
    return render(request, "services/bravopHMonitoring.html")

def services_colonoscopy(request):
    return render(request, "services/colonoscopy.html")

def services_upperEndoscopy(request):
    return render(request, "services/upperEndoscopy.html")

def services_ercp(request):
    return render(request, "services/ercp.html")

def services_pillCam(request):
    return render(request, "services/pillCam.html")

def areas_of_expertise(request):
    return render(request, "bravogastro/areasOfExpertise.html")

def patient_information_update(request):
    return FileResponse(open("templates/patientForms/Patient-Information-Update.pdf", 'rb'), content_type='application/pdf')

def patient_registration_Form(request):
    return FileResponse(open("templates/patientForms/Patient-Registration-Form.pdf", 'rb'), content_type='application/pdf')

def hippa(request):
    return FileResponse(open("templates/patientForms/HIPPA.pdf", 'rb'), content_type='application/pdf')

def registro_de_pacientes(request):
    return FileResponse(open("templates/patientForms/Registro-de-Pacientes.pdf", 'rb'), content_type='application/pdf')

def aviso_del_paciente(request):
    return FileResponse(open("templates/patientForms/Aviso-del-paciente-sobre-las-prácticas-de-privacidad.pdf", 'rb'), content_type='application/pdf')

# Areas of Expertise
def abdominal_pain(request):
    return render(request, "areasOfExpertise/abdominalPainSyndrome.html")

def acid_reflux(request):
    return render(request, "areasOfExpertise/acidReflux.html")

def celiac_disease(request):
    return render(request, "areasOfExpertise/celiacDisease.html")

def colon_polyps(request):
    return render(request, "areasOfExpertise/colonPolyps.html")

def colorectal_cancer(request):
    return render(request, "areasOfExpertise/colorectalCancer.html")

def crohns_disease(request):
    return render(request, "areasOfExpertise/crohnsDisease.html")

def diarrheal_diseases(request):
    return render(request, "areasOfExpertise/diarrhealDiseases.html")

def diverticulosis_diverticulitis(request):
    return render(request, "areasOfExpertise/diverticulosisDiverticulitis.html") 

def gallstones(request):
    return render(request, "areasOfExpertise/gallstones.html")

def inflammatory_bowel(request):
    return render(request, "areasOfExpertise/inflammatoryBowelDisease.html")

def pancreatic_cancer(request):
    return render(request, "areasOfExpertise/pancreaticCancer.html")

def pancreatitis(request):
    return render(request, "areasOfExpertise/pancreatitis.html")  