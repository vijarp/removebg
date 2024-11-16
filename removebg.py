from rembg import remove
from PIL import Image
def remove_background(image_path, output_path) :
    processed_image = Image.open(image_path)
    # removing background image
    output_image = remove(processed_image)
    # saving image
    output_image. save ( output_path)
print( "Tmage processed successfully")
# insert path to where image is saved
image_path= "b1.jpeg"
# insert path and name to save processed image(png format)
output_path = "b1_rm.png"
remove_background(image_path, output_path)