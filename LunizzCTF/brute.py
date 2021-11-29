import bcrypt
import base64

hashpassword = b'$2b$12$SVInH5XmuS3C7eQkmqa6UOM6sDIuumJPrvuiTr.Lbz3GCcUqdf.z6'

salt= b'$2b$12$SVInH5XmuS3C7eQkmqa6UO'

with open("rockyou1.txt","r") as f:
     for word in f.readlines():
          passw = word.strip().encode('ascii', 'ignore')
          b64str = base64.b64encode(passw)
          hashAndSalt = bcrypt.hashpw(b64str, salt)
          #print(hashAndSalt)
          #print(passw)

          if hashpassword == hashAndSalt:
               print("[+] Password Found!!!: %s" % passw)
               break