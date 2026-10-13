from abc import ABC,abstractmethod

class SkillAnalyzer(ABC):

    @abstractmethod
    def analyze():
        pass

class MatchScoreCalculator(SkillAnalyzer):
    def analyze(student,job):
        matched_skills = job.get_req_skills().intersection(student.get_skills())
        try:

            match_percentage = (len(matched_skills) / len(job.get_req_skills())) * 100
            return matched_skills, int(match_percentage)
        except ZeroDivisionError:
           return 0

class MissingSkillDetector(SkillAnalyzer):
    def analyze(student,job):
        missing_skills = job.get_req_skills() - student.get_skills()
        return missing_skills
