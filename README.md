# 🎨 QR Code Generator with Custom Colors

A simple Python script to generate QR codes with customizable **fill** and **background** colors.

---

## 🔧 Features

- Generate QR codes for any text or URL
- Choose custom colors using standard color names or HEX codes
- Input validation for color names (no crashes on typos!)
- Supports creating multiple QR codes in one session
- Clean and user-friendly terminal prompts

---

## ▶️ How to Run

1. Make sure you have Python 3 installed.
2. Install the required libraries:
   ```bash
   pip install qrcode[pil]
   
3. Run the script:
    ```bash
    python qr_generator.py

4. Example Usage
    ```bash
    Enter the text or URL: https://github.com
    Enter the filename: myqr
    Choose a fill color: red, green, blue, black, yellow
    Enter the fill color (default: black): blue
    Enter the background color (default: white): yellow
    ✅ QR code saved as myqr.png
    One More QR-? y/n: y

5. Valid Color Formats
  You can enter:

  Common color names: red, blue, green, black, white, etc.
  
  See full color list: https://www.w3schools.com/tags/ref_colornames.asp

7. Output
   
     -QR codes are saved as .png images in the same directory where the script is run.

8. Future Ideas
   
     -Add GUI support with tkinter
   
     -Let users set size and border width
   
     -Save history of generated QR codes



    
    




