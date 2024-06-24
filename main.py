import os
import json
from argparse import ArgumentParser
from PIL import Image, ImageDraw


image_folder_list = ["data/gt_back_cropped_1/test", "data/gt_back_cropped_2/test", "data/gt_back_cropped_3/test", "data/gt_back_cropped_4/test", "data/gt_back_cropped_5/test", "data/gt_back_cropped_6/test", "data/gt_back_cropped_7/test", "data/gt_back_cropped_8/test", "data/gt_front_cropped_1/test", "data/gt_front_cropped_2/test", "data/gt_front_cropped_3/test"]
json_folder_list = ["data/gt_back_cropped_1/test/json", "data/gt_back_cropped_2/test/json", "data/gt_back_cropped_3/test/json", "data/gt_back_cropped_4/test/json", "data/gt_back_cropped_5/test/json", "data/gt_back_cropped_6/test/json", "data/gt_back_cropped_7/test/json", "data/gt_back_cropped_8/test/json", "data/gt_front_cropped_1/test/json", "data/gt_front_cropped_2/test/json", "data/gt_front_cropped_3/test/json"]

for image_folder, json_folder in zip(image_folder_list, json_folder_list):
    output_mask = f"output/{image_folder.split('/')[1]}/mask"
    output_images = f"output/{image_folder.split('/')[1]}/images"

    # os.makedirs(output_mask, exist_ok=True)
    # os.makedirs(output_images, exist_ok=True)

    image_list = os.listdir(image_folder)
    # json_list = os.listdir(json_folder)

    # print("===============================================")
    # print(f"Image folder: {image_folder}")
    # print(f"Image folder: {image_list}")
    # print("===============================================")
    # print("===============================================")
    # print(f"JSON folder: {json_folder}")
    # print(f"JSON folder: {json_list}")


    for filename in image_list:
        if filename.endswith(".jpg"):
            image_path = os.path.join(image_folder, filename)
            json_path = os.path.join(json_folder, os.path.splitext(filename)[0] + ".json")

            print(image_path)
            print(json_path)

            image = Image.open(image_path)

            if filename[0] == "n":
                output_image_path = os.path.join(
                output_images, os.path.splitext(filename)[0] + ".png"
            )
                image.save(output_image_path)

            else:
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
