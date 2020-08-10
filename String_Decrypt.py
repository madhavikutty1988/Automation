import String_Encrypt

usrnm_decrypt=String_Encrypt.cipher.decrypt(String_Encrypt.usrnm_encrypt)
usrnm_use=(str(usrnm_decrypt,'utf8'))

pswd_decrypt=String_Encrypt.cipher.decrypt(String_Encrypt.pswd_encrypt)
pswd_use=str(pswd_decrypt,'utf8')
