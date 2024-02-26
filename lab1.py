# Panos Lelakis 1083712 lab1

import requests

url = input('Give URL: ')
response = requests.get(url)
headers = response.headers
print(headers)

# a
print('\nServer software: ', headers.get('Server'))

# b
cookies = response.cookies
if len(cookies) != 0:
    print('\nWebpage is using cookies')

# c
    for cookie in cookies:
        print('Cookie name: '+ cookie.name)
        print('Cookie expiration time: '+ str(cookie.expires))
    
else:
    print('\nWebpage is NOT using cookies')

# Source: https://stackoverflow.com/questions/22577182/python-get-cookie-expiry-time-using-the-requests-library

#b
#if 'Set-Cookie' in headers:
    #print('Webpage is using cookies')

#c
    #cookies = headers['Set-Cookie'].split(',')
    #for cookie in cookies:
        #cookie_parts = cookie.split(';')
        #cookie_name = cookie_parts[0].split('=')[0].strip()
        #expires = None
        #for part in cookie_parts:
            #if part.strip().startswith('Expires='):
                #expires = part.split('=')[1].strip()
                #expires = datetime.strptime(expires, '%a, %d %b %Y %H:%M:%S %Z')
                #break
        #if expires:
            #print("Cookie:", cookie_name, "Expires:", expires)
        #else:
            #print("Cookie:", cookie_name, "Expires: None")
#else:
    #print('Webpage is not using cookies')