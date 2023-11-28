import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

# Функция для создания QR-кода с надписью
def create_qr_with_text(data, text, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Создание изображения QR-кода
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Создание изображения с надписью
    img_with_text = Image.new('RGB', (qr_img.size[0], qr_img.size[1] + 50), color='white')
    img_with_text.paste(qr_img, (0, 0))

    draw = ImageDraw.Draw(img_with_text)
    font = ImageFont.load_default()  # Можно выбрать другой шрифт

    draw.text((10, qr_img.size[1] + 10), text, fill="black", font=font)

    # Сохранение изображения с QR-кодом и текстом
    img_with_text.save(filename)

# Список серийных номеров
serial_numbers = [
    "901SF2NDKB00164",
    "901SF2NDKB00215",
    "901SF3NDKB00029",
    "901SF3NDKB00065",
    "901SF1NDKB00073",
    "901SEQNDKC00937",
    "901SF4NDL100059",
    "901SF4NDL100060",
    "901SF3NDL100155",
    "901SF3NDL100158",
    "901SF3NDL100161",
    "901SF3NDL100162",
    "901SF3NDL100164",
    "901SEQNDL101356"]

# Список надписей для каждого серийного номера
texts = [
    "HSC010017",
    "HSC010017",
    "HSC010018",
    "HSC010018",
    "HSC010016",
    "HSC010006",
    "HSC010019",
    "HSC010019",
    "HSC010018",
    "HSC010018",
    "HSC010018",
    "HSC010018",
    "HSC010018",
    "HSC010006"
]

# Создание папки для сохранения QR-кодов, если ее нет
output_folder = "qrcodes_with_text"
os.makedirs(output_folder, exist_ok=True)

# Генерация QR-кодов для каждого серийного номера с надписью и сохранение их
for idx, serial_number in enumerate(serial_numbers):
    if idx < len(texts):
        text = texts[idx]
    else:
        text = "Надпись отсутствует"

    filename = f"{output_folder}/QR_{serial_number}.png"
    create_qr_with_text(serial_number, text, filename)

print("Генерация QR-кодов завершена.")
