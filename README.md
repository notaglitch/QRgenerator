# QR Code Generator

Welcome to the **QR Code Generator Tool**! This simple Python tool allows you to generate custom QR codes based on a source URL, with customizable colors for both the QR code itself and its background. Once created, the QR code is saved as a PNG file on your system.

---

## Features

- **Customizable Colors**: Choose your preferred color for both the QR code and its background.
- **Save as PNG**: The generated QR code is saved in PNG format with the name you specify.
- **Simple User Input**: The program prompts you for a link, file name, and colors, making it easy to create QR codes.

---

## How to Use

### 1. **Clone the Repository**

Clone the repository to your local machine:

```bash
git clone https://github.com/notaglitch/QRgenerator.git
```

### 2. **Install Required Libraries**

Before running the script, you'll need to install the following Python libraries:

- `qrcode`: Used to generate the QR code.
- `Pillow`: Used for image processing.

You can install them using pip:

```bash
pip install qrcode[pil] pillow
```

### 3. **Run the Script**

Navigate to the directory where the script is located, and run it:

```bash
python qrgen.py
```

### 4. **Follow the Prompts**

The tool will ask you to provide the following inputs:

1. **Source Link**: The URL or text you want the QR code to encode.
2. **File Name**: The name you want to give the PNG file. The script will automatically add `.png` to the name.
3. **QR Code Color**: The color you want the QR code itself to be.
4. **Background Color**: The color you want the background of the QR code to be.

The script will then generate the QR code and save it as a PNG file in the same directory.

---

## Example

1. **Run the script**:

    ```
    Enter the source link: https://www.example.com
    Save file as: (Enter a name without the format) my_qr_code
    What color do you want the QR code? blue
    What color do you want the background? white
    ```

2. **Output**:
   The script will generate a QR code with the following properties:
   - URL: `https://www.example.com`
   - QR code color: `blue`
   - Background color: `white`
   - File saved as: `my_qr_code.png`

---

## Code Explanation

The script works as follows:

1. **Input Collection**:
   - The script prompts you to input the source URL (`source`), the name for the output file (`file_name`), and the desired colors for the QR code and its background.
   
2. **QR Code Creation**:
   - The `qrcode.QRCode()` method is used to create the QR code object.
   - `add_data()` is called to add the provided URL or text to the QR code.
   - `make_image()` generates the image, applying the selected fill (QR code) and background colors.

3. **Saving the Image**:
   - The generated QR code image is saved with the specified filename using the `save()` method.

---

## Customization

- **QR Code Colors**: You can customize both the foreground (QR code) and background colors using any valid color name or hex code. For example:
  - `qr_color = "blue"` or `qr_color = "#0000FF"` (for blue)
  - `bg_color = "white"` or `bg_color = "#FFFFFF"` (for white)

- **Image Resolution**: You can modify the resolution of the QR code by changing the `box_size` parameter in the `QRCode()` constructor. Increasing this value makes the QR code larger.

---

## Example Walkthrough

If you run the script with the following inputs:

```
Enter the source link: https://www.example.com
Save file as: my_website_qr
What color do you want the QR code? green
What color do you want the background? black
```

- The tool will generate a QR code for the link `https://www.example.com` with:
  - **Green QR code**.
  - **Black background**.
  - The file will be saved as `my_website_qr.png` in your current working directory.

---

## Requirements

- Python 3.x
- Libraries:
  - `qrcode`
  - `pillow`

Install the necessary libraries with:

```bash
pip install qrcode[pil] pillow
```

---

## Contributing

Feel free to fork the repository and submit pull requests if you'd like to contribute. Suggestions for improvements and new features are always welcome!

---

## Disclaimer

- This tool is for educational and personal use. Ensure you have permission to share or use QR codes for any links that require access control.

