import os.path
from os import mkdir, remove
from PIL import Image


def make_preview(sender, **kwargs):
    """Makes preview for uploaded image"""
    image = kwargs['instance']
    image_path = image.file.path
    image_dir, image_filename = os.path.split(image_path)
    previews_dir = os.path.join(image_dir, 'previews')
    if not os.path.exists(previews_dir): mkdir(previews_dir)
    preview_path = os.path.join(previews_dir, 'thumb_' + image_filename)
    try:
        img = Image.open(image_path)
        width, height = img.size
        # crop to square
        if width > height:
            left = (width - height) // 2
            img.crop((left, 0, left + height, height)).save(preview_path)
        elif height > width:
            top = (height - width) // 2
            img.crop((0, top, width, top + width)).save(preview_path)
        else:
            img.save(preview_path)
    except:
        pass


def delete_images(sender, **kwargs):
    """Deletes unused images from filesystem"""
    image = kwargs['instance']
    image_path = image.file.path
    image_dir, image_filename = os.path.split(image_path)
    preview_path = os.path.join(image_dir, 'previews', 'thumb_' + image_filename)
    try:
        # delete image file
        image.file.delete(save=False)
        # delete preview
        remove(preview_path)
    except:
        pass
