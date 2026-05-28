from pydantic import BaseModel

class StudentInput(BaseModel):
    school: str        # "GP" or "MS"
    sex: str           # "F" or "M"
    age: int
    address: str       # "U" or "R"
    famsize: str       # "GT3" or "LE3"
    Pstatus: str       # "T" or "A"
    Medu: int          # 0-4
    Fedu: int          # 0-4
    Mjob: str          # "teacher", "health", "services", "at_home", "other"
    Fjob: str          # "teacher", "health", "services", "at_home", "other"
    reason: str        # "home", "reputation", "course", "other"
    guardian: str      # "mother", "father", "other"
    traveltime: int    # 1-4
    studytime: int     # 1-4
    failures: int      # 0-4
    schoolsup: str     # "yes" or "no"
    famsup: str        # "yes" or "no"
    paid: str          # "yes" or "no"
    activities: str    # "yes" or "no"
    nursery: str       # "yes" or "no"
    higher: str        # "yes" or "no"
    internet: str      # "yes" or "no"
    romantic: str      # "yes" or "no"
    famrel: int        # 1-5
    freetime: int      # 1-5
    goout: int         # 1-5
    Dalc: int          # 1-5
    Walc: int          # 1-5
    health: int        # 1-5
    absences: int      # 0+

class PredictionOutput(BaseModel):
    prediction: int
    prediction_label: str
    probability: list