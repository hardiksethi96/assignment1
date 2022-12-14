print("This tool converts time from seconds to minutes")
time = int(input("Enter time in seconds: "))
minutes = time//60
seconds = time%60
print(str(time) + " seconds equal " + str(minutes) + " minutes and " + str(seconds) + " seconds.")