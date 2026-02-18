import sys
import fitz  # PyMuPDF library
import os
import random
import re








in_service_template_directory = os.getcwd() + "\\In_Service_Template\\"







#filling_date = input("Please input date: ")
#Aide_Name = input("Please input Aide's name: ")
filling_date = (sys.argv[1]).strip()
Aide_Name = (sys.argv[2]).strip()
aide_language = ""
temp_year = filling_date.split("/")
filling_year = temp_year[-1]
in_service_directory = ""


def aide_language_judge():

    global in_service_directory
    global aide_language

    #aide_language = input("Please input aide's language (Chinese/English): ")
    aide_language = (sys.argv[3]).strip()

    if aide_language == "Chinese":

        in_service_directory = in_service_template_directory + "in_service_Chinese"

    elif aide_language == "English":

        in_service_directory = in_service_template_directory + "in_service_English"

    else:

        print("Language is wrong, please input language again!")
        #aide_language_judge()
        quit()








def create_patient_folder():

    patient_folder_path = os.getcwd() + "\\Outcome\\" + Aide_Name
    os.makedirs(patient_folder_path, exist_ok = True)

def fill_out_advanced():

    advanced_directive_file = in_service_directory + "\\Advanced Directive.pdf"

    if aide_language == "Chinese":

        doc = fitz.open(advanced_directive_file)
        page_1 = doc.load_page(0)
        page_1.insert_text((160,130), Aide_Name, fontsize=16)
        page_1.insert_text((220, 340), filling_date, fontsize=16)
        page_1.insert_text((304, 274), filling_year, fontname="hebo", fontsize=14)

    else:

        doc = fitz.open(advanced_directive_file)
        page_1 = doc.load_page(0)
        page_1.insert_text((160, 135), Aide_Name, fontsize=16)
        page_1.insert_text((215, 322), filling_date, fontsize=16)
        page_1.insert_text((290, 283), filling_year, fontname="hebo", fontsize=14)




    outcome_directory = os.getcwd() + "\\Outcome\\" + Aide_Name + "\\Advanced Directive.pdf"
    doc.save(outcome_directory)
    doc.close()





def fill_out_caregiver():

    caregiver_file = in_service_directory + "\\Caregiver's Matters To Be Aware of.pdf"

    if aide_language == "Chinese":

        doc = fitz.open(caregiver_file)
        page_1 = doc.load_page(0)
        page_1.insert_text((160, 135), Aide_Name, fontsize=16)
        page_1.insert_text((200, 364), filling_date, fontsize=16)
        page_1.insert_text((445, 281), filling_year, fontname="hebo", fontsize=14)

    else:

        doc = fitz.open(caregiver_file)
        page_1 = doc.load_page(0)
        page_1.insert_text((160, 135), Aide_Name, fontsize=16)
        page_1.insert_text((210, 320), filling_date, fontsize=16)
        page_1.insert_text((430, 281), filling_year, fontname="hebo", fontsize=14)




    outcome_directory = os.getcwd() + "\\Outcome\\" + Aide_Name + "\\Caregiver's Matters To Be Aware of.pdf"
    doc.save(outcome_directory)
    doc.close()





def fill_out_covid():

    covid_file = in_service_directory + "\\COVID-19.pdf"

    if aide_language == "Chinese":

        doc = fitz.open(covid_file)
        page_1 = doc.load_page(0)
        page_1.insert_text((160, 140), Aide_Name, fontsize=16)
        page_1.insert_text((230, 340), filling_date, fontsize=16)
        page_1.insert_text((278, 277), filling_year, fontname="hebo", fontsize=14)

    else:

        doc = fitz.open(covid_file)
        page_1 = doc.load_page(0)
        page_1.insert_text((160, 140), Aide_Name, fontsize=16)
        page_1.insert_text((230, 325), filling_date, fontsize=16)
        page_1.insert_text((265, 285), filling_year, fontname="hebo", fontsize=14)






    outcome_directory = os.getcwd() + "\\Outcome\\" + Aide_Name + "\\COVID-19.pdf"
    doc.save(outcome_directory)
    doc.close()






def fill_out_electronic_visit():

    electronic_file = in_service_directory + "\\Electronic Visit Verification.pdf"

    if aide_language == "Chinese":

        doc = fitz.open(electronic_file)
        page_1 = doc.load_page(0)
        page_1.insert_text((160, 140), Aide_Name, fontsize=16)
        page_1.insert_text((220, 345), filling_date, fontsize=16)
        page_1.insert_text((377, 273), filling_year, fontname="hebo", fontsize=14)

    else:

        doc = fitz.open(electronic_file)
        page_1 = doc.load_page(0)
        page_1.insert_text((160, 140), Aide_Name, fontsize=16)
        page_1.insert_text((220, 350), filling_date, fontsize=16)
        page_1.insert_text((355, 271), filling_year, fontname="hebo", fontsize=14)

    outcome_directory = os.getcwd() + "\\Outcome\\" + Aide_Name + "\\Electronic Visit Verification.pdf"
    doc.save(outcome_directory)
    doc.close()





def fill_out_emergency():

    emergency_file = in_service_directory + "\\Emergency Response.pdf"

    if aide_language == "Chinese":

        doc = fitz.open(emergency_file)
        page_1 = doc.load_page(0)
        page_1.insert_text((160, 140), Aide_Name, fontsize=16)
        page_1.insert_text((230, 370), filling_date, fontsize=16)
        page_1.insert_text((333, 270), filling_year, fontname="hebo", fontsize=14)

    else:

        doc = fitz.open(emergency_file)
        page_1 = doc.load_page(0)
        page_1.insert_text((160, 140), Aide_Name, fontsize=16)
        page_1.insert_text((220, 350), filling_date, fontsize=16)
        page_1.insert_text((308, 270), filling_year, fontname="hebo", fontsize=14)

    outcome_directory = os.getcwd() + "\\Outcome\\" + Aide_Name + "\\Emergency Response.pdf"
    doc.save(outcome_directory)
    doc.close()




def fill_out_handwash():

    handwash_file = in_service_directory + "\\Handwash Teching info from CDC.pdf"

    if aide_language == "Chinese":

        doc = fitz.open(handwash_file)
        page_1 = doc.load_page(0)
        page_1.insert_text((160, 140), Aide_Name, fontsize=16)
        page_1.insert_text((435, 273), filling_year, fontname="hebo", fontsize=14)
        page_1.insert_text((210, 360), filling_date, fontsize=16)

    else:

        doc = fitz.open(handwash_file)
        page_1 = doc.load_page(0)
        page_1.insert_text((160, 140), Aide_Name, fontsize=16)
        page_1.insert_text((450, 273), filling_year, fontname="hebo", fontsize=14)
        page_1.insert_text((230, 325), filling_date, fontsize=16)

    outcome_directory = os.getcwd() + "\\Outcome\\" + Aide_Name + "\\Handwash Teching info from CDC.pdf"
    doc.save(outcome_directory)
    doc.close()





def fill_out_hipaa():

    hipaa_file = in_service_directory + "\\HIPAA.pdf"

    if aide_language == "Chinese":

        doc = fitz.open(hipaa_file)
        page_1 = doc.load_page(0)
        page_1.insert_text((160, 140), Aide_Name, fontsize=16)
        page_1.insert_text((267, 277), filling_year, fontname="hebo", fontsize=14)
        page_1.insert_text((230, 350), filling_date, fontsize=16)

    else:

        doc = fitz.open(hipaa_file)
        page_1 = doc.load_page(0)
        page_1.insert_text((160, 140), Aide_Name, fontsize=16)
        page_1.insert_text((230, 277), filling_year, fontname="hebo", fontsize=14)
        page_1.insert_text((230, 320), filling_date, fontsize=16)

    outcome_directory = os.getcwd() + "\\Outcome\\" + Aide_Name + "\\HIPAA.pdf"
    doc.save(outcome_directory)
    doc.close()



def fill_out_hiv():

    hiv_file = in_service_directory + "\\HIV Confidentriality.pdf"

    if aide_language == "Chinese":

        doc = fitz.open(hiv_file)
        page_1 = doc.load_page(0)
        page_1.insert_text((160, 140), Aide_Name, fontsize=16)
        page_1.insert_text((304, 277), filling_year, fontname="hebo", fontsize=14)
        page_1.insert_text((230, 360), filling_date, fontsize=16)

    else:

        doc = fitz.open(hiv_file)
        page_1 = doc.load_page(0)
        page_1.insert_text((160, 140), Aide_Name, fontsize=16)
        page_1.insert_text((295, 278), filling_year, fontname="hebo", fontsize=14)
        page_1.insert_text((230, 320), filling_date, fontsize=16)

    outcome_directory = os.getcwd() + "\\Outcome\\" + Aide_Name + "\\HIV Confidentriality.pdf"
    doc.save(outcome_directory)
    doc.close()






def fill_out_osha():

    osha_file = in_service_directory + "\\OSHA.pdf"

    if aide_language == "Chinese":

        doc = fitz.open(osha_file)
        page_1 = doc.load_page(0)
        page_1.insert_text((160, 140), Aide_Name, fontsize=16)
        page_1.insert_text((213, 278), filling_year, fontname="hebo", fontsize=14)
        page_1.insert_text((230, 350), filling_date, fontsize=16)


    else:

        doc = fitz.open(osha_file)
        page_1 = doc.load_page(0)
        page_1.insert_text((160, 140), Aide_Name, fontsize=16)
        page_1.insert_text((207, 276), filling_year, fontname="hebo", fontsize=14)
        page_1.insert_text((230, 320), filling_date, fontsize=16)

    outcome_directory = os.getcwd() + "\\Outcome\\" + Aide_Name + "\\OSHA.pdf"
    doc.save(outcome_directory)
    doc.close()




def fill_out_patient():

    patient_file = in_service_directory + "\\Patient Rights.pdf"

    if aide_language == "Chinese":

        doc = fitz.open(patient_file)
        page_1 = doc.load_page(0)
        page_1.insert_text((160, 140), Aide_Name, fontsize=16)
        page_1.insert_text((270, 275), filling_year, fontname="hebo", fontsize=14)
        page_1.insert_text((230, 370), filling_date, fontsize=16)

    else:

        doc = fitz.open(patient_file)
        page_1 = doc.load_page(0)
        page_1.insert_text((160, 140), Aide_Name, fontsize=16)
        page_1.insert_text((250, 273), filling_year, fontname="hebo", fontsize=14)
        page_1.insert_text((230, 350), filling_date, fontsize=16)

    outcome_directory = os.getcwd() + "\\Outcome\\" + Aide_Name + "\\Patient Rights.pdf"
    doc.save(outcome_directory)
    doc.close()




def fill_out_stop_sex():

    stop_sex_file = in_service_directory + "\\Stop Sexual Harassment.pdf"

    if aide_language == "Chinese":

        doc = fitz.open(stop_sex_file)
        page_1 = doc.load_page(0)
        page_1.insert_text((160, 140), Aide_Name, fontsize=16)
        page_1.insert_text((350, 272), filling_year, fontname="hebo", fontsize=14)
        page_1.insert_text((250, 350), filling_date, fontsize=16)

    else:

        doc = fitz.open(stop_sex_file)
        page_1 = doc.load_page(0)
        page_1.insert_text((160, 140), Aide_Name, fontsize=16)
        page_1.insert_text((328, 272), filling_year, fontname="hebo", fontsize=14)
        page_1.insert_text((230, 320), filling_date, fontsize=16)

    outcome_directory = os.getcwd() + "\\Outcome\\" + Aide_Name + "\\Stop Sexual Harassment.pdf"
    doc.save(outcome_directory)
    doc.close()




def fill_out_toberculosis():

    toberculosis_file = in_service_directory + "\\Toberculosis Risk Assessment.pdf"

    if aide_language == "Chinese":

        doc = fitz.open(toberculosis_file)
        page_1 = doc.load_page(0)
        page_1.insert_text((160, 140), Aide_Name, fontsize=16)
        page_1.insert_text((368, 273), filling_year, fontname="hebo", fontsize=14)
        page_1.insert_text((235, 350), filling_date, fontsize=16)

    else:

        doc = fitz.open(toberculosis_file)
        page_1 = doc.load_page(0)
        page_1.insert_text((160, 140), Aide_Name, fontsize=16)
        page_1.insert_text((390, 273), filling_year, fontname="hebo", fontsize=14)
        page_1.insert_text((220, 320), filling_date, fontsize=16)

    outcome_directory = os.getcwd() + "\\Outcome\\" + Aide_Name + "\\Toberculosis Risk Assessment.pdf"
    doc.save(outcome_directory)
    doc.close()






def fill_out_unicersal():

    unicersal_file = in_service_directory + "\\Unicersal precaution.pdf"

    if aide_language == "Chinese":

        doc = fitz.open(unicersal_file)
        page_1 = doc.load_page(0)
        page_1.insert_text((160, 140), Aide_Name, fontsize=16)
        page_1.insert_text((330, 273), filling_year, fontname="hebo", fontsize=14)
        page_1.insert_text((235, 370), filling_date, fontsize=16)

    else:

        doc = fitz.open(unicersal_file)
        page_1 = doc.load_page(0)
        page_1.insert_text((160, 140), Aide_Name, fontsize=16)
        page_1.insert_text((310, 272), filling_year, fontname="hebo", fontsize=14)
        page_1.insert_text((235, 320), filling_date, fontsize=16)

    outcome_directory = os.getcwd() + "\\Outcome\\" + Aide_Name + "\\Unicersal precaution.pdf"
    doc.save(outcome_directory)
    doc.close()







aide_language_judge()
create_patient_folder()
fill_out_advanced()
fill_out_caregiver()
fill_out_covid()
fill_out_electronic_visit()
fill_out_emergency()
fill_out_handwash()
fill_out_hipaa()
fill_out_hiv()
fill_out_osha()
fill_out_patient()
fill_out_stop_sex()
fill_out_toberculosis()
fill_out_unicersal()
print(Aide_Name, "  ", filling_date)

