import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','SantoshJobsWebPortal.settings')
import django
django.setup()

from jobapp.models import PuneJobs #,BangloreJobs,ChennaiJobs,MumbaiJobs
from faker import Faker
from random import *
fake=Faker()
def phoneindgen():
    d1= randint(6,9)
    num = str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements=('Project Manager', 'Team Leader', 'Project Head', 'Junior Software Engineer', 'Senior Software Engineer', 'DevOps Engineer', 'Associate Engineer'))
        feligibility = fake.random_element(elements=('B.Tech', 'M.Tech', 'BCA', 'MCA', 'BSC in Computer Science', 'Phd'))
        faddress = fake.address()
        fskills_required = fake.random_element(elements=('Django', 'Python(core and advanced)', 'MongoDb', 'Linux administrator', 'Java(core and advanced)', 'HTML CSS JAVASCRIPT'))
        fcity = fake.city()
        femail = fake.email()
        fexperience= fake.random_element(elements=(1,2,3,4,5,6,7,8,9,10,11,12))
        fphone_number=phoneindgen()
        punejobs_record =PuneJobs.objects.get_or_create(date=fdate, company_name=fcompany, title=ftitle, eligibility=feligibility, address=faddress, skills_required=fskills_required, city=fcity, email=femail, phone_number=fphone_number,experience=fexperience)

n = int(input("Enter the number of records to insert into the database: "))
populate(n)
print(f"{n} Records Inserted Successfully")
print('*'*30)
