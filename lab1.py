# Panos Lelakis 1083712 lab1

import requests

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break

url = input('Give URL: ')

with requests.get(url) as response:
    headers = response.headers
    print(headers)

# a
    server = headers.get('Server')
    if server:
        print('\nServer software: ', server)
    else:
        print('\nNo server found')

# b
    cookies = response.cookies
    if len(cookies) != 0:
        print('\nWebpage is using cookies')

# c
        for cookie in cookies:
            print('Cookie name: ', cookie.name)
            print('Cookie expiration time: ', str(cookie.expires))
    
    else:
        print('\nWebpage is NOT using cookies')