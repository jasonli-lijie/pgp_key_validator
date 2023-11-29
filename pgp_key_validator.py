import pgpy
print("Enter/Paste your public key here. Ctrl-Z ( windows ) to save it.")
contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)

KEY_PUB = '\n'.join(contents)
print(KEY_PUB)

KEY_PUB = KEY_PUB.lstrip()


pub_key = pgpy.PGPKey()
pub_key.parse(KEY_PUB)

print("Key created: ",  pub_key.created)
print("Key expires_at: ",  pub_key.expires_at)
print("Key is_expired: ",  pub_key.is_expired)
print("Key is_primary: ",  pub_key.is_primary)

print("Key is_public: ",  pub_key.is_public)
print("Key key_algorithm: ",  pub_key.key_algorithm)
print("Key key_algorithm.can_gen: ",  pub_key.key_algorithm.can_gen)
print("Key key_algorithm.can_encrypt: ",  pub_key.key_algorithm.can_encrypt)
# print("Key key_algorithm.can_gen(): ",  pub_key.key_algorithm.can_gen)

print("Key key_size: ",  pub_key.key_size)
print("Key userattributes: ",  pub_key.userattributes)

print("Key userids: ")
for id in pub_key.userids:
    print('-------------------')
    print('name: ', id.name)
    print('email: ', id.email)
    print('comment: ', id.comment)
    print('userid: ', id.userid)
    # print('name: ', id.name)
    print('-------------------')


