# Reference:
#  - https://github.com/RedFurrFox/PSpammerv2

import requests, threading, random, string, humanize, datetime, os
from requests.adapters import HTTPAdapter, Retry
from urllib.parse import urlparse, parse_qs
from colorama import Fore, Style

os.system('cls||clear')

success=0
failed=0

def banner():
    print(f"""{Fore.CYAN}
  _, __,  _, _, _ _, _ _ _, _  _,   __, _,_ _  _, _ _, _  _,
 (_  |_) / \ |\/| |\/| | |\ | / _   |_) |_| | (_  | |\ | / _
 , ) |   |~| |  | |  | | | \| \ /   |   | | | , ) | | \| \ /
  ~  ~   ~ ~ ~  ~ ~  ~ ~ ~  ~  ~    ~   ~ ~ ~  ~  ~ ~  ~  ~ 
                       {Fore.GREEN}~ By Rizsyad AR ~{Fore.RESET}
                  {Fore.RED} - Let's destroyed Phising - {Fore.RESET}
""")

def random_str():
    """random_str()

    Returns:
        String: get random string
    """
    
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(100, 200)))

def random_number():
    """random_number()

    Returns:
        String: get random number
    """

    return ''.join(random.choice(string.digits) for _ in range(random.randint(50, 100)))

def random_email():
    """random_email()

    Returns:
        String:  get random email
    """

    str = random_str()
    domain = ["gmail","outlook","me","yahoo","pornhub","microsoft","youtube","pornhub","brazzers","google","hotmail","insta","facebook","msn","gore","freebrazzers"]
    return f'{string}@{random.choice(domain)}.com'

def random_useragents():
    """random_useragents()

    Returns:
        String: get random user agent in useragent.txt file
    """

    useragents = open('useragents.txt','r').readlines()
    return random.choice(useragents).replace('\n', '')

def random_ip():
	a = random.randint(1,999)
	b = random.randint(0,999)
	c = random.randint(0,999)
	d = random.randint(0,999)
	return  str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d)

def generate_data(data):
    """generate_data(data)

    Args:
        data (String): form data payload ex: email={email}&password={string}

    Returns:
        String: get payload with patch data
    """

    return data.replace('{email}', random_email()).replace('{string}', random_str()).replace('{number}', random_number())

def req_spam(url, data):
    """req_spam(url, data)

    Args:
        url (String): url phising or scammers
        data (String): form data payload ex: email={email}&password={string}

    Return:
        Print success or faild message post request
    """

    global success, failed

    while True:
        domain = urlparse(url).netloc
        protocol = urlparse(url).scheme
        ip = random_ip()
        data = generate_data(data)

        dataJson = { k: v
            for k, vs in parse_qs(data).items()
            for v in vs
        } 

        headers = {
            'Authority': domain,
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': f'{protocol}://{domain}',
            'Referer': f'{protocol}://{domain}',
            'Upgrade-Insecure-Requests': '1',
            "X-Originating-IP": ip,
            'X-Forwarded-For': ip,
            "X-Remote-IP": ip,
            "X-Remote-Addr": ip,
            "X-Client-IP": ip,
            'User-Agent': random_useragents()
        }

        try:
            s=requests.Session()
            retry=Retry(connect=3, backoff_factor=0.5)
            adapter=HTTPAdapter(max_retries=retry)
            s.mount('http://', adapter)
            s.mount('https://', adapter)

            response = requests.post(url, headers=headers, data=data)

            if response.status_code == 200:
                print(f'{Fore.CYAN}{Style.BRIGHT} [+] Spam Sent Successfully To This {url} Link {Fore.RESET}')
                print(f'{Fore.BLUE}{Style.BRIGHT} [*] Generated Data = {dataJson}\n {Fore.RESET}')
                success = success + 1
            else:
                print(f'{Fore.RED}{Style.BRIGHT} [-] Spam Sent Fail To This {url} Link {Fore.RESET}')
                print(f'{Fore.BLUE}{Style.BRIGHT} [*] Generated Data = {dataJson}\n {Fore.RESET}')
                failed = failed + 1
                pass       

        except Exception as e:
            print(f'{Fore.RED}{Style.BRIGHT} [-] Spam Sent Fail To This {url} Link {Fore.RESET}')
            print(f'{Fore.BLUE}{Style.BRIGHT} [*] Generated Data = {dataJson}\n {Fore.RESET}')
            failed = failed + 1
            pass

banner()

print(f"""
{Fore.BLUE}[?]{Fore.RESET} Please Choose Your Selection To Start:
{Fore.BLUE}[01]{Fore.RESET} Start
{Fore.BLUE}[02]{Fore.RESET} Help
{Fore.BLUE}[00]{Fore.RESET} Exit\n
""")

select = input(f"{Fore.BLUE}[=]{Fore.RESET} Your Selection: ")
templateData = "email={email}&username={string}&password={string}&login=submit"
infoParse = """
\t\t{email} - generate random Email
\t\t{string} - generate random string
\t\t{number} - generate random number
"""

try:
    if select == "1" or select == "01":

        url = input(f"{Fore.BLUE}[?]{Fore.RESET} Please Enter The url Phising/Scam: ")
        data = input(f"{Fore.BLUE}[?]{Fore.RESET} Please Enter The FormData: ")

        start_time = datetime.datetime.now()
        threads = []

        for i in range(150):
            t = threading.Thread(target=req_spam, args=(url, data))
            t.daemon = True
            threads.append(t)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

    elif select == "2" or select == "02":
        print(f"""{Fore.CYAN}{Style.BRIGHT}
        ========================================================================
        To Use This Tool, You Must Collect The Following:
        ========================================================================
            - URL Where The Data You've Entered Goes 
                Example: Use 'https://target.com/reward.php' 
                Instead Of: 'https://target.com'
            - FormData Request 
                Example: '{templateData}' for FormData request based on url
                {infoParse}
        ------------------------------------------------------------------------
        You Can Access All Of This By Using A Built-in DevTool On Your Selected 
        Browser (Works Great On PC).
        ------------------------------------------------------------------------
        +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +
        ========================================================================
        Notes Before You Run This Script:
        ========================================================================
            - This May Cause DOS Attack On Your Target.
                So Please Only Use This On Phishing Sites NOT On Any Legit Sites
                Like Google And Facebook.
            - This Can Cause Lag On Your Device While It Is Running.
                Make Sure Your Phone Has Atleast 2GB 
                So This Script Will Not Cause Lags On Your Device
            - This Tool Can Be Tricky To Non Geek Peoples.
            - If You Have Discovered Some Bug, Please Try To Report It On Us.
            - Want To Suggest A Feature On This Script?
                Feel Free To Suggest It On My Github Repo Or Go To Our FB Group
            - I Am Not Responsible For Any Lawsuits Against Third Party Users 
            Using This Tool Too Far From What I Intended Purpose.
                As A User Of My Script, Please Please Please...
                Atleast Know Your Limit.
            - This Tool Is Created To Spam Phishing Links... 
            So Basically, I Made This To Annoy Bad Hackers :)
            - Download All Required Modules For This Script To Run
                (Like: Threading, Requests, Random And Time)
        ------------------------------------------------------------------------
        \n""")
        print(f"{Fore.BLUE}[*]{Fore.RED} Exiting Script...{Fore.RESET} \n")
        exit()
    elif select == "0" or select == "00":
        print(f"{Fore.CYAN}[-]{Fore.BLUE} Thank You For Using My Script :)")
        print(f"{Fore.BLUE}[*]{Fore.RED} Exiting Script...{Fore.RESET} \n")
        exit()
    else:
        print(f'{Fore.RED}[X] {select}{Fore.RESET} Is Not On The List, Please Try Again.')
        print(f"{Fore.BLUE}[*]{Fore.RED} Exiting Script...{Fore.RESET} \n")
        exit()
except KeyboardInterrupt:
    end = humanize.precisedelta(start_time - datetime.datetime.now(), minimum_unit='seconds')
    print(f"\n{Fore.BLUE}=============== INFO SPAM Phising ===============")
    print(f"{Fore.CYAN}[+] Success: {Fore.RESET}{success}")
    print(f"{Fore.RED}[X] Failed: {Fore.RESET}{failed}")
    print(f"{Fore.GREEN}[*] Execute Time: {Fore.RESET} {end}")
    print(f"{Fore.BLUE}================================================= \n{Fore.RESET}")
    exit()