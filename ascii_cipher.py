

def main():
    encrypted_list = list("dfl?'SV)Z[WY)V*T%(\\S)XW(T%TXS'YA")
    decrypted_list = []
    new_word = []
    """
    for poopy in range(1, 101):
        for item in encrypted_list:
	        x = ord(item)
	        new_item = chr(x if 32 <= x <= 126 else 31 + x % 126)
	        decrypted_list.append(new_item)
        

        print(decrypted_list)
        #caesar_offset = caesar_offset + 1
        #break
    """
    for poopy in range (1, 101):
        for word in encrypted_list: 
            for character in word:
                x = ord(character) + poopy
                new_word.append(chr(x if 32 <= x <= 126 else 31 + x % 126))
        decrypted_list.append("".join(new_word))
        print(" ".join(decrypted_list))
        decrypted_list = []
        new_word = []




if __name__ == "__main__":
	main()