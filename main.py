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

# Convertir l'image en mode RGBA pour pouvoir utiliser la transparence
img = img.convert("RGBA")

# Convertir le fond en transparent (remplacer la couleur blanche par de la transparence)
data = img.getdata()

new_data = []
for item in data:
    # Remplacer le blanc par de la transparence (alpha = 0)
    if item[:3] == (255, 255, 255):  # RGB de blanc
        new_data.append((255, 255, 255, 0))  # Fond transparent
    else:
        new_data.append(item)

img.putdata(new_data)

# Ouvrir l'image générée
width, height = img.size


# Afficher l'image pour vérifier
img.show()

if input("Sauvegarder l'image ?  ") == 'oui':
    img.save('qrcode.png')
    print("Image sauvegardée")
else:
    print("Image non sauvegardée !")