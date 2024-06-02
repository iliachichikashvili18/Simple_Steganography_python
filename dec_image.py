from PIL import Image

def decrypt_image(original_image_path, encrypted_image_path):
    # open the original and encrypted images
    original_image = Image.open(original_image_path)
    encrypted_image = Image.open(encrypted_image_path)

    # load pixel maps
    original_pixel_map = original_image.load()
    encrypted_pixel_map = encrypted_image.load()

    # get the size of the images
    width, height = original_image.size

    # space for empy string
    decrypted_message = ""

    # iterate over each pixel in the images
    for y in range(height):
        for x in range(width):
            # get RGB values of the original and encrypted pixels
            r_original, g_original, b_original = original_pixel_map[x, y]
            r_encrypted, g_encrypted, b_encrypted = encrypted_pixel_map[x, y]

            # decrypt the message by subtracting the RGB values(at this moment only red)
            decrypted_char = chr((r_encrypted - r_original)+96)

            # append the decrypted character to the message
            if decrypted_char != '`':
                decrypted_message += decrypted_char

    return decrypted_message

# usage
original_image_path = "original_image_path"
encrypted_image_path = "encrypted_image_path"
decrypted_message = decrypt_image(original_image_path, encrypted_image_path)
print("Decrypted Message:", decrypted_message)
