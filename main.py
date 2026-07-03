import requests
import pandas as pd
from datetime import datetime

# 1. Запрос к открытому API NASA (используем демо-ключ DEMO_KEY)
date_today = datetime.today().strftime('%Y-%m-%d')
url = f"https://api.nasa.gov/rest/v1/feed?start_date={date_today}&end_date={date_today}&api_key=DEMO_KEY"

print(f"Загрузка космических данных NASA за {date_today}...")
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    asteroids = data['near_earth_objects'][date_today]
    
    asteroid_list = []
    
    # 2. Сбор и парсинг данных об астероидах
    for ast in asteroids:
        name = ast['name']
        size_min = ast['estimated_diameter']['meters']['estimated_diameter_min']
        size_max = ast['estimated_diameter']['meters']['estimated_diameter_max']
        avg_size = (size_min + size_max) / 2
        
        speed = float(ast['close_approach_data'][0]['relative_velocity']['kilometers_per_hour'])
        miss_distance = float(ast['close_approach_data'][0]['miss_distance']['kilometers'])
        is_hazardous = ast['is_potentially_hazardous_asteroid']
        
        asteroid_list.append({
            "Name": name,
            "Avg Diameter (m)": round(avg_size, 2),
            "Speed (km/h)": round(speed, 2),
            "Miss Distance (km)": round(miss_distance, 2),
            "Potentially Hazardous": is_hazardous
        })
    
    # 3. Анализ данных с помощью pandas
    df = pd.DataFrame(asteroid_list)
    
    print("\n--- Сводный анализ околоземных объектов на сегодня ---")
    print(df.to_string(index=False))
    
    # 4. Политико-технологический вывод (фильтрация потенциальных угроз)
    hazardous_ones = df[df["Potentially Hazardous"] == True]
    print("\n--- Анализ космической безопасности ---")
    if not hazardous_ones.empty:
        print(f"Внимание! Обнаружено потенциально опасных объектов: {len(hazardous_ones)}")
        print(hazardous_ones[["Name", "Avg Diameter (m)", "Miss Distance (km)"]])
    else:
        print("Сегодня потенциально опасных астероидов вблизи Земли не обнаружено. Орбита стабильна.")

else:
    print("Ошибка при получении данных от NASA. Проверьте подключение или API-ключ.")
