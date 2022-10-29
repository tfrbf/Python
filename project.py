#Libraries
import random




#Functions
def Encrypte():
    sentence = input("Enter your text: ")
    words = sentence.split()
    new_words = []
    
    for word in words:

        #Generate key
        ordered_list=[]
        for i in range(len(word)):
            ordered_list.append(i)
            random.shuffle(ordered_list)
            key = ordered_list
            
        key_asc = []
        for letter in key:
            key_asc.append(chr(letter+95))
        
        key_asc = "".join(key_asc)
        print(key_asc)
        

        shuffeled_word = []
        i=0

        #Generate encrypted word 
        for j in range(0,len(word)):
            shuffeled_word.append(word[key[j]])
            i += 1
        #print(Encrypted_word)
        
        Encrypted_word = []
        asc_code = 0
        for i in range(0,len(shuffeled_word)):
            asc_code = 122 - (ord(shuffeled_word[i]) - 97)
            Encrypted_word.append(chr(asc_code))
            
        Encrypted_word = "".join(Encrypted_word)
        print(Encrypted_word)
    
        new_words.append(Encrypted_word)
    
    new_words = " ".join(new_words)

    print(new_words)

        
            


        
    


#Main
#mode = input("Encrypte or Decrypt \t")

#if mode == "1":
Encrypte()