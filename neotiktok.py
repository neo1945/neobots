try:
  import telebot
  from telebot import types
  import requests,json
  d
except:
  import os
  os.system("pip install pyTelegramBotAPI")
  os.system("pip install requests")


token = "8175972415:AAFi2IzmVeK9hvFIdczFIljp8cahSwfCMk8"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
  name = message.from_user.first_name
  my = types.InlineKeyboardButton(text='چەنال',url="t.me/toolsneo")
  xx = types.InlineKeyboardMarkup()
  xx.add(my)
  bot.reply_to(message,f'بەخێربێت بۆ بۆتی زانیاری تیکتۆک ئەم بۆتە لەلایان @OVR07دروست کراوە تکایە یوسەری کەسەکە بنوسە بەم شێوەیە @neo',reply_markup=xx)
@bot.message_handler(func=lambda m:True)
def r(message):
  xr = types.InlineKeyboardMarkup()
  my = types.InlineKeyboardButton(text='چەناڵ',url="t.me/toolsneo")
  acc = types.InlineKeyboardButton(text='کردنەوە ',url='https://tiktok.com/@'+message.text)
  xr.row(acc,my)

  username = message.text
  ur = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser"
  dat = {'key': "AIzaSyAZqmylIOE4fQmf0pemugc2iBH33rSeMkg"}

  dataa = json.dumps({"returnSecureToken": True})
  he = {'User-Agent': "okhttp/3.12.1",
'Accept-Encoding': "gzip",
'Content-Type': "application/json",
'x-client-version': "ReactNative/JsCore/7.8.1/FirebaseCore-web"}
  res = requests.post(ur, params=dat, data=dataa, headers=he)
  res.raise_for_status()
  rre = res.json()
  token = rre.get("idToken")
  url = "https://us-central1-tikfans-prod-a3557.cloudfunctions.net/getTikTokUserInfo"
  data = json.dumps({"data": {"username": username}})
  he = {'User-Agent': "okhttp/3.12.1",
'Accept-Encoding': "gzip",
'Content-Type': "application/json",
'authorization': f"Bearer {token}"}
  re = requests.post(url, data=data, headers=he)
  re.raise_for_status()      
  data = re.json()
  r = json.dumps(data, indent=4, ensure_ascii=False)
  ff = f"{data['result']['coversMedium'][0]}"

  usse = (f"Username: {data['result']['uniqueId']}\n"
f"User ID: {data['result']['userId']}\n"
f"Nickname: {data['result']['nickName']}\n"
f"Following: {data['result']['following']}\n"
f"Fans: {data['result']['fans']}\n"
f"Videos: {data['result']['video']}\n"
f"Signature: {data['result']['signature']}\n"
f"Hearts: {data['result']['heart']}\n"
f"Digg: {data['result']['digg']}\n"
f"Secret Account: {data['result']['isSecret']}\n"
f"SecUID: {data['result']['secUid']}\n"
f"Open Favorite: {data['result']['openFavorite']}");bot.send_photo(message.chat.id, ff, caption=f"{usse}",reply_markup=xr)

bot.infinity_polling()

