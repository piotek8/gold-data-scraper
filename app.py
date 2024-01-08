from constants import URL
import requests
from datetime import datetime


def get_gold_price(date):
    try:
        formatted_date = datetime.now().strftime("%Y-%m-%d") if date.lower() == "today" else "-".join(
            reversed(date.split("-")))

        url = f"{URL}{formatted_date}"

        response = requests.get(url)
        if response.status_code == 200:
            gold_data = response.json()
            gold_price = gold_data[0]["cena"]
            return (f"Gold price on {formatted_date}: {gold_price} PLN per gram")
        else:
            return(f"Failed to retrieve the gold price. HTTP status code: {response.status_code}")
    except requests.RequestException as e:
        return (f"An error occurred while fetching the data: {e}")
