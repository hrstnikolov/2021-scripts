import os
from datetime import datetime
from typing import List
import excel2img


def excel_to_images(file, sheets, image_format):
    for sheet in sheets:
        try:
            timestamp = datetime.now().strftime(image_format)
            excel2img.export_img(file, f"{timestamp}.png", sheet, None)
        except OSError:
            raise FileNotFoundError(f'No such sheet in {file}.')


def filter_files(directory, extensions):
    filtered_files = []
    file_names = sorted(os.listdir(directory))
    for file_name in file_names:
        for extension in extensions:
            if file_name.endswith(extension):
                filtered_files.append(file_name)
                break

    return filtered_files


directory = r'C:\Users\a1056968\Desktop'
# directory = r'C:\Users\a1056968\OneDrive - PROD - sensata.com Azure AD (sso.sensata.com) (Not O365)\01 MSG\NPD\Rapa SFF\PV\Tests\E-16\RID17646_E-16_Ground potential difference'

excel_files = filter_files(directory, ['.xlsx'])
for file in excel_files:
    excel_to_images(file, ['FC1', 'FC2'], "%Y-%m-%d-%H-%M-%f")



