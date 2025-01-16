# Experiment 1
requires a configuration file with a path to the images set to be used, and the destination directory to store the results
images_dir: 'path/to/images/set'
destination_dir: 'path/to/destination/directory'

for each image, transforms the orginal image to rgb, lab, gray and hsv

# Experiment 2
don't really know what I was doing here

# Experiment 3
just experimenting the opencv gray scale transformation

# Experiment 4
first try on removing a mask from an image
transforms the original image to hsv, extracts a mask of the chosen color and
    1. changes the color to yellow
    2. removes the mask
image and destination hard coded

# Experiment 5
don't understand all of it, but it is used with a live camera feed

# Experiment 6
requires a configuration file similar to the Experiment 1, but with the additional case of color, where the user must insert the desired hsv color code
creates a mask os the color
    1. shows the mask in white
    2. shows the orignal mask
    3. removes the mask from the image

# Intensity Transformation
transforms intensity and encounters the perfect transformation using logarithmic or power-law (gamma)
