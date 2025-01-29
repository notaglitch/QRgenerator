import qrcode
from PIL import Image
import qrcode.constants
import os

def generate_basic_qr():
    source = input("Enter the source link: ")
    file_name = input("Save file as: (Enter a name without the format)") + ".png"
    qr_color = input("What color do you want the QR code? (e.g., 'black') ")
    bg_color = input("What color do you want the background? (e.g., 'white') ")

    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=10)
    qr.add_data(source)
    qr.make(fit=True)

    img = qr.make_image(fill_color=qr_color, back_color=bg_color)
    img.save(file_name)
    print(f"QR code saved as {file_name}")

def generate_qr_with_logo():
    source = input("Enter the source link: ")
    file_name = input("Save file as: (Enter a name without the format)") + ".png"
    qr_color = input("What color do you want the QR code? ")
    bg_color = input("What color do you want the background? ")

    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=10)
    qr.add_data(source)
    qr.make(fit=True)

    img = qr.make_image(fill_color=qr_color, back_color=bg_color)

    logo_path = input("Enter the logo file path (leave empty if no logo): ")
    if logo_path and os.path.exists(logo_path):
        logo = Image.open(logo_path)
        qr_width, qr_height = img.size
        logo_size = int(qr_width / 4)  # Adjust logo size
        logo = logo.resize((logo_size, logo_size))
        logo_x = (qr_width - logo_size) // 2
        logo_y = (qr_height - logo_size) // 2
        img.paste(logo, (logo_x, logo_y), logo.convert("RGBA"))
    
    img.save(file_name)
    print(f"QR code with logo saved as {file_name}")

def main():
    while True:
        print(''' 
 ▄▄▄▄▄▄▄  ▄    ▄ ▄▄▄▄▄ ▄▄▄▄▄▄▄ 
 █ ▄▄▄ █ ▀█▄█▀▀██▄  ▄█ █ ▄▄▄ █ 
 █ ███ █ ▀▀▄▀▄█▄▀▀███▄ █ ███ █ 
 █▄▄▄▄▄█ █ █ ▄ ▄▀█▀▄ █ █▄▄▄▄▄█ 
 ▄▄▄▄▄ ▄▄▄▄▄ █ █▄█▄ ▀ ▄ ▄ ▄ ▄  
  ▄▀ ██▄▀ █ ▄▄▄█▄█▄ ▀▀▄█▀▀   ▀ 
 ▀▄▄▄ ▄▄  █▀█ ▄██▄▄ █▀  ▀ █▄▀  
  ██▄▀▄▄▄ ▀▀ ▀▄▄█▀ █▀▄▀█▄▀▄▄ ▀ 
 ▀▀ ▀█▄▄ █▄▄ █ ██▀▄  ▀ ▀█▀▄▄▀  
 █ ▀█  ▄ █▄█▄▄▀▀▄█  ▀▀ ▀█▀ █ ▀ 
 █   █ ▄ █▀ █ ▄▄▀█▄▀▀▄▄▄██ ▄█▄ 
 ▄▄▄▄▄▄▄ █▀█ ▀▄ ▄ ▄█▄█ ▄ ███▀▀ 
 █ ▄▄▄ █ ▄ █ █ █▄█▄ ▀█▄▄▄█ ▄▄█ 
 █ ███ █ ██ ▄▄ ▀▄█▀██  ▄█▄███▀ 
 █▄▄▄▄▄█ █▄ █▄ ▀ █▄██▀▄ █▄█▄▀  
                              
        ''')
        print("-notaglitch")
        print("\nQR Code Generator")
        print("1. Generate Basic QR Code")
        print("2. Generate QR Code with Logo")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            generate_basic_qr()
        elif choice == "2":
            generate_qr_with_logo()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
