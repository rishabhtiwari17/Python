#I have created a sample.text file which consit of 25 different tweets
#Then I have made a list of some words which are termed as racial slurs
#I did not use any libraries like profanity_checker
#I simply used File I/O and loops to detect profanity in each tweet
#I have made the sample file such that every line cosnist of one tweet

words=["CurryCunt","nigga","DickIndians","IndianBitch","curry"]
content=True
i=1
with open("sample.txt") as f:
    while content:

        content=f.readline()
        for word in words:
           if word in content:

               print(f"This tweet is racist tweetnumber:{i}")
               print(content)


        i+=1