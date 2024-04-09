import requests

def exchange_code_for_token(code):
    client_id = 'daeea42af07e4702905904f246591317'
    client_secret = '3ef2f6e66658400490e6add0739a9a3b'
    redirect_uri = 'https://swoodberry13.github.io/Bones_and_Company/'
    
    # Spotify token endpoint
    token_url = 'https://accounts.spotify.com/api/token'
    
    # Request body
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri
    }
    
    # POST request to exchange code for token
    response = requests.post(token_url, data=data)
    response_data = response.json()
    
    if 'access_token' in response_data:
        access_token = response_data['access_token']
        return access_token
    else:
        print("Error: Failed to exchange code for token")
        return None

# Example usage:
# code = 'THE_AUTHORIZATION_CODE_RECEIVED_FROM_SPOTIFY'
# access_token = exchange_code_for_token(code)
# print(access_token)
