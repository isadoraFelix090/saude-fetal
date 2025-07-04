from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()



class ExameFetal(BaseModel):
    cpf: str
    baseline_value: float
    accelerations: float
    fetal_movement: float
    uterine_contractions: float
    light_decelerations: float
    severe_decelerations: float
    prolongued_decelerations: float
    abnormal_short_term_variability: float
    mean_value_of_short_term_variability: float
    percentage_of_time_with_abnormal_long_term_variability: float
    mean_value_of_long_term_variability: float
    histogram_width: float
    histogram_min: float
    histogram_max: float
    histogram_number_of_peaks: float
    histogram_number_of_zeroes: float
    histogram_mode: float
    histogram_mean: float
    histogram_median: float
    histogram_variance: float
    histogram_tendency: float


@app.post("/registros")
def analisar_exame(exame: ExameFetal):
    resultado = 1
    return {
        "cpf": exame.cpf,
        "fetal_health": resultado
    }
