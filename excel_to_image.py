import os
from datetime import datetime
from typing import List
import excel2img


def excel_to_images(file, sheets: List, image_format):
    for sheet in sheets:
        excel2img.export_img(file, f"{datetime.now().strftime(image_format)}.png", sheet, None)


def apply_function_to_files(function, directory, file_extension):
    os.chdir(directory)
    file_names = sorted(os.listdir(directory))
    for file_name in file_names:
        if file_name.endswith(file_extension):
            function(file_name, ['FC1', 'FC2'], "%Y-%m-%d-%H-%M-%f")


directory = r'C:\Users\a1056968\Desktop\New folder'
apply_function_to_files(excel_to_images, directory, '.xlsx')
