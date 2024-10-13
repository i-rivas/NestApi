import requests
import json
import pprint

client_id = '1068820101263-o6i0m3icec7vr8mkqae59kgqv67gmngb.apps.googleusercontent.com'

client_secret = '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'

authorization_code = '4/0AVG7fiTLCkB9wVGeW-JloQ7aLfB9WMi5-KhuXGEJa_7HuDalNZpag34cv2l5DPhyFd59ng'


get_code = requests.post(f'https://www.googleapis.com/oauth2/v4/token?client_id={client_id}&client_secret={client_secret}&code={authorization_code}&grant_type=authorization_code&redirect_uri=https://www.google.com')

pprint.pp(get_code)
