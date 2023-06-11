from difflib import SequenceMatcher

with open("1.txt") as file1, open("2.txt") as file2:
    #read both text file
    file1data=file1.read()
    file2data=file2.read()

    #compare both text files
    similarity=SequenceMatcher(None,file1data,file2data).ratio()

    #convert decimal output in integer
    result=int(similarity*100)
    print(f"{result}% Plagiarized Content")
