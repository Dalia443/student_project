# analysis.py
import os
from datetime import date
import statistics

def calculate_student_metrics(students):
    """
    Calcule l'âge de chaque étudiant et la moyenne de ses 3 notes.
    """
    current_year = date.today().year
    analyzed_students = []
    
    for s in students:
        # Calcul de l'âge (Année actuelle - Année de naissance)
        age = current_year - s["birth_date"].year
        
        # Calcul de la moyenne des notes
        avg_grade = sum(s["grades"]) / len(s["grades"])
        
        analyzed_students.append({
            "id": s["id"],
            "birth_date": s["birth_date"],
            "grades": s["grades"],
            "age": age,
            "average_grade": round(avg_grade, 2)
        })
        
    return analyzed_students


def get_class_statistics(analyzed_students):
    """
    Calcule les statistiques globales de la classe demandées par le TP :
    - mean (moyenne)
    - median (médiane)
    - standard deviation (écart-type)
    - minimum et maximum average (min/max des moyennes)
    - mean age (âge moyen)
    """
    averages = [s["average_grade"] for s in analyzed_students]
    ages = [s["age"] for s in analyzed_students]
    
    stats = {
        "mean": round(statistics.mean(averages), 2),
        "median": round(statistics.median(averages), 2),
        "std_dev": round(statistics.stdev(averages), 2) if len(averages) > 1 else 0.0,
        "min_average": min(averages),
        "max_average": max(averages),
        "mean_age": round(statistics.mean(ages), 2)
    }
    
    return stats


def save_report(stats, filename="results/report.txt"):
    """
    Crée automatiquement le dossier 'results' s'il n'existe pas 
    et sauvegarde le résumé statistique dans le fichier 'report.txt'.
    """
    # Crée le dossier 'results' automatiquement
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # Écrit les statistiques dans le fichier texte
    with open(filename, "w", encoding="utf-8") as f:
        f.write("=== RAPPORT STATISTIQUE DE LA CLASSE ===\n\n")
        f.write(f"Moyenne de la classe (Mean) : {stats['mean']}\n")
        f.write(f"Médiane (Median) : {stats['median']}\n")
        f.write(f"Écart-type (Standard Deviation) : {stats['std_dev']}\n")
        f.write(f"Moyenne minimum : {stats['min_average']}\n")
        f.write(f"Moyenne maximum : {stats['max_average']}\n")
        f.write(f"Âge moyen (Mean Age) : {stats['mean_age']} ans\n")
    
    print(f"Rapport sauvegardé avec succès dans le fichier : {filename}")
