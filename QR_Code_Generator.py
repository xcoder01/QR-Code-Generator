# QR Code Generator 

import qrcode

text = input("Enter text or URL to generate a QR code: ")

file_name = input("Enter the file name to save the QR code (e.g., 'my_qrcode.png'): ")

qr = qrcode.QRCode(
    version=1,  
    box_size=10,  
    border=4    
)

qr.add_data(text)
qr.make(fit=True)  

img = qr.make_image(fill_color="black", back_color="white")

try:
    img.save(file_name)
    print(f"QR code successfully generated and saved as {file_name}.")
except Exception as e:
    print(f"Error saving QR code: {e}")