import requests

url = "https://site-wordpress/wp-cron.php"

tries = 9999

count = 0

while count < tries:
    try:
        req = requests.get(url=url)
        count +=1
    except:
        break