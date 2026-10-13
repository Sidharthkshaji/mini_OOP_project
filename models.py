class StudentProfile:
    def __init__(self,student,skills = []):
        self.__student = student
        student_skills = {skill.lower().strip() for skill in skills}
        self.__skills = student_skills

    def get_name(self):
        return self.__student

    def get_skills(self):
        return self.__skills


class JobDescription:
    def __init__(self,title,req_skills = []):
        self.__title = title
        job_req_skills = {skill.lower().strip() for skill in req_skills}
        self.__req_skills = job_req_skills

    def get_title(self):
        return self.__title

    def get_req_skills(self):
        return self.__req_skills