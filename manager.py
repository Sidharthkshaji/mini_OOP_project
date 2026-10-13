from analyzers import MatchScoreCalculator, MissingSkillDetector

class Manager:
    def __init__(self,student,job):
        self.student = student
        self.job = job
        self.analyzer_object = [MatchScoreCalculator,MissingSkillDetector]
        self.result_list = []

    def run_analysis(self):
        for analyzer in self.analyzer_object:
            result = analyzer.analyze(self.student, self.job)
            self.result_list.append(result)

        Manager.print_output(self,self.student,self.job)


    def print_output(self,student,job):
        matched_skills = self.result_list[0][0]
        missing_skills = self.result_list[1]
        print("STUDENT - JOB SKILL ANALYSIS REPORT")
        print("Student Name:",student.get_name().title())
        print("Job Title:",job.get_title().title())
        print("Required Skills:",len(job.get_req_skills()))
        print("Matching Skills:")

        for skill in matched_skills:
            print(f" - {skill.title()}")

        print("Missing Skills:")

        for skill in missing_skills:
            print(f" - {skill.title()}")

        print(f"Match Score: {self.result_list[0][1]}%")
        print(f"Explanation:\nThe student matches {len(matched_skills)} out of {len(job.get_req_skills())} skills."
                f"Therefore, the skill match percentage is {self.result_list[0][1]}%\n")
        self.result_list = []