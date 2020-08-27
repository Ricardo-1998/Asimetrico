import Crypto
import binascii

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


random_number = Crypto.Random.new().read 

#Creamos nuestras llaves utilizando RSA
privateKey = RSA.generate(1024,random_number) #Tamaño de llave debe ser mayor a 1024
publicKey = privateKey.publickey()


#Decodificamos las llaves utilizando binascii(pasa de binario a ascii)
privateKey = privateKey.export_key(format='DER')
publicKey = publicKey.export_key(format='DER')

privateKey = binascii.hexlify(privateKey).decode('utf-8')
publicKey = binascii.hexlify(publicKey).decode('utf-8')


#Convertimos las llaves a objetos RSA 
privateKey = RSA.import_key(binascii.unhexlify(privateKey))
publicKey =  RSA.import_key(binascii.unhexlify(publicKey))


mensaje = "Hola mundo"
mensaje = mensaje.encode()

#Encrypt
cipher = PKCS1_OAEP.new(publicKey)
mensajeCifrado=cipher.encrypt(mensaje)
print("Mensaje cifrado: "+ str(mensajeCifrado))



#Decrypt
cipher = PKCS1_OAEP.new(privateKey)
mensaje =  cipher.decrypt(mensajeCifrado)
print("Mensaje: " + str(mensaje))