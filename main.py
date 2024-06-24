import os
import json
from PIL import Image, ImageDraw

image_folder = "data/images"
json_folder = "data/json"

output_mask = "output/output_mask"
output_images = "output/output_images"

os.makedirs(output_mask, exist_ok=True)
os.makedirs(output_images, exist_ok=True)

for filename in os.listdir(image_folder):
    if filename.endswith(".bmp"):
        image_path = os.path.join(image_folder, filename)
        json_path = os.path.join(json_folder, os.path.splitext(filename)[0] + ".json")

        print(image_path)
        print(json_path)

        image = Image.open(image_path)

        with open(json_path, "r") as f:
            data = json.load(f)

        mask = Image.new("L", image.size, 0)
        draw = ImageDraw.Draw(mask)

        for annotation in data["shapes"]:
            points = [tuple(point) for point in annotation["points"]]
            draw.polygon(points, outline=255, fill=255)

        output_path = os.path.join(output_mask, os.path.splitext(filename)[0] + ".png")
        mask.save(output_path)

        output_image_path = os.path.join(
            output_images, os.path.splitext(filename)[0] + ".png"
        )
        image.save(output_image_path)

        print(f"Done: {filename}")
