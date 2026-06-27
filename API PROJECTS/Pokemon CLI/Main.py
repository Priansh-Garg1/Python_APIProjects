import requests

name=input("Enter the Pokemon name : ").lower().strip()


url = f"https://pokeapi.co/api/v2/pokemon/{name}"
try :
    response = requests.get(url , timeout=10)
    data=response.json()
    if response.status_code==200:
        name=(data["name"]).capitalize()
        height=str(int(data["height"])/10)+"m"
        weight= str(int(data["weight"])/10)+"kg"
        basexp=data["base_experience"]
        
        
        print("========== Pokémon Information ==========")
        print(f"Name            :{name}")
        print(f"Height          :{height}")
        print(f"Weight          :{weight}")
        print(f"Base Experience :{basexp}")
        print("Type(s):")
        for i in data["types"]:
            print("\t-",i["type"]["name"])
        print("Ability(s):")
        for i in data["abilities"]:
            print("\t-", i["ability"]["name"])
        print("=========================================")
    else :
        print("Status Code" , response.status_code,"Please retry")


except requests.exceptions.Timeout:
    print("Request Timed Out")

except requests.exceptions.ConnectionError:
    print("No Internet Connection")

except requests.exceptions.RequestException as e:
    print("Request Failed:", e)

except Exception as e:
    print("Unexpected Error:", e)
