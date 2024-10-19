import qrcode
from PIL import Image
import qrcode.constants

source = input("Enter the source link: ")
file_name = input("Save file as: (Enter a name without the format)")
file_name = file_name + ".png"

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10, border=10,)
qr.add_data(source)
qr.make(fit=True)
img=qr.make_image(fill_color="red", back_color="black")
img.save(file_name)