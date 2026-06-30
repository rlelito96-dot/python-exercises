
import time

def get_data():
    print(f"Pobieranie danych...")
    time.sleep(2)
    return "Dane gotowe"

print(get_data())
print(f"Koniec programu")


#////////////////////////////////////////////


import asyncio


async def get_data():
    print(f"Pobieranie danych...")
    await asyncio.sleep(2)
    return "Dane gotowe"

async def main():
    print(f"Start programu...")
    result = await get_data()
    print(result)
    print(f"Koniec programu")

asyncio.run(main())

#////////////////////////////////////////////


import asyncio

async def fetch_data(number):
    print(f"Pobieranie danych {number}...")
    await asyncio.sleep(2)
    print(f"Dane {number} pobrane")
    return number * 10

async def main():
    tasks = [fetch_data(i) for i in range(1, 4)]
    results = await asyncio.gather(*tasks)
    print("Wyniki:", results)

asyncio.run(main())
