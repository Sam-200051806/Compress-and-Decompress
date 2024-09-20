import zlib
import base64
def compress(inputfile,outputfile):
    data = open(inputfile,'r').read()
    databytes = bytes(data,'utf-8') #changing from str to bytes
    compresseddata = base64.b64encode(zlib.compress(databytes,9)) #compressed here
    decodedata = compresseddata.decode('utf-8') #decoding to write in new
    file2 = open(outputfile,'w')
    file2.write(decodedata)
    file2.close()
def decompress(inputfile,outputfile):
    data = open(inputfile,'r').read()
    encode = bytes(data,'utf-8')
    decom = zlib.decompress(base64.b64decode(encode))
    decoded_data = decom.decode('utf-8')
    file = open(outputfile,'w')
    file.write(decoded_data)       
    file.close() 