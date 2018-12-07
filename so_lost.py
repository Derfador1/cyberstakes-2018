from pwn import *

def main():
    #print("puppy")
    iter_var = 0
    correct_answers = 0

    p = remote("challenge.acictf.com", 31802)

    while (True):
    	text = p.recvline('')

        if(correct_answers == "40"): #I hate this elif
            if(text[0:4]) == "flag":
                print(text)
                break


        if text == 'left':
            p.sendline('<')
        elif text == 'right':
            p.sendline('>')
        elif text == 'up':
            p.sendline('^')
        elif text == 'down':
            p.sendline('V')
        elif text[0:3] == "Awe": #I hate this elif
            correct_answers = text[37:39]





if __name__ == "__main__":
	main()

