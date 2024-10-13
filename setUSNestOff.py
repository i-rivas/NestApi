import requests
import json

refreshToken = '1//0fIjlc_bhGmfaCgYIARAAGA8SNwF-L9Ir5JqyHsnHQyAhtOPYFWIo8rkoPQLK3EayXuj8VZOtpfo4GFnqAvSo-FnW5fwjRwgtadg'

refreshTokenResource = requests.post(f"""https://www.googleapis.com/oauth2/v4/token?client_id=1068820101263-o6i0m3icec7vr8mkqae59kgqv67gmngb.apps.googleusercontent.com&client_secret=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&refresh_token={refreshToken}&grant_type=refresh_token""")


access_token_responce = refreshTokenResource.json()
access_token = access_token_responce['access_token']

def setToOff():
    tempResourceURL = 'https://smartdevicemanagement.googleapis.com/v1/enterprises/ca897a23-d921-4f36-b195-25a54b963851/devices/AVPHwEt6uhfH1cfKdW39jJSxLHZknGOZBOA47FmQZ-I8En7koK_RiSbBaVAe79Bg5kU5NzBsqvxrxu7ProObqx1dy-Ie2w:executeCommand'
    headers = {'Content-Type':'application/json', 'Authorization':f'Bearer {access_token}'}
    requestBody = {'command':'sdm.devices.commands.ThermostatMode.SetMode', 'params':{'mode': 'OFF'}}
    setCoolTemp = requests.post(url=tempResourceURL, headers=headers, json=requestBody)

setToOff()