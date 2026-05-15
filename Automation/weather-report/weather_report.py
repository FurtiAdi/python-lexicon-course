import os
import smtplib
import requests
from datetime import datetime
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv(
    "/Users/furtunaeyob/Library/CloudStorage/OneDrive-StockholmUniversity/Skrivbordet/python_course_lexicon/python-lexicon-course/.env"
)

# Cities with coordinates
cities = {
    "Stockholm": (59.3293, 18.0686),
    "Gothenburg": (57.7089, 11.9746),
    "Malmo": (55.6050, 13.0038)
}

def get_weather(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url)
    data = response.json()
    return data["current_weather"]

def generate_report():
    report = f"Weather Report - {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
    report += "-" * 40 + "\n"

    for city, (lat, lon) in cities.items():
        weather = get_weather(lat, lon)
        report += f"{city}:\n"
        report += f"  Temperature: {weather['temperature']}°C\n"
        report += f"  Wind Speed: {weather['windspeed']} km/h\n\n"

    return report

def send_email(report):
    sender = "furtiadi@gmail.com"
    receiver = "adhanomdk@gmail.com"
    password =  os.getenv("APP_PASSWORD")

    msg = MIMEText(report)
    msg["Subject"] = "Daily Weather Report"
    msg["From"] = sender
    msg["To"] = receiver

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print("Error sending email:", e)


def save_report(report):
    with open("/Users/furtunaeyob/Library/CloudStorage/OneDrive-StockholmUniversity/Skrivbordet/python_course_lexicon/python-lexicon-course/Automation/weather-report/weather_log.txt", "a") as file:
        file.write(report + "\n")


if __name__ == "__main__":
    report = generate_report()
    print(report)
    save_report(report)
    send_email(report)