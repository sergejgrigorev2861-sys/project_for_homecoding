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

def filter_young_rich_passengers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Фильтрует пассажиров с ценой билета > 50 и возрастом < 30,
    затем сортирует по имени в алфавитном порядке.
    """

    # Фильтруем: цена билета > 50 И возраст < 30
    filtered = df[(df['Fare'] > 50) & (df['Age'] < 30)]

    # Сортируем по имени в алфавитном порядке
    result = filtered.sort_values('Name')

    return result

def get_passenger_stats_by_class(df: pd.DataFrame) -> str:
    """
    Группирует пассажиров по классу и вычисляет:
    - среднюю стоимость билета
    - количество пассажиров
    """
    # группируем по классу (Pclass) и агрегируем
    stats = df.groupby('Pclass').agg(
        average_ticket_price=('Fare', 'mean'),
        passenger_count=('Fare', 'count')
    ).round(2)

    # преобразуем в словарь и заменяем ключи на "1st", "2nd", "3rd"
    result = {}
    class_names = {1: "1st", 2: "2nd", 3: "3rd"}

    for pclass, row in stats.iterrows():
        result[class_names[pclass]] = {
            "average_ticket_price": row['average_ticket_price'],
            "passenger_count": int(row['passenger_count'])
        }

    return json.dumps(result, ensure_ascii=False, indent=4)

def save_survivors_to_json(df: pd.DataFrame, output_path: str) -> int:
    """
    Фильтрует выживших пассажиров и сохраняет их данные в JSON-файл.
    """
    # Фильтруем выживших (Survived == 1)
    survivors = df[df['Survived'] == 1].copy()

    # Приеобразуем в список словарей
    survivors_list = survivors.to_dict(orient='records')

    # Сохраняем в JSON-файл
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(survivors_list, f, ensure_ascii=False, indent=4)

    # Возврашаем количество выживших
    return len(survivors)

if __name__ == '__main__':

    # Проверка первой функции
    print("=== Средний возраст ===")
    print(get_average_age_by_sex('data/titanic.csv'))

    # Проверка второй функции
    print("\n === Фильтрация и сортировка ===")
    df = pd.read_csv('data/titanic.csv')
    result = filter_young_rich_passengers(df)
    print(result[['Name', 'Age','Fare']].head(10).to_markdown(index=False))

    # Проверка третьей функции
    print("\n=== Статистика по классам ===")
    print(get_passenger_stats_by_class(df))

    # Проверка чертвертой функции
    print("\n=== Сохранение выживших в JSON ===")
    survivors_count = save_survivors_to_json(df, 'data/survivors_count.json')
    print(f"Количество выживших пассажиров: {survivors_count}")
