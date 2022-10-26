from pathlib import Path

import pandas as pd
import requests
import numpy as np
from slugify import slugify
from PIL import Image

def download_and_format_image_path(url):
    path = Path(url)
    ref_path = f"images/{slugify(path.stem)}{path.suffix}"
    output_path = f"static/{ref_path}"
    r = requests.get(url)
    with open(output_path, 'wb') as f:
        f.write(r.content)
    reduce_image_size(output_path)
    return ref_path

# function to reduce the size of the image
def reduce_image_size(image_path):
    img = Image.open(image_path)
    img.save(image_path, optimize=True, quality=85)


# Descargo el csv creando un DataFrame
df = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vR-BAUvNUjp2AeV_daeeqHReX0M3ew3ZpEL3nfkrz96uUd816mV_hV1uWMvbsACphEBGjqHJBswGwFz/pub?gid=614465369&single=true&output=csv")

# Creo una columna con el path de la imagen y creo otro csv
df['Portada'] = df['Portada'].replace(np.nan, '', regex=True)
df['Images'] = df['Portada'].apply(lambda x: download_and_format_image_path(x))
df.to_csv("webdata.csv", index=False)


