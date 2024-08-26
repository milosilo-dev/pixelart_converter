# Pixel Art Converter

![A view of the UI for the program.](https://ibb.co/SNWJjS3)

## **About**

This is a small project that I built quickly in 1 day. This can be used to take normal bitmap images and create pixel art from them. This project is built in python and uses `FreeSimpleGUI` for the front end and uses `PIL` for image manipulation. At the moment it only supports `.jpg` and `.png`.

## Install

To install you first have to run:

pip3 install FreeSimpleGUI PIL
after that you can run it using:

python3 converter.py
## Usage

**Step 1:**
When you run the program you should first click on the `Photo Selection` button, then you will see a file explorer pop up and you will need to navigate to the photo that you want to convert. The default directory is the one that you were in when you ran the python script.

**Step 2:**
After that you can select a new width for the image in pixels. The height will be calculated automatically to keep the same aspect ratio.

**Step 3:**
Now you can name your converted file, there is a button that will get the filename of the uploaded file and add a "_px" to the end of it. The file will be saved to the same directory as the file that you selected in step 1.

**Step 4:**
once you hit the `Convert` button you will see both of your images pop up, the first is the original and the second is the converted version. Once the images are closed the converted image will auto save in the same directory as the original and the file extension will be kept.

## Possible ideas

Here are some features that I could add in the future:

- Different file formats
- Output to pixel art programs for editing
- More customisation for the output
- Built-in image cropping
