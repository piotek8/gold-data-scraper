from app import get_gold_price


if __name__ == "__main__":
    user_date = input("Enter the date in the format DD-MM-YYYY (example: 20-12-2023): ")
    result = get_gold_price(user_date)
    print("-" * 45)
    print(result)
    print("-" * 45)