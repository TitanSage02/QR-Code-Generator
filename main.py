import qrcode
from PIL import Image, ImageDraw

text = input("Entrez le texte à encoder dans le QR code: ")

# Générer le QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(text)
qr.make(fit=True)

# Créer l'image du QR code
img = qr.make_image(fill='black', back_color='white')

# Ouvrir l'image générée
draw = ImageDraw.Draw(img)
width, height = img.size


# Afficher l'image pour vérifier
img.show()

if input("Sauvegarder l'image ?  ") == 'oui':
    img.save('qrcode.png')
    print("Image sauvegardée")
else:
    print("Image non sauvegardée !")