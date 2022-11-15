from google.colab import files as FILE
import os
import requests
url="https://raw.githubusercontent.com/danielgatis/rembg/master/examples/girl-2.jpg"
img_data = requests.get(url).content
with open('input.jpg', 'wb') as handler:
    handler.write(img_data)
