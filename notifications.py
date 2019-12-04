# code smell tut

# creating a Function
def Yell(text):
    text.upper()
    number_of_chars = len(text)
    result = text + "!" * (number_of_chars //4)
    print(result)

#showing Praise
Yell("You are doing Great")
Yell("Don't forget to ask for Help")
Yell("Keep it D.R.Y.")