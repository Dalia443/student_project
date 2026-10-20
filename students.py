# students.py
import random
from datetime import date

def generate_students(num_students=10):
    """
    Génère une liste de dictionnaires représentant les étudiants avec :
    - Un ID étudiant
    - Une date de naissance aléatoire entre 2000 et 2006
    - Trois notes aléatoires entre 0 et 20
    """
    students = []
    
    for i in range(1, num_students + 1):
        student_id = f"STU{i:03d}"
        
        # Année de naissance aléatoire entre 2000 et 2006
        year = random.randint(2000, 2006)
        month = random.randint(1, 12)
        day = random.randint(1, 28) # Sécurisé pour éviter les erreurs de jours par mois
        birth_date = date(year, month, day)
        
        # 3 notes aléatoires entre 0 et 20 (arrondies à 2 décimales)
        grades = [round(random.uniform(0, 20), 2) for _ in range(3)]
        
        student = {
            "id": student_id,
            "birth_date": birth_date,
            "grades": grades
        }
        students.append(student)
        
    return students
