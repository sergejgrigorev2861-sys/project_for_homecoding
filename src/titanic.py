"""
Модуль для анализа данных пассажиров Titanic.
"""
import json
import pandas as pd

def get_average_age_by_sex(file_path: str) -> str:
    """
    Вычисляет средний возраст мужчин и женщин из данных Titanic.
    """
    df = pd.read_csv(file_path)
    avg_age = df.groupby('Sex')['Age'].mean().round(2)

    result = {
        'male': avg_age.get('male', 0.0),
        'female': avg_age.get('female', 0.0),
    }
    return json.dumps(result, ensure_ascii=False)