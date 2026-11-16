import os
from dotenv import load_dotenv
import requests
import base64
from PIL import Image

load_dotenv()

api_token = os.getenv("CLOUDFLARE_API_TOKEN")
account_id = os.getenv("CLOUDFLARE_ACCOUNT_ID")

url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/@cf/black-forest-labs/flux-1-schnell"

headers = {
    "Authorization" : f"Bearer {api_token}"
}

print("Görsel üretimi başlıyor...")

def generate_image(prompt):
    try:
        response = requests.post(
            url,
            headers=headers,
            json={"prompt":prompt,
                  "steps":8},
            timeout=180)

        response.raise_for_status()
        result=response.json()

        if result["success"]:
            image_base64 = result["result"]["image"]
            image_bytes = base64.b64decode(image_base64)

            with open("uretilen_gorsel3.png","wb") as file:
                file.write(image_bytes)

                print("Görsel başarıyla oluşturuldu...")

                image = Image.open("uretilen_gorsel3.png")
                print("Görselin orijinal boyutu: " , image.size)

                image.thumbnail((512,512))

                image.save("new_size.png")
                print("Yeni boyut: ", image.size)

                cropped_image= image.crop((200,200,800,800))
                cropped_image.save("cropped_image.png")
                cropped_image.show()

                image = image.convert("RGB")
                image.save("convert_image.jpg", quality=90)
        else:
            print("API hatası: ",result["errors"])    

    except requests.exceptions.Timeout:
        print("İstek zaman aşımına uğradı")

    except requests.exceptions.RequestException as e:
        print("Bağlantı veya HTTP hatası ", e)


    except (ValueError, KeyError) as e:
        print("API yanıtı işlenemedi", e)

metin= """
A small female calico kitten peacefully sleeping
on a wooden garden table under an apple tree. Please take the shot at eye level.

The scene takes place in a beautiful 25-square-meter
private garden on a sunny afternoon.

The garden is surrounded by a wooden fence.
It contains daisies, lilies, roses and geraniums.

The apple tree is located in the back-right corner
of the garden. A wooden table is placed beneath it.

The kitten is lying comfortably on top of the table.

Warm golden hour sunlight,
soft natural shadows

Photorealistic photography,
wide-angle garden composition.

The kitten is the main subject of the image.

"""        

generate_image(metin)       