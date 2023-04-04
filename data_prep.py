import os
import numpy as np
from midi2image import midi2image
from PIL import Image
from matplotlib import pyplot as plt 
import numpy as np
from numba import jit, cuda


path = '/home/rgurung/projects/projects/surname_checked_midis/surname_checked_midis' #path of the MIDI files
os.chdir(path)
midiz = os.listdir()
midis = []
for midi in midiz:
    midis.append(path+'/'+midi)
path = '..'
os.chdir(path)

# print(midis)
print(len(midis))

@jit
def create_midi_images():
    new_dir = '/home/rgurung/projects/projects/surname_checked_midi_images_gpu' #path to save the MIDI images
    for midi in midis:
    #   try:
            os.chdir(new_dir)
            print(midi)
            midi2image(midi)
    #   except:
    #       pass
    os.chdir('..')

    print('MIDIs converted to images')

create_midi_images()

# new_dir = '/content/midi_image'
# os.chdir(new_dir)
# img_list = os.listdir('./surname_checked_midi_images_gpu')
@jit
def resize_images():
    img_list = os.listdir('./surname_checked_midi_images_gpu')
    for i in range(len(img_list)):
        img=Image.open("./surname_checked_midi_images_gpu/"+img_list[i])
        img = img.resize((106,106), Image.ANTIALIAS)
        img.save(('./surname_checked_midi_images_gpu_resized/'+img_list[i]).replace(".png","_resized.png"))

resize_images()
print('Images resized')

@jit
def access_images(img_list,path):
    pixels = []
    imgs = []
    for i in range(len(img_list)):
        if 'png' in img_list[i]:
            # try:
                img = Image.open(path+'/'+img_list[i],'r')
                img = img.convert('1')
                pix = np.array(img.getdata())
                pix = pix.astype('float32')
                # pix /= 255.0
                pix = (pix - 127.5) / 127.5
                pixels.append(pix.reshape(106,106,1))
                imgs.append(img)
            # except:
            #     pass
    return np.array(pixels),imgs
def show_image(pix_list):
    array = np.array(pix_list.reshape(106,106), dtype=np.uint8)
    new_image = Image.fromarray(array)
    new_image.show()

@jit
def save_npy():
    path = './surname_checked_midi_images_gpu_resized'
    os.getcwd()
    img_list = os.listdir(path)
    pixels,imgs = access_images(img_list,path)

    np.save('new_1272022_pixels.npy', pixels)


save_npy()

print('new_1272022_pixels.npy saved')
pixels=np.load('new_1272022_pixels.npy')
print('pixel shape: ',pixels.shape)
# print(pixels.shape)

print(np.unique(pixels)) 
