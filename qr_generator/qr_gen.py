import qrcode
"""
1) Create a Virtual Environment
-> A Virtual Environment in python is separated 
isolated workspace to install packages and run python
projects.
-python -m venv venv(WINDOWS)
-python3 -m venv venv(MACOS)
-venv folder will be creted automatically
-it contains several file which we do not
 git to track it. In order to achieve this
 create a global file in the main folder(.gitignore)
 write (venv/) to tell git to not to track the venv
 folder

2) In order to activate venv write the following
statement in the terminal
(venv/Scripts/activate) - WINDOWS
(source venv/bin/activate)-MACOS

To generate a QR CODE we will use a thrid party library
https://pypi.org/project/qrcode/
 execute the following statement to
 install qrcode package or you can copy
 the command from the official website as well
 pip install qrcode
"""

data = input('Enter the text or URL: ').strip()
filename = input('Enter the filename: ').strip()

qr = qrcode.QRCode(box_size = 10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_color = 'white')
image.save(filename)
print(f'QR code saved as {filename}')