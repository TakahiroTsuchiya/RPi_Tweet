# coding: utf-8
import datetime
import json
from requests_oauthlib import OAuth1Session

CONSUMER_KEY      = ""
CONSUMER_SECRET   = ""
ACCESS_KEY      = ""
ACCESS_SECRET   = ""

URL_MEDIA = "https://upload.twitter.com/1.1/media/upload.json"
URL_TEXT = "https://api.twitter.com/1.1/statuses/update.json"

text = '{0:%Y/%m/%d %H:%M:%S}'.format(datetime.datetime.now())

twitter = OAuth1Session(CONSUMER_KEY,CONSUMER_SECRET, ACCESS_KEY,ACCESS_SECRET)

files = {"media" : open('preview.jpg', 'rb')}

req_media = twitter.post(URL_MEDIA, files = files)
# レスポンスを確認
if req_media.status_code != 200:
#    print ("画像アップデート失敗: %s", req_media.text)
    exit()
# Media ID を取得
media_id = json.loads(req_media.text)['media_id']
#print ("Media ID: %d" % media_id)

# Media ID を付加してテキストを投稿
params = {'status': text, "media_ids": [media_id]}
req_media = twitter.post(URL_TEXT, params = params)
# 再びレスポンスを確認
if req_media.status_code != 200:
#    print ("テキストアップデート失敗: %s", req_text.text)
    exit()

#    print ("OK")

exit()
