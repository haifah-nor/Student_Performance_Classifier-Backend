import joblib
import os

BASE_DIR = os.path.dirname(__file__)

model_path = os.path.join(
    BASE_DIR,
    "svm_student_model_f1_optimized.pkl"
)

model = joblib.load(model_path)