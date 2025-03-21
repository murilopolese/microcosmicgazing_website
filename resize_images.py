import glob
from PIL import Image
import shutil

W = int(1024)
# H = int(273)
H = 0

def create_thumbnail(source_path, dest_path):
    with Image.open(source_path) as img:
        if img.mode != "RGB":
            img = img.convert("RGB")

        width = img.size[0]
        height = img.size[1]

        aspect = min(W/width, height/height)

        img.thumbnail((W, height*aspect))
        if '.jpg' in dest_path:
            img.save(dest_path, "JPEG", optimize=True, quality=60)
        if '.png' in dest_path:
            img.save(dest_path, "PNG", optimize=True, quality=60)
        if '.gif' in dest_path:
            shutil.copy(source_path, dest_path)


image_queries = [
    'images_full/*.png'
]

for query in image_queries:
    paths = glob.glob(query)
    print(paths)
    for path in paths:
        p = path.split('/')
        p[0] = 'images'
        new_path = '/'.join(p)
        print('converting', path)
        create_thumbnail(path, new_path)

print("DONE")
