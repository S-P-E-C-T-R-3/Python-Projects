name1=input("What is your name?")
name2=input("what is their name?")
combinestr = name1 + name2
tolower = combinestr.lower()
t = tolower.count("t")
r = tolower.count("r")
u = tolower.count("u")
e = tolower.count("e")
true = t + r + u + e
l = tolower.count("l")
o = tolower.count("o")
v = tolower.count("v")
e = tolower.count("e")
love = l + o + v + e
love_score = int(str(true) + str(love))
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos")
if love_score >= 40 and love_score <= 50:
    print(f"Your love score is {love_score}, you are all right together")
else:
    print(f"your love score is {love_score}")
