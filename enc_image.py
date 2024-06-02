from PIL import Image

# open the image
img = Image.open(image_path)

# load the pixel map
pixel_map = img.load()

# define the string
text = "ASCII stands for American Standard Code for Information Interchange. Below is the ASCII character table, including descriptions of the first 32 characters. ASCII was originally designed for use with teletypes, and so the descriptions are somewhat obscure and their use is frequently not as intended."

# define the starting point
xd = 0

# iterate over each character in the string
for char in text:
    # get the RGB values of the current pixel
    r, g, b = img.getpixel((xd, 0))

    # convert the character to its ASCII value and add it to the red component

    r = min(r + ord(char)-96 , 255)

    # update the pixel with the new RGB values
    pixel_map[xd, 0] = (r, g, b)

    # increment the coordinate for the next pixel
    xd += 1

# save the modified image in a lossless format (PNG)
img.save("zd.png", format="PNG")
