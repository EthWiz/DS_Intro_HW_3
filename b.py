def longest_words(file):
    try:
        fhand = open(file)
        text= fhand.read()
        for char in text:
            if char.isalpha() == False:
                text = text.replace(char,' ') 
        text= text.split()
        text.sort(reverse= True, key= len)
        return(text[:5])
    except:
        print("file not found")
        return []


print(longest_words("test.txt"))