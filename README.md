# 🎯 Student-Job Skill Match Analyzer

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Paradigm](https://img.shields.io/badge/paradigm-Object--Oriented%20Programming-brightgreen.svg)](#-object-oriented-programming-oop-principles)
[![Stage](https://img.shields.io/badge/stage-1%20completed-success.svg)](#-roadmap--future-enhancements)
[![License](https://img.shields.io/badge/license-MIT-informational.svg)](#)

An Object-Oriented Python application that performs skill-gap analysis by comparing candidate skills with job requirements. It evaluates compatibility, calculates a percentage-based match score, identifies missing competencies, and outputs structured analytical reports.

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Object-Oriented Programming (OOP) Principles](#-object-oriented-programming-oop-principles)
- [Project Architecture](#-project-architecture)
- [Getting Started](#-getting-started)
- [Usage Example](#-usage-example)
- [Sample Output](#-sample-output)
- [Roadmap & Next Stages](#-roadmap--future-enhancements)

---

## 📖 Overview

When candidates apply for technical roles, understanding their exact skill alignment and missing competencies is essential. This project provides a modular, extensible engine designed using **clean OOP principles** to analyze and report on candidate-job compatibility.

The system normalizes skill inputs, applies polymorphic analyzers (for score calculation and gap detection), and orchestrates report generation through a dedicated manager class.

---

## ✨ Key Features

- **Automated Skill Normalization:** Automatically cleans whitespace and converts input skills to lowercase to ensure accurate, case-insensitive comparison.
- **Match Score Calculation:** Computes the exact matching percentage between the student's skill set and the job's prerequisites.
- **Skill Gap Detection:** Identifies which required skills the candidate is currently missing.
- **Modular Analyzer Architecture:** Built on abstract base classes, making it straightforward to plug in new analysis criteria (e.g., weighted skills, minimum requirements).
- **Clean Report Formatting:** Generates clean, human-readable terminal reports.

---

## 🧠 Object-Oriented Programming (OOP) Principles

This project serves as a practical demonstration of the 4 core pillars of OOP:

| Principle | Implementation in Project |
| :--- | :--- |
| **Encapsulation** | `StudentProfile` and `JobDescription` protect internal attributes (`__skills`, `__student`, `__req_skills`) via private naming conventions, exposing safe access through getter methods. |
| **Abstraction** | `SkillAnalyzer` in `analyzers.py` inherits from `abc.ABC` and defines the abstract contract `@abstractmethod def analyze()`, hiding specific implementation details behind a clean interface. |
| **Inheritance** | Concrete classes `MatchScoreCalculator` and `MissingSkillDetector` inherit from the base `SkillAnalyzer` class. |
| **Polymorphism** | Both analyzers implement their own version of `.analyze(student, job)`. The `Manager` iterates over different analyzer objects uniformly without needing conditional logic for each. |

---

## 📂 Project Architecture

```text
mini_OOP_project/
│
├── models.py       # Data models (StudentProfile, JobDescription) with encapsulated attributes
├── analyzers.py    # Abstract base class (SkillAnalyzer) and concrete analyzers
├── manager.py      # Manager orchestrator for running analyses and printing reports
├── main.py         # Entry point demonstrating sample profiles and job evaluations
└── README.md       # Project documentation
```

### Class Responsibilities

- **`StudentProfile` (`models.py`)**: Represents a candidate, storing the candidate name and a normalized set of their skills.
- **`JobDescription` (`models.py`)**: Represents a job posting, storing the job title and a normalized set of required skills.
- **`SkillAnalyzer` (`analyzers.py`)**: Abstract base class defining the standard interface for analyzers.
- **`MatchScoreCalculator` (`analyzers.py`)**: Calculates overlapping skills and match percentage.
- **`MissingSkillDetector` (`analyzers.py`)**: Identifies skills required by the job that the student does not have.
- **`Manager` (`manager.py`)**: Coordinates analyzers, collects results, and prints the formatted analysis report.

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.8+** installed on your system.

### Installation & Execution

1. Clone or navigate to the project directory:
   ```bash
   cd mini_OOP_project
   ```

2. Run the application:
   ```bash
   python main.py
   ```

---

## 💻 Usage Example

```python
from models import StudentProfile, JobDescription
from manager import Manager

# 1. Define a student profile
student = StudentProfile("Aarav", ["Python", "SQL", "Java", "HTML", "CSS"])

# 2. Define job requirements
job = JobDescription("Junior Developer", ["Python", "Flask", "SQL", "Devops"])

# 3. Initialize Manager and run analysis
Manager(student, job).run_analysis()
```

---

## 📊 Sample Output

Running `python main.py` outputs:

```text
STUDENT - JOB SKILL ANALYSIS REPORT
Student Name: Aarav
Job Title: Junior Developer
Required Skills: 4
Matching Skills:
 - Sql
 - Python
Missing Skills:
 - Devops
 - Flask
Match Score: 50%
Explanation:
The student matches 2 out of 4 skills.Therefore, the skill match percentage is 50%

STUDENT - JOB SKILL ANALYSIS REPORT
Student Name: Aarav
Job Title: Frontend Developer
Required Skills: 5
Matching Skills:
 - Css
 - Html
Missing Skills:
 - React
 - Django
 - Javascript
Match Score: 40%
Explanation:
The student matches 2 out of 5 skills.Therefore, the skill match percentage is 40%
```

---

## 🔮 Roadmap / Future Enhancements

- [x] **Stage 1 (Completed):** Core data models, abstract analyzer architecture, match score calculator, missing skill detector, and terminal report manager.
- [ ] **Stage 2:** Interactive CLI prompt allowing users to enter custom students and jobs dynamically.
- [ ] **Stage 3:** Skill weightage (e.g., distinguishing between "Must-Have" vs "Good-to-Have" skills).
- [ ] **Stage 4:** Export reports to JSON or PDF format.
- [ ] **Stage 5:** Resume parser integration to automatically extract candidate skills.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).