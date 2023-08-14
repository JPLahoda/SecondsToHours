secondsInitial = int(input("Number of seconds needed to convert: "))
secondsFinal = secondsInitial
hours = secondsFinal // 3600
secondsFinal %= 3600
minutes = secondsFinal // 60
secondsFinal %= 60
print ("The result from", secondsInitial, "seconds is:", hours, "hours,", minutes, "minutes, and", secondsFinal, "seconds")
