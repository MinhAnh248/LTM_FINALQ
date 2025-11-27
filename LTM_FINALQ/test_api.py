import requests
import json

API_URL = 'http://localhost:5000/api'

# Login
print("=== LOGIN ===")
login_data = {
    'email': 'minhanh@gmail.com',
    'mat_khau': '123456'
}
response = requests.post(f'{API_URL}/auth/login', json=login_data)
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")

if response.status_code == 200:
    token = response.json()['access_token']
    
    # Get categories
    print("\n=== GET CATEGORIES ===")
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(f'{API_URL}/danh-muc', headers=headers)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
