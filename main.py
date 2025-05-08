import pandas as pd
import requests
import json
import os
from datetime import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload


def get_weather_data():
    city_name = 'london'
    WEATHER_API_KEY = os.environ['WEATHER_API_KEY']

    coor_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={WEATHER_API_KEY}'
    coor_req = requests.get(coor_url)
    coor_req.raise_for_status()
    coor_data = coor_req.json()

    if coor_data:
        lat = str(coor_data[0]['lat'])
        lon = str(coor_data[0]['lon'])
    else:
        print("No data found")
        return pd.DataFrame()

    fore_url = f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}'
    fore_req = requests.get(fore_url)
    json_data = json.loads(fore_req.text)

    forecast_list = json_data.get('list', [])
    weather_data = []

    for forecast in forecast_list:
        dt = pd.to_datetime(forecast['dt_txt'])
        weather = forecast['weather'][0]
        main = forecast['main']
        wind = forecast['wind']

        weather_data.append({
            'date': dt.date(),
            'time': dt.strftime('%H:%M:%S'),
            'weather': weather['main'],
            'weather_desc': weather['description'],
            'temp': main['temp'],
            'feels_like': main['feels_like'],
            'temp_min': main['temp_min'],
            'temp_max': main['temp_max'],
            'pressure': main['pressure'],
            'humidity': main['humidity'],
            'wind_speed': wind['speed'],
            'wind_deg': wind['deg'],
            'wind_gust': wind.get('gust', None)
        })

    weather_df = pd.DataFrame(weather_data)

    if not weather_df.empty:
        weather_df[['year', 'month', 'day']] = weather_df['date'].astype(str).str.split('-', expand=True)
        weather_df.drop(columns=['date'], inplace=True)
        cols = ['year', 'month', 'day'] + [col for col in weather_df.columns if col not in ['year', 'month', 'day']]
        weather_df = weather_df[cols]

    return weather_df


def upload_to_drive_service(filename, folder_id):
    creds_json = os.environ['GDRIVE_CREDS_JSON']
    creds = service_account.Credentials.from_service_account_info(json.loads(creds_json))
    service = build('drive', 'v3', credentials=creds)

    file_metadata = {
        'name': filename,
        'parents': [folder_id]
    }
    media = MediaFileUpload(filename, mimetype='text/csv')

    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

    print(f"Uploaded {filename} to Google Drive. File ID: {file.get('id')}")


if __name__ == "__main__":
    weather_df = get_weather_data()
    if not weather_df.empty:
        output_file = f"weather_forecast_{datetime.now().date()}.csv"
        weather_df.to_csv(output_file, index=False)
        print(f"CSV saved as {output_file}")

       # Replace with your actual Drive folder ID (after the last “/” from your folder link in google drive)
        folder_id = "1SWgsW72IGuHMnhoH6_iH28AVSfTzvu0Q"
        upload_to_drive_service(output_file, folder_id)
    else:
        print("No data to save.")
