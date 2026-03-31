import qrcode

def generate_qr_code(data, filename):
    # Create a QR Code instance
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,
                        box_size=10, border=4)
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill='black', back_color='white')
    
    # Save the generated QR code image
    img.save(filename)

if __name__ == '__main__':
    # Example usage
    generate_qr_code('https://example.com', 'qr_example.png')