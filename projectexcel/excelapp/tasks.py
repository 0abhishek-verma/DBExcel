from celery import shared_task
import requests

@shared_task
def call_download_excel_api():
    print("🚀 Celery task started!")
    url = "http://127.0.0.1:8000/api/excel-download/"  # Replace with your actual API endpoint
    try:
        response = requests.get(url)
        return f"Status: {response.status_code}"
    except Exception as e:
        return str(e)