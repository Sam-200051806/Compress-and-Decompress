import zlib
import base64
data = open('compressed.txt','r').read()
encode = bytes(data,'utf-8') #data.encode('utf-8') or  databytes = bytes(data,'utf-8')
decom = zlib.decompress(base64.b64decode(encode))
decoded_data = decom.decode('utf-8')
file = open('decompressed.txt','w')
file.write(decoded_data)       
file.close() 