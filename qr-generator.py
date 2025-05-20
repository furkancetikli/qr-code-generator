import qrcode
from PIL import ImageColor

def is_valid_color(color_str):
    try:
        ImageColor.getrgb(color_str)  # Geçersizse hata verir
        return True
    except ValueError:
        return False

data = input('Enter the test or URL: ').strip()
filename = input('Enter the filename: ').strip()

while True:
    print("Choose a fill color: red, green, blue, black, yellow")

    f_color = input('Enter the fill color (default: black): ').strip() or 'black'
    if not is_valid_color(f_color):
        print(f"❌ '{f_color}' is not a valid color. Please try again.")
        continue
    
    b_color = input('Enter the background color (default: white): ').strip() or 'white'
    if not is_valid_color(b_color):
        print(f"❌ '{b_color}' is not a valid color. Please try again.")
        continue


    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(data)
    image = qr.make_image(fill_color = f_color, back_color = b_color)
    image.save(f'{filename}.png')


    print(f'QR code saved as {filename}'),

    choice = input("One More QR-? y/n")
    if choice == 'n':
        break
