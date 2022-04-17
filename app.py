# pip install colorama 
# pip install Faker
# sudo apt install Faker
# sd._sttri   sadra_sattari
from colorama import  Fore , init
from faker import  Faker
import  os 
import time
init()
print(Fore.LIGHTGREEN_EX + """
                   ...                                 ..                                                
          .Y#&&@@: ?PPPPGPY:                  :5#&&@& .GGGGGGGG7.GGGGGGGG7 YP555J!:   !#BBG         
         .&@@@@&#: B@@@BG@@@7                :&@@@@&B :@@@@@@@@P^@@@@@@@@P &@@@##@@B  J@@@@.        
         ^@@@@Y    G@@@J^@@@&                ?@@@@7   .G#@@@@BG?.G#@@@@BG7 &@@@::@@@: J@@@&         
         .&@@@&G^  G@@@J^@@@@.               :@@@@&P.   :@@@@:    :@@@@.   &@@@B&@@#  J@@@&         
          :B@@@@@! G@@@?~@@@&.                ^#@@@@@:  :@@@@:    :@@@@.   &@@@@@@@^  ?@@@&         
         .  ^&@@@G G@@@?Y@@@B :##&J          .  !@@@@J  :@@@@.    :@@@&.   #@@@Y&@@#. 7@@@&         
         ~@&&@@@@^ G@@@&@@@&: :@@@# .??????^ J@&&@@@&.  :@@@@.    :@@@&    #@@@~:@@@J ~@@@&         
         .B&&&#P:  !GPPGPY!   .&&&B !@@@@@@# :#&&&#Y.   .PGGP     .GGG5    7GP5. ~G^  :#GGY         
                                    ~@&&&&@B                                                        

""" + Fore.RESET)
fake = Faker()
F_name = fake.first_name()
L_name = fake.last_name()
city = fake.city()
street = fake.street_name()
bulding_num = fake.building_number()
email = fake.ascii_email()
phone = fake.msisdn()
contry =  fake.country()
current_contry = fake.current_country()
postcode = fake.postcode()
compony = fake.company()
phone_contry_code = fake.country_calling_code()
credit_expire = fake.credit_card_expire()
credit_number = fake.credit_card_number()
credit_provider  =   fake.credit_card_provider()
credit_pass =  fake.credit_card_security_code()
job = fake.job()
windows = fake.windows_platform_token() 
linux = fake.linux_platform_token()
ios  =  fake.ios_platform_token()
mac =  fake.mac_platform_token()
android = fake.android_platform_token()
print(Fore.GREEN +  " [ + ] " + Fore.YELLOW + "your request was sumbit...! \r\n")
time.sleep(1)
print(Fore.GREEN +  " [ + ] " + Fore.YELLOW + "generate information.... \r\n")
time.sleep(2)
print(Fore.GREEN +  " [ + ] " + Fore.YELLOW + "please wait ... \r\n")
time.sleep(4)
print(Fore.LIGHTYELLOW_EX + """
                    ########################################################################
                                            instagram : sd._sttri       
                    ########################################################################


""")
print(Fore.YELLOW + " [ + ]  first name: " + Fore.CYAN + F_name)
print(Fore.YELLOW + " [ + ]  last name: " + Fore.CYAN + L_name)
print(Fore.YELLOW + " [ + ]  email: " + Fore.CYAN + email)
print(Fore.YELLOW + " [ + ]  phone number: " + Fore.CYAN + phone)
print(Fore.YELLOW + " [ + ]  email: " + Fore.CYAN + phone_contry_code)
print(Fore.YELLOW + " [ + ]  contry: " + Fore.CYAN + contry)
print(Fore.YELLOW + " [ + ]  current contry: " + Fore.CYAN + current_contry)
print(Fore.YELLOW + " [ + ]  city: " + Fore.CYAN + city)
print(Fore.YELLOW + " [ + ]  street: " + Fore.CYAN + street)
print(Fore.YELLOW + " [ + ]  bulding number: " + Fore.CYAN + bulding_num)
print(Fore.YELLOW + " [ + ]  post code: " + Fore.CYAN + postcode)
print(Fore.YELLOW + " [ + ]  compony: " + Fore.CYAN + compony)
print(Fore.YELLOW + " [ + ]  job: " + Fore.CYAN + job)
print(Fore.YELLOW + " [ + ]  credit provider: " + Fore.CYAN + credit_provider)
print(Fore.YELLOW + " [ + ]  credit number: " + Fore.CYAN + credit_number)
print(Fore.YELLOW + " [ + ]  credit expire: " + Fore.CYAN + credit_expire)
print(Fore.YELLOW + " [ + ]  credit password: " + Fore.CYAN + credit_pass)
print(Fore.YELLOW + " [ + ]  windows: " + Fore.CYAN + windows)
print(Fore.YELLOW + " [ + ]  mac version: " + Fore.CYAN + mac)
print(Fore.YELLOW + " [ + ]  ios version: " + Fore.CYAN + ios)
print(Fore.YELLOW + " [ + ]  linux version: " + Fore.CYAN + linux)
os.system("pause")