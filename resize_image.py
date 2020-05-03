from PIL import Image

import os

for filename in os.listdir("test"):
    if not(filename.endswith("png") or filename.endswith("jpg") or filename.endswith("jpeg")):
        continue
    print("file :" + filename)

    image = Image.open(os.path.join("test", filename))
    width = image.size[0]
    height = image.size[1]

    aspect = width / float(height)

    ideal_height = 200
    ideal_width = 380

    ideal_aspect = ideal_width / float(ideal_height)

    thumb = image.resize((ideal_width, ideal_height), Image.ANTIALIAS)
    thumb.save('output/'+filename)
