import qrcode
from PIL import Image
import qrcode.constants

source = input("Enter the source link: ")
file_name = input("Save file as: (Enter a name without the format)")
file_name = file_name + ".png"
qr_color = input("What color do you want the QR code? ")
bg_color = input("What color do you want the background? ")

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10, border=10,)
qr.add_data(source)
qr.make(fit=True)
img=qr.make_image(fill_color=qr_color, back_color=bg_color)
img.save(file_name)