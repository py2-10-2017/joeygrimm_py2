class Patient(object):
    id_number = 0
    def __init__(self, name, allergies,bed_number=0):
        Patient.id_number += 1
        self.id_number=Patient.id_number
        self.name=name
        self.allergies=allergies
        self.bed_number=bed_number

class Hospital(object):
    hosp_bed_number = 0
    patients = []
    patients.sort()
    hosp_patient = {}
    def __init__(self,name,capacity=5):
        self.name=name
        self.capacity=capacity
    def admit(self,Patient):
        if len(Hospital.patients) == self.capacity:
            print "{} can't be admitted. Hospital is a maximum capacity.".format(Patient.name)
            return self
        else:
            Hospital.hosp_bed_number+= 1
            Patient.bed_number=Hospital.hosp_bed_number
            Hospital.hosp_patient={
                "Patient Name": Patient.name,
                "Patient Bed#": Patient.bed_number,
                "Allergies": Patient.allergies
            }
            Hospital.patients.append(Hospital.hosp_patient)
            print "Patient added to bed # {}".format(Hospital.hosp_bed_number)
            return self
    def discharge(self):
        for i in Hospital.patients:
            print "Patient", i['Patient Name'], "Bed#" , i['Patient Bed#']
        print "Discharge the Patient by entering their bed number."
        Form_Bed_Num=input('Bed number: ')
        for i in Hospital.patients:
            if i['Patient Bed#'] == Form_Bed_Num:
                Hospital.patients.remove(i)
                i['Patient Bed#']=0
                print "Patient", i['Patient Name'], "discharged.\n", "Bed number now:", i['Patient Bed#']
                return self
            
        return self
                
    def display(self):
        for i in Hospital.patients:
            print "Patient", i['Patient Name'], "Bed#" , i['Patient Bed#']
        return self



frank=Patient("Frank Knees", "None")

dave=Patient("Dave Husky", "None")

ronald=Patient("Ronald McDonald", "Cats")

joe=Patient("Joe Grimm","Red Meat")

lea=Patient("Lea Collier","None")

krissy=Patient("Kristina Vance","None")

saintlukea=Hospital("Saint Lukes")

childrensmercy=Hospital("Children's Mercy Hospital")

childrensmercy.admit(dave).admit(ronald).admit(frank).admit(joe).admit(lea).display().admit(krissy).display().discharge().display()