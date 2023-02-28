from PIL import Image

# Open the original image
original_image = Image.open("assets/char_356_broca/back/char_356_broca_marthe_4[alpha].png")

# Get the original image dimensions
width, height = original_image.size

# Resize the original image to double its dimensions
resized_image = original_image.resize((width*2, height*2))

# Create a new image with double the dimensions
new_image = Image.new("RGBA", (width * 2, height * 2), color=(255, 255, 255, 0))

# Paste the resized image onto the new image with stretching
new_image.paste(resized_image, (0, 0, width * 2, height * 2))

# Save the new image
new_image.save("doubled_stretched.png")
