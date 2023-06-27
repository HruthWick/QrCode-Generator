import qrcode

features= qrcode.QRCode(version=1,box_size=40,border=3);
features.add_data('https://youtu.be/dQw4w9WgXcQ')
features.make(fit=True)
generate_image= features.make_image(fill_color="green",back_color="black")
generate_image.save('test4.png') 