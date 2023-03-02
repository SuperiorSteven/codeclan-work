# set animal  = input "What animal are you"
# if the animal is a "chicken"
#  THEN PRINT "This is my favorite animal"
#  ELSE 
#  IF animal is "Kitten"
#   THEN PRINT "I love kittens" 
#  ELSE 
#   PRINT "Sad, not my favourite"
# END

animal = input("What animal are you? ")

if animal == "chicken":
    print("This is my favorite animal")
elif animal == "kitten":
     print ("I love kittens")
else:
    print("Sad, not my favourite")

    score = 6

    result = "pass" if score > 5 else "fail"

    # checking multiple conditions