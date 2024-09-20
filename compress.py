import zlib
import base64
data = open('demo.txt','r').read()
databytes = bytes(data,'utf-8') #changing from str to bytes
compresseddata = base64.b64encode(zlib.compress(databytes,9)) #compressed here
decodedata = compresseddata.decode('utf-8') #decoding to write in new
file2 = open('compressed.txt','w')
file2.write(decodedata)
file2.close()

 