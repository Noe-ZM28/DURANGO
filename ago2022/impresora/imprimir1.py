from escpos.printer import *

# see https://github.com/python-escpos/python-escpos/blob/development/src/escpos/escpos.py

""" Seiko Epson Corp. Receipt Printer (EPSON TM-T20II) """
#p = Usb(0x04b8, 0x0e15, 0, profile="TM-T88II")
#p = Usb(0x04b8, 0x0e15, 0)
p = Usb(0x04b8, 0x0202, 0)
#p.set(bold=True, underline=1, align='center', custom_size=True, width=2, height=2)
p.text("Hello world")
#p.ln(count=1)
#p.set()
p.text("this is a test")

#p.set(align='center')
p.image("fecha.png")
#p.image("examples/graphics/climacons/rain.png")
p.qr("Dies ist ein Test", size=8)
#p.set()

p.barcode('1324354657687', 'EAN13', width=3)
p.barcode('123456', 'CODE39', width=3)

p.block_text("Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.", font='a', columns=None)
#p = Usb(0x04b8, 0x0e15, 0)
#p.text("Boleto de ENTRADA\n")
#p.image("gato.jpg")
#p.image("oso.jpg")
#p.image("fecha.png")
#p.barcode('0209201901335', 'EAN13', 64, 2, '', '')
#p.barcode('9999999650087', 'EAN13', 64, 2, '', '')
#p.cut()
p.cut()
