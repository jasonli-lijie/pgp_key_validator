import pgpy
from datetime import datetime

KEY_PUB = """
-----BEGIN PGP PUBLIC KEY BLOCK-----
[YOUR PGP PUBLIC KEY HERE]
-----END PGP PUBLIC KEY BLOCK-----
""".lstrip()


file_to_encrypt = '[FILENAME_TO_ENCRYPT]'
file_message = pgpy.PGPMessage.new(file_to_encrypt, file=True)

pub_key = pgpy.PGPKey()
pub_key.parse(KEY_PUB)
start_time = datetime.now()

encrypted_message = pub_key.pubkey.encrypt(file_message)

end_time = datetime.now()
print("Encryption time: ", end_time - start_time)
output_filename = file_to_encrypt + '.pgp'
with open(output_filename, 'w') as output_file:
    output_file.write(str(encrypted_message))
