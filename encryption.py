alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

end=input("What do you want to do to your text: encode or decode? ")
text=input("Enter your text: ").lower()
shift=int(input("Enter shift number: "))

def encrypt(plain_text,shift_no):
  cipher_text=""
  for letter in plain_text:
    pos = alphabet.index(letter)
    new_pos = pos + shift_no
    new_letter = alphabet[new_pos]
    cipher_text += new_letter
  print(f"Encrypted text is {cipher_text}")

def decrypt(cipher_text,shift_no):
  plain_text=""
  for letter in cipher_text:
    pos = alphabet.index(letter)
    new_pos = pos - shift_no
    new_letter = alphabet[new_pos]
    plain_text += new_letter
  print(f"Decrypted text is {plain_text}")

if end == "encode":
  encrypt(plain_text=text,shift_no=shift)
elif end == "decode":
  decrypt(cipher_text=text,shift_no=shift)
