
import os,platform
while True:
    try:
        import selenium
        break
    except ImportError: 
        if platform.system() == 'Windows': 
            os.system('pip install selenium')
            os.system('pip install --upgrade selenium')
        else:
            input('Thư Viện Khá Là Nặng Mọi Người Cân Nhắc Dung Lượng Khi Cài Vài Cái Khá Lâu Nhé! Enter Để Tiếp Tục')            
            os.system('pip install selenium==4.9.1')
            os.system('yes | pkg install x11-repo -y')
            os.system('yes | pkg install tur-repo -y')
            os.system('yes | pkg install chromium -y')
            os.system('pip install --upgrade selenium')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import requests,os,json, random,platform
from time import sleep
from datetime import datetime
class Golike:
    def __init__(self, token):
        self.session = requests.Session()
        self.token = token
        self.headers = {'t': 'VFZSamQwMXFSWHBOVkdzMVRrRTlQUT09','authority': 'gateway.golike.net','accept': 'application/json, text/plain, */*','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','authorization': self.token,'content-type': 'application/json;charset=utf-8','sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',}
        info = self.session.get('https://gateway.golike.net/api/users/me',headers=self.headers).json()
        self.name = info['data']['name']
        self.users = info['data']['username']
        self.coin = info['data']['coin']
    def info(self):
        return self.name,self.users,self.coin
    def cauhinh(self):
        try:
            return True, self.session.get('https://gateway.golike.net/api/tiktok-account',headers=self.headers).json()['data']
        except: return False, []
    def getjob(self,account_id):
        try:
            return True, self.session.get('https://gateway.golike.net/api/advertising/publishers/tiktok/jobs?account_id={}&data=null'.format(account_id),headers=self.headers).json()
        except: return False, []
    def nhanxu(self,ads_id,account_id,content=None,comment_id=None):
        try:
            json_data = {'ads_id': ads_id,'account_id': account_id,'async': True,'data': None,'captcha_token': '','captcha': 'recaptcha', 'message': content, 'comment_id': comment_id}
            response = self.session.post('https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',headers=self.headers,json=json_data).json()
            if response['status'] == 200:
                return True, response['data']['prices']
            return False, 0
        except: return False, 0
    def report(self,ads_id: int,object_id: str,account_id: int,type: str):
        try:
            json_data = {'ads_id': ads_id,'object_id': object_id,'account_id': account_id,'type': type,}
            response = self.session.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',headers=self.headers,json=json_data).json()
            if response['status'] == 200:
                return True
            return False
        except: return False
        
class Tiktok:
    def __init__(self,cookie):
        self.cookie = cookie
        self.chromeoptions=webdriver.ChromeOptions()
        self.chromeoptions.add_argument("--window-size=580,800")
        self.chromeoptions.add_argument('--lang=en')
        self.chromeoptions.add_argument('--disable-gpu')
        self.chromeoptions.add_argument('--log-level=3')
        self.chromeoptions.add_argument("--mute-audio")
        self.chromeoptions.add_argument('--disable-blink-features=AutomationControlled')
        self.chromeoptions.add_argument('--disable-blink-features=AutomationControlled')
        self.chromeoptions.add_argument("--no-sandbox")
        self.chromeoptions.add_argument("--disable-dev-shm-usage")
        if platform.system() == 'Windows':pass 
        else:self.chromeoptions.add_argument("--headless=new")
        self.chromeoptions.add_argument('--disable-blink-features=AutomationControlled')
        self.chromeoptions.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.chromeoptions.add_experimental_option('excludeSwitches', ['enable-logging'])
        prefs = {
            "profile.default_content_setting_values.notifications" : 2,
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
        while(True):
            win = random.randint(7,11)
            if win != 9:
                break
        #self.chromeoptions.add_argument(f'--user-agent=Mozilla/5.0 (Windows NT {win}.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(85, 102)}.0.4844.82 Safari/537.36')
        self.chromeoptions.add_experimental_option('useAutomationExtension', False)
        self.chromeoptions.add_argument('--disable-blink-features=AutomationControlled')
        self.chromeoptions.add_experimental_option("prefs",prefs)
        self.driver = webdriver.Chrome(options=self.chromeoptions)
        self.driver.get("https://www.tiktok.com")
    def outchrome(self):
        self.driver.close()
    def info(self):
        return self.driver.page_source.split('uniqueId":"')[1].split('"')[0]
    def login(self):
        cookie = self.cookie
        cookiett = ''
        for x in ['msToken', 'multi_sids', 'odin_tt', 'passport_csrf_token_default', 'sid_guard', 'ssid_ucp_v1', 'uid_tt', 'tt_chain_token', 'sid_ucp_v1', 'tt-target-idc-sign', 'sessionid_ss', 'sid_tt', 'uid_tt_ss', 'sessionid', 'store-country-code', 'cmpl_token', 'passport_csrf_token', 'tt-target-idc', 'ttwid', 'store-idc', 'tt_csrf_token', 'store-country-code-src']:
            cookiett += f'{x}='+cookie.split(f'{x}=')[1].split(';')[0]+';'
        cookie = cookiett.replace(" ", "").split(';')
        for i in cookie:
            if i != "":
                ck = i.split("=")
                self.driver.add_cookie({"name":ck[0],"value":ck[1],"domain":".tiktok.com"})
        self.driver.refresh()
        sleep(3)
    def follow(self,link):
        try:
            self.driver.get(link)
            sleep(10)
            self.driver.find_element(By.XPATH, '//*[@id="main-content-others_homepage"]/div/div[1]/div[1]/div[2]/div/div[1]/button').click()
        except:pass
    def like(self,link):
        try:
            self.driver.get(link)
            sleep(10)
            self.driver.find_element(By.XPATH, '//*[@id="main-content-video_detail"]/div/div[2]/div/div[1]/div[1]/div[4]/div/button[1]').click()
        except:pass
    def comment(self,link,content):
        try:
            self.driver.get(link)
            sleep(10)
            comment = self.driver.find_element(By.CSS_SELECTOR,'#main-content-video_detail > div > div.css-12kupwv-DivContentContainer.ege8lhx2 > div > div.css-x4xlc7-DivCommentContainer.e1a7v7ak0 > div.css-1bg47i4-DivCommentBarContainer.e1a7v7ak2 > div > div > div.css-1vplah5-DivLayoutContainer.e1rzzhjk1 > div > div.css-4p7h1x-DivInputEditorContainer.e1rzzhjk3 > div > div > div.DraftEditor-editorContainer > div')
            comment.send_keys(content)
            comment.send_keys(Keys.ENTER)
        except:pass

        
        
def addcookie(settingmenu):
    while True:
        cookie = input(toaidz+luc+f'Nhập Cookie Tiktok {luc}: {vang}')
        try:
            print(f' {luc}Đang Đăng Nhập Tiktok    ',end='\r')
            tiktok = Tiktok(cookie)
            tiktok.login()
            info = tiktok.info()
            tiktok.outchrome()
            print('{} Id Tiktok: {}{}'.format(luc,vang,info));print(thanhngang)
            listCookie.append(cookie)
            return
        except Exception as s:
            print('{} Cookie Tiktok Die ! Vui Lòng Xem Lại Đã Thêm Tk Tiktok Vào Golike chưa !!!'.format(do)); print(thanhngang)
            try: tiktok.outchrome()
            except:pass
listCookie = []
toaidz = '\033[1;31m[\033[1;37m<\>\033[1;31m] \033[1;37m=> '
vang = '\033[1;33m'
trang = '\033[1;37m'
luc = '\033[1;32m'
do = '\033[1;31m'
xanh = '\033[1;96m'
thanhngang = '\033[1;37m'+'- '*32
settingmenu = toaidz, vang, trang, luc, do, xanh, thanhngang
def logo():
			os.system('cls' if os.name == 'nt' else 'clear')
			print("""
        \033[1;32m © Tool Auto Golike Tiktok  New
        
\033[1;31m ██████╗ ██╗   ██╗██╗   ██╗██╗  ██╗██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗
\033[1;36m ██╔══██╗██║   ██║╚██╗ ██╔╝██║ ██╔╝██║  ██║██╔══██╗████╗  ██║██║  ██║
\033[1;32m ██║  ██║██║   ██║ ╚████╔╝ █████╔╝ ███████║███████║██╔██╗ ██║███████║
\033[1;34m ██║  ██║██║   ██║  ╚██╔╝  ██╔═██╗ ██╔══██║██╔══██║██║╚██╗██║██╔══██║
\033[1;35m ██████╔╝╚██████╔╝   ██║   ██║  ██╗██║  ██║██║  ██║██║ ╚████║██║  ██║
\033[1;31m ╚═════╝  ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
 
               BOX ZALO: https://zalo.me/g/nguadz335
               ADMIN : DUY KHÁNH 
               YTB : REVIEWTOOL247NDK""")
			print('\033[1;37m'+'- '*32)
def dlow_delay(x:int):
    while x > 0:
        sec = x % 60
        min = int(x / 60) % 60
        hou = int(x / 3600)
        print(f' \033[1;37m[\033[1;96mREVIEWTOOL\033[1;37m] \033[1;37m[\033[1;96mDELAY\033[1;37m] \033[1;37m[\033[1;96m{hou:02}:{min:02}:{sec:02}\033[1;37m] \033[1;37m[\033[1;33mXXXXX\033[1;37m]','          ', end="\r");sleep(1/14)
        print(f' \033[1;37m[\033[1;96mREVIEWTOOL\033[1;37m] \033[1;37m[\033[1;96mDELAY\033[1;37m] \033[1;37m[\033[1;96m{hou:02}:{min:02}:{sec:02}\033[1;37m] \033[1;37m[\033[1;33mX.X.X\033[1;37m]','          ', end="\r");sleep(1/14)
        print(f' \033[1;37m[\033[1;96mREVIEWTOOL\033[1;37m] \033[1;37m[\033[1;96mDELAY\033[1;37m] \033[1;37m[\033[1;96m{hou:02}:{min:02}:{sec:02}\033[1;37m] \033[1;37m[\033[1;33m.X.X.\033[1;37m]','          ', end="\r");sleep(1/14)
        print(f' \033[1;37m[\033[1;96mREVIEWTOOL\033[1;37m] \033[1;37m[\033[1;96mDELAY\033[1;37m] \033[1;37m[\033[1;96m{hou:02}:{min:02}:{sec:02}\033[1;37m] \033[1;37m[\033[1;33mX...X\033[1;37m]','          ', end="\r");sleep(1/14)
        print(f' \033[1;37m[\033[1;96mREVIEWTOOL\033[1;37m] \033[1;37m[\033[1;96mDELAY\033[1;37m] \033[1;37m[\033[1;96m{hou:02}:{min:02}:{sec:02}\033[1;37m] \033[1;37m[\033[1;33mX....\033[1;37m]','          ', end="\r");sleep(1/14)
        print(f' \033[1;37m[\033[1;96mREVIEWTOOL\033[1;37m] \033[1;37m[\033[1;96mDELAY\033[1;37m] \033[1;37m[\033[1;96m{hou:02}:{min:02}:{sec:02}\033[1;37m] \033[1;37m[\033[1;33m.X...\033[1;37m]','          ', end="\r");sleep(1/14)
        print(f' \033[1;37m[\033[1;96mREVIEWTOOL\033[1;37m] \033[1;37m[\033[1;96mDELAY\033[1;37m] \033[1;37m[\033[1;96m{hou:02}:{min:02}:{sec:02}\033[1;37m] \033[1;37m[\033[1;33m..X..\033[1;37m]','          ', end="\r");sleep(1/14)
        print(f' \033[1;37m[\033[1;96mREVIEWTOOL\033[1;37m] \033[1;37m[\033[1;96mDELAY\033[1;37m] \033[1;37m[\033[1;96m{hou:02}:{min:02}:{sec:02}\033[1;37m] \033[1;37m[\033[1;33m...X.\033[1;37m]','          ', end="\r");sleep(1/14)
        print(f' \033[1;37m[\033[1;96mREVIEWTOOL\033[1;37m] \033[1;37m[\033[1;96mDELAY\033[1;37m] \033[1;37m[\033[1;96m{hou:02}:{min:02}:{sec:02}\033[1;37m] \033[1;37m[\033[1;33m....X\033[1;37m]','          ', end="\r");sleep(1/14)
        print(f' \033[1;37m[\033[1;96mREVIEWTOOL\033[1;37m] \033[1;37m[\033[1;96mDELAY\033[1;37m] \033[1;37m[\033[1;96m{hou:02}:{min:02}:{sec:02}\033[1;37m] \033[1;37m[\033[1;33m...X.\033[1;37m]','          ', end="\r");sleep(1/14)
        print(f' \033[1;37m[\033[1;96mREVIEWTOOL\033[1;37m] \033[1;37m[\033[1;96mDELAY\033[1;37m] \033[1;37m[\033[1;96m{hou:02}:{min:02}:{sec:02}\033[1;37m] \033[1;37m[\033[1;33m..X..\033[1;37m]','          ', end="\r");sleep(1/14)
        print(f' \033[1;37m[\033[1;96mREVIEWTOOL\033[1;37m] \033[1;37m[\033[1;96mDELAY\033[1;37m] \033[1;37m[\033[1;96m{hou:02}:{min:02}:{sec:02}\033[1;37m] \033[1;37m[\033[1;33m.X...\033[1;37m]','          ', end="\r");sleep(1/14)
        print(f' \033[1;37m[\033[1;96mREVIEWTOOL\033[1;37m] \033[1;37m[\033[1;96mDELAY\033[1;37m] \033[1;37m[\033[1;96m{hou:02}:{min:02}:{sec:02}\033[1;37m] \033[1;37m[\033[1;33mX....\033[1;37m]','          ', end="\r");sleep(1/14)
        print(f' \033[1;37m[\033[1;96mREVIEWTOOL\033[1;37m] \033[1;37m[\033[1;96mDELAY\033[1;37m] \033[1;37m[\033[1;96m{hou:02}:{min:02}:{sec:02}\033[1;37m] \033[1;37m[\033[1;33mXXXXX\033[1;37m]','          ', end="\r");sleep(1/14)
        x = x - 1
    print(f' \033[1;37m              REVIEWTOOL                ',end="\r")
logo()

if os.path.exists(f'HoangTool-authorizationgolike.json') == False:
    while(True):
        token = input(toaidz+luc+'Nhập Authorization Golike:'+vang+' ')
        print(' \033[1;32mĐang Xữ Lý...','     ',end='\r')
        try:
            golike = Golike(token)
            info = golike.info()
            name,users,coin = info[0],info[1],info[2]
            print(luc+'Đăng Nhập Thành Công') 
            with open('HoangTool-authorizationgolike.json','w') as f: json.dump([token+'|'+users+' - '+ name],f);break
        except: print(do+'Đăng Nhập Thất Bại')
else:
    token_json = json.loads(open('HoangTool-authorizationgolike.json','r').read())
    stt_token = 0
    for tokens in token_json:
        if len(tokens) > 5: stt_token += 1; print('{}{}Account {}[{}{}{}] {}Để Chạy Tài Khoản: {}{}'.format(toaidz,luc,do,vang,stt_token,do,luc,vang,tokens.split('|')[1]))
    print(thanhngang)
    print('{}{}Nhập {}[{}{}{}] {}Chọn Acc Golike Để Chạy Tool'.format(toaidz,luc,do,vang,'1',do,luc))
    print('{}{}Nhập {}[{}{}{}] {}Nhập Authorization Golike Mới'.format(toaidz,luc,do,vang,'2',do,luc))
    print(thanhngang)
    while True:
        type_  = input(F'{toaidz}{luc}Nhập: {vang}')
        print(thanhngang)
        if type_ == '1':
            while True:
                try:
                    tokenauthorizationgolikegolike = int(input(f'{toaidz}{luc}Nhập Số Acc: {vang}'))
                    print(thanhngang)
                    golike = Golike(token_json[tokenauthorizationgolikegolike - 1].split("|")[0])
                    info = golike.info()
                    name,users,coin = info[0],info[1],info[2]
                    print(luc+'Đăng Nhập Thành Công');break
                except Exception as s: print('{} Số Acc Không Tồn Tại'.format(do))
            break
        elif type_ == '2':
            while(True):
                token = input(toaidz+luc+'Nhập Authorization Golike:'+vang+' ')
                print(' \033[1;32mĐang Xữ Lý...','     ',end='\r')
                try:
                    golike = Golike(token)
                    info = golike.info()
                    name,users,coin = info[0],info[1],info[2]
                    print(luc+'Đăng Nhập Thành Công') 
                    token_json.append(token+'|'+users+' - '+ name)
                    with open('LQTOAI-authorizationgolike.json','w') as f: json.dump(token_json,f);break
                except: print(do+'Đăng Nhập Thất Bại')
            break
        else: print('{} Vui Long Nhập Chính Xác '.format(do))
logo()

if os.path.exists(f'HoangTool-cookietiktok-golike.json') == False:
    cookie = addcookie(settingmenu)
    with open('HoangTool-cookietiktok-golike.json','w') as f: json.dump(listCookie, f)
else:
    print('{}{}Nhập {}[{}{}{}] {}Sử Dụng Cookie Tik Tok Đã Lưu'.format(toaidz,luc,do,vang,'1',do,luc))
    print('{}{}Nhập {}[{}{}{}] {}Nhập Cookie Tik Tok Mới '.format(toaidz,luc,do,vang,'2',do,luc))
    print(thanhngang)
    type_ = input('{}{}Nhập: {}'.format(toaidz,luc,vang)); print(thanhngang)
    while True:
        if type_ == '1': print(f'{luc} Đang Lấy Dữ Liệu Đã Lưu ','          ',end='\r'); sleep(1); listCookie = json.loads(open('LQTOAI-cookietiktok-golike.json', 'r').read());break
        elif type_ == '2': 
            addcookie(settingmenu)
            with open('HoangTool-cookietiktok-golike.json','w') as f: json.dump(listCookie, f)
            break 
        else: print('{} Vui Lòng Nhập Đúng !!!'.format(do))
logo()

print(toaidz+luc+f'Họ Và Tên: {vang}{name}')
print(toaidz+luc+f'Tên Tài Khoản: {vang}{users}')
print(toaidz+luc+f'Số Dư: {vang}{str(coin)}')
print(thanhngang)
while(True):
    try:delay = int(input(toaidz+luc+'Delay Tool:'+vang+' ')); break
    except:print(do+' Vui Lòng Nhập Số')
while(True):
    try:DelayBlock = int(input(toaidz+luc+'Sau Khi Phát Hiện Block Thì Nghỉ Bao Nhiêu Giây:'+vang+' ')); break
    except:print(do+' Vui Lòng Nhập Số')
print(thanhngang)
stt = 0
jobfail = 0
total = 0
while True:
    if len(listCookie) == 0:
        print('{} Đã Xóa Tất Cả Cookie, Vui Lòng Nhập Lại !!!'.format(do))
        addcookie(settingmenu)
        with open('HoangTool-cookietiktok-golike.json','w') as f: json.dump(listCookie, f)
    for cookie in listCookie:
        try:
            tiktok = Tiktok(cookie)
            tiktok.login()
            info = tiktok.info()
            account_id = ""
            for x in golike.cauhinh()[1]:
                if x['unique_username'] == info:
                    account_id = x['id']
                    break
            if account_id != "": print(luc+'Id Tiktok:',vang+info)
            else: print(luc+'Id Tiktok:',vang+info,do+' ❤️😍'); break
        except: 
            print('{} Cookie Tiktok Die ! Đã Xóa Ra Khỏi List !!!'.format(do))
            try:tiktok.outchrome()
            except:pass
            listCookie.remove(cookie); break
        print(luc+'Delay Check Acc...',end='\r');sleep(1.5)
        dlow_delay(30)
        while True:
            try:
                getjob = golike.getjob(account_id)
                if len(getjob[1]) != 0 and getjob[0] and getjob[1] != [] and getjob[1]['error'] == []:
                    thongtin = getjob[1]
                    id = thongtin['data']['id']
                    object_id = thongtin['data']['object_id']
                    package_name = thongtin['data']['package_name']
                    message = thongtin['lock']['message']
                    comment_id = thongtin['lock']['comment_id']
                    print(luc+f" Đã Tìm Thấy Nhiệm Vụ {package_name.title()}           ",end = "\r")
                    if package_name == 'follow': tiktok.follow(thongtin['data']['link'])
                    if package_name == 'like-tim-thuongthuong-buon-haha-phanno': tiktok.like(thongtin['data']['link'])
                    if package_name == 'comment':tiktok.comment(thongtin['data']['link'], message)
                    dlow_delay(delay)
                    nhanjob = golike.nhanxu(id,account_id,message,comment_id)
                    if nhanjob[0]:
                        timejob = datetime.now().strftime('%H:%M:%S')
                        stt += 1
                        jobfail = 0
                        total += int(nhanjob[1])
                        print(f"{vang}{stt}{do} | {xanh}{timejob}{do} | {luc}SUCCESS{do} | {vang}{package_name.upper()}{do} | {trang}{object_id}{do} | {vang}+{nhanjob[1]}{do} | {vang}{str(total)}")	
                    else:
                        huyjob = golike.report(id,object_id,account_id,package_name)
                        jobfail += 1
                        timejob = datetime.now().strftime('%H:%M:%S')
                        if huyjob:print(f"{vang}@{do} | {xanh}{timejob}{do} | {do}FAIL{do} | {vang}{package_name.upper()}{do} | {trang}{object_id}{do} |{luc} Hủy Job Thành Công")
                        else: print(f"{vang}@{do} | {xanh}{timejob}{do} | {do}FAIL{do} | {vang}{package_name.upper()}{do} | {trang}{object_id}{do} |{do} Hủy Job Thất Bại")
                    if int(jobfail) % 5 == 0 and jobfail != 0: dlow_delay(DelayBlock)
                else: print(do+f' Đã Hết Nhiệm Vụ.                ',end="\r"); sleep(1); dlow_delay(5)
            except Exception as s: print(do+' Vui Lòng Xem Lại Mạng!!!!!          ',' ', end="\r")