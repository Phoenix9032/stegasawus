import os
import numpy

from skimage import io

from stegano import exifHeader
from stegano import lsbset
from stegano.lsbset import generators

#*******************************************************************************
def get_secret_message(filepath):
    with open(filepath, 'rb') as f:
        message = f.read()
    return message

def hide_message_jpg(secret_message, cover_file, stego_file):
    exifHeader.hide(cover_file, stego_file, secret_message=secret_message)

def batch_hide_message_jpg(secret_message, path_images, path_output):
    print 'encoding images...'
    for i, filename in enumerate(os.listdir(path_images)):
        cover = '{}{}'.format(path_images, filename)
        stego = '{}{}'.format(path_output, filename)
        exifHeader.hide(cover, stego, secret_message=secret_message*1000)
        print '{}: {}'.format(i, filename)
    print 'image encoding complete.'

def batch_hide_message_png(secret_message, path_images, path_output):
    print 'encoding images...'
    for i, filename in enumerate(os.listdir(path_images)):
        try:
            cover = '{}{}'.format(path_images, filename)
            stego = '{}{}'.format(path_output, filename)
            S = lsbset.hide(cover, secret_message, generators.eratosthenes())
            S.save(stego)
            print '{}: {}'.format(i, filename)
        except IndexError as e:
            print '{}: {} | IndexError: {}'.format(i, filename, e)

    print 'image encoding complete.'

def batch_png_to_jpg(path_input, path_output):
    print 'coverting images...'
    for i, filename in enumerate(os.listdir(path_input)):
        input_jpg = '{}{}'.format(path_input, filename)
        output_png = '{}{}'.format(path_output, filename.replace('.jpg', '.png'))
        I = io.imread(input_jpg)
        io.imsave(output_png, I)
        print '{}: {}'.format(i, filename)
    print 'image conversion complete.'


#*******************************************************************************
if __name__ == '__main__':
    # path = '/home/rokkuran/workspace/stegasawus/'
    # path_images = '{}images/train_catdog/cover/'.format(path)
    # path_output = '{}images/stego/catdog/'.format(path)
    # secret_message = get_secret_message('{}message.txt'.format(path))
    # batch_hide_message_jpg(secret_message, path_images, path_output)

    # exifHeader.hide(
    #     "{}images/Lenna.jpg".format(path),
    #     "{}images/Lenna_stego.jpg".format(path),
    #     secret_message=secret_message
    # )

    # path_cover = '{}images/train/cropped/'.format(path)
    # path_stego = '{}images/stego/paintings/'.format(path)
    # secret_message = get_secret_message('{}message.txt'.format(path))
    # batch_hide_message_jpg(secret_message, path_cover, path_stego)

    # path = '/home/rokkuran/workspace/stegasawus/'
    # path_input = '{}images/train_catdog/cover/'.format(path)
    # # path_input = '{}images/png/cover/'.format(path)
    # path_output = '{}images/png/cover/'.format(path)
    # # path_output = '{}images/png/stego/'.format(path)
    # batch_png_to_jpg(path_input, path_output)

    path = '/home/rokkuran/workspace/stegasawus/'
    path_images = '{}images/png/cover/'.format(path)
    path_output = '{}images/png/stego/'.format(path)
    secret_message = get_secret_message('{}message.txt'.format(path))
    batch_hide_message_png(secret_message, path_images, path_output)
