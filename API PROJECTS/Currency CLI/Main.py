import requests

base_curr = input("Enter the currency to convert from: ").upper()
res_curr = input("Enter the currency to convert to: ").upper()
amt = float(input("Enter the amount: "))

url = f"https://open.er-api.com/v6/latest/{base_curr}"

try:
    response = requests.get(url, timeout=10)

    if response.status_code == 200:

        data = response.json()

        if data["result"] == "success":

            if res_curr in data["rates"]:

                convrate = data["rates"][res_curr]
                converted = amt * convrate

                print("\n========== Currency Converter ==========")
                print(f"Base Currency   : {base_curr}")
                print(f"Target Currency : {res_curr}")
                print(f"Amount          : {amt}")
                print(f"Exchange Rate   : {convrate}")
                print("----------------------------------------")
                print(f"{amt} {base_curr} = {converted:.2f} {res_curr}")
                print("========================================")

            else:
                print("❌ Invalid target currency code.")

        else:
            print("❌ Invalid base currency code.")

    else:
        print(f"❌ Request Failed! Status Code: {response.status_code}")

except requests.exceptions.Timeout:
    print("❌ Request timed out. Please try again.")

except requests.exceptions.ConnectionError:
    print("❌ No internet connection.")

except requests.exceptions.RequestException as e:
    print("❌ Request failed:", e)

except Exception as e:
    print("❌ Unexpected error:", e)
