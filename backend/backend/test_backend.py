from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_post_registro():
    payload = {
        "cpf": "12345678900",
        "baseline_value": 120,
        "accelerations": 0.003,
        "fetal_movement": 0.002,
        "uterine_contractions": 0.01,
        "light_decelerations": 0.0,
        "severe_decelerations": 0.0,
        "prolongued_decelerations": 0.0,
        "abnormal_short_term_variability": 0.0,
        "mean_value_of_short_term_variability": 0.8,
        "percentage_of_time_with_abnormal_long_term_variability": 10,
        "mean_value_of_long_term_variability": 3.0,
        "histogram_width": 50,
        "histogram_min": 60,
        "histogram_max": 150,
        "histogram_number_of_peaks": 3,
        "histogram_number_of_zeroes": 1,
        "histogram_mode": 130,
        "histogram_mean": 135,
        "histogram_median": 133,
        "histogram_variance": 12,
        "histogram_tendency": 1
    }


    response = client.post("/registros", json=payload)
    assert response.status_code == 200
    assert "fetal_health" in response.json()
