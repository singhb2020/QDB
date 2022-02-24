# QRCode Functions

# ------------------ Importing Libraries ------------------ #
import qrcode
import cv2


# ------------------ QRCode Functions ------------------ #

def generate_qrcode(database_name, table_name, id_num):
    input_data = f"{database_name}\n{table_name}\n{id_num}"
    qr = qrcode.QRCode(
        version=1,
        box_size = 10,
        border = 1
    )

    qr.add_data(input_data)
    qr.make()

    img = qr.make_image(fill='black', back_color='white')
    return img

def read_qrcode(image):
    qrDecoder = cv2.QRCodeDetector()
    data, bbox, rectifiedImage = qrDecoder.detectAndDecode(image)

    if len(data) > 0:
        output = data.split('\n')
        return output
    