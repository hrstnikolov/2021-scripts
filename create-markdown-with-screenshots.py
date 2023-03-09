DIRECTORY = r''
main_path = Path(DIRECTORY)
images_path = main_path / 'images'

title = 'Class-based Views'
output_file = f'{title}1.md'

image_str = [f'![[images/{image.stem}.png]]' for image in images_path.iterdir()]

final_text = '\n\n'.join([
    title,
    *image_str,
])

with open(main_path / output_file, 'w') as f:
    f.write(final_text)
