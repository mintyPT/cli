#!/usr/bin/python
import json
import requests


def getPageTitle(_url):
    r = requests.get(_url)

    source = r.text

    _tini = source.find('<title>')
    _tfin = source.find('</title>')

    if _tini == -1 or _tfin == -1:
        return ''

    return source[_tini+7:_tfin]



def bitlyAccountCreator(username, password, email):
    

    s = requests.session()

    s.get('https://bitly.com/')

 
    headers = { 'X-Requested-With': 'XMLHttpRequest',
                'X-XSRFToken': s.cookies['_xsrf'],
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5'}

    signinPayload = { 'username': username,
                     'password': password,
                     'email': email,
                     'rd': '/'}



    r = s.post('https://bitly.com/a/sign_up', data=signinPayload, headers=headers)

    response    = json.loads(r.text)
    status_code = response['status_code']
    status_txt  = response['status_txt']

    

    if status_code == 200 and status_txt == 'OK':
        return True
    else:
        for key in response['data']['errors']:
            print '\t==> %s: \t%s' % (key, response['data']['errors'][key])
        return False
    



def bitly(long_url, login_user, login_password):
    

    s = requests.session()

    s.get('https://bitly.com/')

 
    headers = { 'X-Requested-With': 'XMLHttpRequest',
                'X-XSRFToken': s.cookies['_xsrf'],
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5'}

    loginPayload = { 'username': 'customemoustard',
                     'password': 'customemoustard',
                     'rd': '/'}

    longUrlPayload = {  'longUrl': long_url,
                        'private':'false',
                        'title': getPageTitle(long_url)}

    r = s.post('https://bitly.com/a/sign_in', data=loginPayload, headers=headers)

    response    = json.loads(r.text)
    status_code = response['status_code']
    status_txt  = response['status_txt']

    boolLogin = False

    if status_code == 200 and status_txt == 'OK':
        boolLogin = True
    else:
        print 'something went wrong with the login'
        print response
        return
    

    if boolLogin == True:

        r = s.post('https://bitly.com/data/beta/save', data=longUrlPayload, headers=headers)

        response    = json.loads(r.text)
        status_code = response['status_code']
        status_txt  = response['status_txt']

        if status_code == 200 and status_txt == 'OK':
            return response['data']['link']

        elif status_code == 304 and status_txt == 'LINK_ALREADY_EXISTS':
            return response['data']['link_save']['link']

        else:
            print 'something went wrong with the url shortner'
            print response
            return










# login    = ''  
# password = ''    
# url = ''
# print bitly(url, login, password)

# username = ''
# email = ''
# password = ''
# bitlyAccountCreator(username, password, email)

    

