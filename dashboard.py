import os
import requests
import json

api_key = os.getenv('eyJrIjoiU3JZNlpsMW9hRTdqN3dwYnhxa3NVZDVuZDJnNFp4NjgiLCJuIjoic2NyaXB0X3B5dGhvbiIsImlkIjoxfQ==')

base_url = 'http://10.0.0.9:3000/api'
headers = {
    'Authorization': 'Bearer ' + 'eyJrIjoiU3JZNlpsMW9hRTdqN3dwYnhxa3NVZDVuZDJnNFp4NjgiLCJuIjoic2NyaXB0X3B5dGhvbiIsImlkIjoxfQ=='
}

response = requests.get(url=base_url + '/search', headers=headers)

