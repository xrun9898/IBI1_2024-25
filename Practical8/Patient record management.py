class Patient:
    def __init__ (self, name, age, latestAdmissionDate, medicalHistory):
        self.name = name
        self.age = age
        self.latestAdmissionDate = latestAdmissionDate
        self.medicalHistory = medicalHistory
    def printAll(self):
        print(f"Name: {self.name}, Age: {self.age}, Admission Date: {self.latestAdmissionDate}, Medical History: {self.medicalHistory}")

patientExample =Patient("sharei", "18", "4.1", "fever")
patientExample.printAll()
datas = input("input patient name; age; date of latest admission; and medical history").split()
name, age,latestAdmissionDate, medicalHistory = datas[0],datas[1],datas[2],datas[3]
patient = Patient(name, age, latestAdmissionDate, medicalHistory)  
patient.printAll()
    