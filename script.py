#-- imports with requisites, mandatory to have modules installed
import time
import requests
import sys
from termcolor import colored
from tqdm import tqdm

#-- Starting code to check urls
def check_status(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(colored(f'{url} is up!', 'green'))
            return True
        else:
            print(colored(f'{url} is down!', 'red'))
            return False
    except requests.ConnectionError:
        print(colored(f'{url} is down!', 'red'))
        return False

def read_file(file_name):
    with open(file_name, 'r') as file:
        urls = file.readlines()
        return urls

#-- File and Recheck function
if __name__ == '__main__':
    while True:
        urls = read_file('web.txt') #-- Input file here, if you want to change de def name change here.
        for url in urls:
            check_status(url.strip())
        for _ in tqdm(range(60), desc='Checking again in:', unit='sec'): #-- range(60) = 60 seconds, if you want a lower interval to recheck all change here
            time.sleep(1)
            sys.stdout.flush()
