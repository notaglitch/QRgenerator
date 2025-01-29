This QR Code Generator is a simple yet powerful tool that allows users to create custom QR codes with ease. Built using Python, it leverages the `qrcode` and `Pillow` libraries to generate and manipulate QR codes.

### Features

- **Customizable QR Codes**: Users can specify the color of the QR code and its background. This allows for personalized designs that can match branding or personal preferences.
- **Logo Integration**: Users have the option to add a logo to the center of the QR code. This feature is particularly useful for businesses looking to incorporate their branding into the QR code.
- **User-Friendly Interface**: The program prompts users for input, making it accessible even for those with minimal technical knowledge. The clear prompts guide users through the process of generating a QR code.

### How to Use

1. **Clone the Repository**: Start by cloning the repository to your local machine using the following command:

   ```bash
   git clone https://github.com/notaglitch/QRgenerator.git
   ```

2. **Install Required Libraries**: Before running the script, you'll need to install the necessary Python libraries. You can do this using pip:

   ```bash
   pip install qrcode[pil] pillow
   ```

3. **Run the Script**: Navigate to the directory where the script is located and run it:

   ```bash
   python qrgen.py
   ```

4. **Follow the Prompts**: The tool will ask you to provide the following inputs:

   - **Source Link**: The URL or text you want the QR code to encode.
   - **File Name**: The name you want to give the PNG file. The script will automatically add `.png` to the name.
   - **QR Code Color**: The color you want the QR code itself to be.
   - **Background Color**: The color you want the background of the QR code to be.
   - **Logo File Path** (optional): If you want to add a logo, provide the file path to the logo image.

5. **Generate and Save**: After providing the inputs, the script will generate the QR code and save it as a PNG file in the same directory.

### Example

1. **Run the script**:
   `   Enter the source link: https://www.example.com
Save file as: (Enter a name without the format) my_qr_code
What color do you want the QR code? blue
What color do you want the background? white
Enter the logo file path (leave empty if no logo): /path/to/logo.png`
   The script will then create a QR code with the specified parameters and save it as `my_qr_code.png` in the current directory.
