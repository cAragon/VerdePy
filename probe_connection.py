from urllib.request import urlopen

def check_connection():
    try:
        response = urlopen('https://www.google.com/', timeout=10)
        return True
    except:
        return False
