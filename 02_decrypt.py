import pgpy
from datetime import datetime
def main(file_to_decrypt):
    KEY_PRI = """
-----BEGIN PGP PRIVATE KEY BLOCK-----
[YOUR PRIVATE KEY HERE]
-----END PGP PRIVATE KEY BLOCK-----
""".lstrip()

    start_time = datetime.now()
    pri_key = pgpy.PGPKey()
    pri_key.parse(KEY_PRI)
    encrypted_file_message = pgpy.PGPMessage.from_file(file_to_decrypt) ## from me
    if pri_key.is_protected:
        with pri_key.unlock('[PRIVATE_KEY_PASSPHRASE]'):
            decrypted_message = pri_key.decrypt(encrypted_file_message)
    else:
        decrypted_message = pri_key.decrypt(encrypted_file_message)

    end_time = datetime.now()
    print("Decryption time: ", end_time - start_time)
    output_filename = file_to_decrypt.replace('.csv.gz.pgp','_decrypted.csv.gz')
    with open(output_filename, 'wb') as output_file:
        output_file.write(decrypted_message.message)

if __name__ == "__main__":
    file_to_decrypt = '[FILE_TO_DECRYPT]'
    main(file_to_decrypt)
