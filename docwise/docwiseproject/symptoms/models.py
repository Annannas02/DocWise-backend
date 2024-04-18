from django.db import models
from user.models import User

class Symptoms(models.Model):
    
    ABDOMINAL_CRAMPS = 1
    ACNEE = 2
    APPETITE_CHANGE = 3
    BODY_MUSCLE_ACHE = 4
    BLOATING = 4
    BREAST_PAIN = 5
    CHEST_TIGHTNESS =6
    CHILLS=7
    COUGHING=8
    DIZZINESS=9
    DRY_SKIN=10
    FATIGUE=11
    FEVER=12
    HEADACHE=13
    LOWER_BACK_PAIN=14
    MOOD_CHANGES=15
    NAUSEA=16
    SKIPPED_HEARTBEATS=17
    VOMITING=18
    WHEEZING=19

    SYMPTOM_TYPE = (
        (ABDOMINAL_CRAMPS, "Abdominal cramps"),
        (ACNEE, "Acnee"),
        (APPETITE_CHANGE, "Appetite changes"),
        (BODY_MUSCLE_ACHE, "Body and muscle ache"),
        (BLOATING, "Bloating"),
        (BREAST_PAIN, "Breast pain"),
        (CHEST_TIGHTNESS, "Chest tightness or pain"),
        (CHILLS, "Chills"),
        (COUGHING, "Coughing"),
        (DIZZINESS, "Dizziness"),
        (DRY_SKIN, "Dry skin"),
        (FATIGUE ,"Fatigue"),
        (FEVER, "Fever"),
        (HEADACHE, "Headache"),
        (LOWER_BACK_PAIN, "Lower back pain"),
        (MOOD_CHANGES, "Mood changes"),
        (NAUSEA, "Nausea"),
        (SKIPPED_HEARTBEATS, "Skipped heartbeats"),
        (VOMITING, "Vomiting"),
        (WHEEZING, "Wheezing")

    )

    NP = 1
    P = 2
    MILD = 3
    MODERATE = 4

    SYMPTOM_STRENGTH = {
        (NP, "Not present"),
        (P, "Present"),
        (MILD, "Mild"),
        (MODERATE, "Moderate")
    }

    personid = models.ForeignKey(User, on_delete=models.CASCADE)
    symptom = models.IntegerField(choices=SYMPTOM_TYPE)
    severity = models.IntegerField(choices=SYMPTOM_STRENGTH)
    timestamp = models.DateTimeField()

    