class Patient:
    def __init__(self, patient_id, name, age, gender, contact):
        self.__patient_id = patient_id
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__contact = contact
        
    def get_patient_info(self):
        return {
            'patient id': self.__patient_id,
            'name': self.__name,
            'age': self.__age,
            'gender': self.__gender,
            'contact': self.__contact
        }
        
class doctor:
    def __init__(self, id, specialisation, name):
        self.__doctor_id = id
        self.__doctor_specialisation = specialisation  
        self.__name = name
        
    def get_doctor_info(self):
        return {
            'Doctor ID': self.__doctor_id,
            'Specialization': self.__doctor_specialisation,
            'name': self.__name,
        }
        
class MedicalRecord:
    def __init__(self):
        self.__records = {}

    def add_record(self, p, d, disease, medication):
        self.__records[p.get_patient_info()['patient id']] = {
            'Patient': p.get_patient_info(),
            'doctor': d.get_doctor_info(),
            'disease': disease,
            'medication': medication,
        }
        
    def get_record(self):
        return self.__records
        
patient1 = Patient(1, 'samay', '23', 'male', '+917983438390 \n')
patient2 = Patient(2, 'samay', '40', 'male', '+91789456123 ')

doctor1 = doctor(420, 'oncologist', 'shivam')
doctor2 = doctor(121,'paediatrician', 'harish')

record = MedicalRecord()
record.add_record(patient1, doctor1, 'chest pain', 'xanax')
record.add_record(patient2, doctor2, 'body pain', 'xanax')


print(record.get_record())
print(patient2.get_patient_info()['name'])
print(patient1.get_patient_info()['name'])


print()
print()

name = input("enter the name of the patient : ")
for i in record.get_record():
    if name == record.get_record()[i]['Patient']['name']:
        print(f" id of the requested patient is \n {record.get_record()[i]['Patient']}")
