# pip install qrcode
# pip install pillow
import qrcode as qr
image=qr.make("https://www.linkedin.com/in/gayatri-musunuri-753531272/")
image.save("Linkedin.png")