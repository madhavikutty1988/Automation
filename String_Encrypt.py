from cryptography.fernet import Fernet
import xml.etree.ElementTree as ET

tree=ET.parse("D:\Tools\Jenkins\EmployeeDetails.xml")
root=tree.getroot()
for e in root.findall('Employee'):
    usrnm_xml=e.find('Username').text

    pswd_xml=e.find('Password').text

usrnm=str.encode(usrnm_xml)
pswd=str.encode(pswd_xml)

key=Fernet.generate_key()
cipher=Fernet(key)

usrnm_encrypt=cipher.encrypt(usrnm)
print(str(usrnm_encrypt,'utf8'))

pswd_encrypt=cipher.encrypt(pswd)
print(str(pswd_encrypt,'utf8'))
