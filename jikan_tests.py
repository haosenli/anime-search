import requests

def get_anime_full():
    anime_id = 38475
    url = f'https://api.jikan.moe/v4/anime/{anime_id}/full'
    response = requests.get(url)
    if response.status_code != 200:
        print('[ERROR] status code:', response.status_code)
        return
    data = response.json()
    for holy, sht in data['data'].items():
        print(holy, sht)
    
def get_anime_characters():
    anime_id = 38475
    url = f'https://api.jikan.moe/v4/anime/{anime_id}/characters'
    response = requests.get(url)
    if response.status_code != 200:
        print('[ERROR] status code:', response.status_code)
        return
    data = response.json()
    for char in data['data']:
        for k, v in char.items():
            print(k, v)
        print()

def main():
    get_anime_characters()        

if __name__ == '__main__':
    main()