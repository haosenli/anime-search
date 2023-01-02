import requests

def get_top_anime():
    url = 'https://api.jikan.moe/v4/top/anime?filter=airing'
    response = requests.get(url)
    if response.status_code != 200:
        print('[ERROR] status code:', response.status_code)
        return
    data = response.json()
    for char in data['data']:
        for k, v in char.items():
            if k == 'title' or k == 'status'or k == 'images':
                print(k, v)
        print()

def get_season_now():
    url = 'https://api.jikan.moe/v4/seasons/now'
    response = requests.get(url)
    if response.status_code != 200:
        print('[ERROR] status code:', response.status_code)
        return
    data = response.json()
    for char in data['data']:
        for k, v in char.items():
            if k == 'title' or k == 'status'or k == 'broadcast':
                print(k, v)
        print()

def get_anime_full():
    anime_id = 34798
    url = f'https://api.jikan.moe/v4/anime/{anime_id}/full'
    response = requests.get(url)
    if response.status_code != 200:
        print('[ERROR] status code:', response.status_code)
        return
    data = response.json()
    for holy, sht in data['data'].items():
        print(holy, sht)
        
def get_anime_episodes():
    anime_id = 34798
    url = f'https://api.jikan.moe/v4/anime/{anime_id}/episodes'
    response = requests.get(url)
    if response.status_code != 200:
        print('[ERROR] status code:', response.status_code)
        return
    data = response.json()
    for holy in data['data']:
        print(holy)
        
def get_anime_images():
    anime_id = 38475
    url = f'https://api.jikan.moe/v4/anime/{anime_id}/pictures'
    response = requests.get(url)
    if response.status_code != 200:
        print('[ERROR] status code:', response.status_code)
        return
    data = response.json()
    for holy in data['data']:
        print(holy)
        
def get_anime_videos():
    anime_id = 38475
    url = f'https://api.jikan.moe/v4/anime/{anime_id}/videos'
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
        
def get_person_full_by_id():
    id = 11184
    url = f'https://api.jikan.moe/v4/people/{id}/full'
    response = requests.get(url)
    if response.status_code != 200:
        print('[ERROR] status code:', response.status_code)
        return
    data = response.json()
    for holy, sht in data['data'].items():
        print(holy, sht)

def get_schedule():
    url = 'https://api.jikan.moe/v4/schedules/?filter=unknown'
    response = requests.get(url)
    if response.status_code != 200:
        print('[ERROR] status code:', response.status_code)
        return
    data = response.json()
    for char in data['data']:
        for k, v in char.items():
            if k == 'title' or k == 'status'or k == 'broadcast':
                print(k, v)
        print()
        
def get_characters_search():
    url = 'https://api.jikan.moe/v4/characters/?q=kanna&order_by=favorites&sort=desc'
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
    get_top_anime()
    # get_anime_full()
    # get_anime_episodes()
    # get_anime_images()
    # get_anime_videos()
    # get_anime_characters()  
    # get_person_full_by_id()
    # get_characters_search()
    # get_schedule()

if __name__ == '__main__':
    main()