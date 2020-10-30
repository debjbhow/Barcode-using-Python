import barcode

from barcode.writer import ImageWriter
data= '34567893463446789'
data1= str(data)
a= barcode.get_barcode_class('ean13')
b=a(data, writer=ImageWriter())
c=b.save('barcode')