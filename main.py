from models import StudentProfile, JobDescription
from manager import Manager


student = StudentProfile("Aarav",["Python","SQL","Java","HTML","CSS"])

job1 = JobDescription("Junior Developer",["Python","Flask","SQL","Devops"])

job2 = JobDescription("Frontend Developer",["HTML","CSS","React","Django","JavaScript"])

manager1 = Manager(student,job1).run_analysis()
manager2 = Manager(student,job2).run_analysis()