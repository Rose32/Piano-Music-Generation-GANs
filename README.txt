The folder should contain the following source code files
	1. data_prep.txt
	2. piano_gan.txt
	3. convert_image2MIDI.txt
	4. image2midi.txt
	5. midi2image.txt
	
The files 4 and 5 are closed form the github repo: https://github.com/mathigatti/midi2img
These files are, as their name suggests, used to convert MIDI files into images and back.

1. data_prep.txt :  - This file prepares the data for the GAN model
					- To run this, you should have a folder containing MIDI files. The full path to this folder should be given in the variable "path"
					- Another directory to save the MIDI images should be created and put in the variable "new_dir" of the create_midi_images function 
					- Another directory for the resized MIDI images should be created and replaces in the path name of img.save in the function resize_images.
					- This path for the resized images should also be put in the path variable of the save_npy function.
					- running this file will convert all the MIDI files into images and save in the given directory, resize the images and save in teh given directory
					  and generates a .npy file containing the normalized pixel values for all the resized images. The pizel shape should be (28587, 106, 106, 1)
					  
2. piano_gan.txt :  - This file contains the GAN model 
					- The pixel file that has the .npy extension should be loaded in the pixel variable at the line 249
					- the batch size, buffer size, epochs and other hyper parameters can be modified my modifying the variables of the same name
					- Running this will train the GAN with the pixels extracted and save the composition.png files in the current directory
					
3. convert_image2MIDI.txt - The composition image file should be passed in the argument of the function image2midi
						  - Running this will generate a composition.mid file that can be downloaded and played in VLC player that has the MIDI file 
						  support extension installed
	
