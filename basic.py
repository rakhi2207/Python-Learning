marks = []
# taking in the input for 5 marks from the user and adding it to the list
for i in range(5):
    marks.append(int(input()))
# now that we have all the marks we can just loop over it
output = ""


# Write your code here
# for every mark concatenate grades to the output e.g output+="A"
# start here

# now we simply print the output
for i in marks:

    if i >= 90 and i <= 100:
        print(i)
        output += "A"
    elif i >= 80 and i <= 89:
        print(i)
        output += "B"
    elif i >= 70 and i <= 79:
        print(i)
        output+= "C"
    elif i >= 60 and i <= 69:
        output += "D"
    elif i >= 50 and i <= 59:
        output += "E"
    else:
        output += "F"

print(output)
