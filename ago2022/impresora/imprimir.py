from escpos.printer import *
#import qrcode
#img = qrcode.make("Hay que ver aa")
#f = open("aa.png", "wb")
#img.save(f)
#f.close()

""" Seiko Epson Corp. Receipt Printer (EPSON TM-T88III) """
#p = Usb(0x04b8, 0x0e15, 0)
p = Usb(0x04b8, 0x0202, 0)
p.text("Boleto de ENTRADA\n")
#p.image("gato.jpg")
p.image("oso.jpg")
p.image("fecha.png")
p.barcode('0209201901335', 'EAN13', 64, 2, '', '')
p.barcode('9999999650087', 'EAN13', 64, 2, '', '')
p.cut()
