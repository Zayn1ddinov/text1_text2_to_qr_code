# QR Code Generator with Text Overlay

This Python script generates QR codes with additional text overlays using the "qrcode" and "Pillow" libraries.

# Installation

**1. Clone the Repository:**
  git clone https://github.com/Zayn1ddinov/text1_text2_to_qr_code
  
  cd YOUR_REPOSITORY/qrcode_generator

**2. Install Dependencies:**
_   pip install -r requirements.txt_
# Usage 

**1. Edit Serial Numbers and Texts:**
Open main.py in a text editor and modify the serial_numbers and texts lists to include your desired serial numbers and corresponding text overlays.

**2. Run the Script:**
Execute the Python script to generate QR codes with text overlays:
bash
Copy code
_python main.py_

**3. Generated QR Codes:**
The generated QR codes with text overlays will be saved in the qrcodes_with_text directory.

#Customization

**Text Overlay Position and Font Size:**
You can adjust the position and font size of the text overlay by modifying the _text_position_ and _font_size_ variables in _create_qr_with_text_ function within _main.py_.

**Text Font:**
To change the font of the text overlay, replace _"arial.ttf"_ with the path to your preferred TrueType font file.
