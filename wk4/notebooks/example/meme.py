
import requests 
from PIL import Image
from io import StringIO
from io import BytesIO
from secrets import USERNAME, PASSWORD

def get_meme_url():

    url = "https://api.imgflip.com/caption_image"
    payload = {"template_id":61579,
            "username":USERNAME,
            "password":PASSWORD,
            "text0":"One does not simply",
            "text1":"Hand-code a POST request",
            }

    r = requests.get(url, params=payload)
    r = r.json()
    img_url = r['data']['url']

    return img_url

def save_pic(pic_url):
    r = requests.get(pic_url)
    with open('meme.jpeg', 'w') as f:
        f.write(r.content)



    
if __name__ == "__main__":
    save_pic(get_meme_url())

