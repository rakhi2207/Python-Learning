def is_password_valid(password):
    numeric = 0
    Upper = 0
    Lower = 0
    if len(password) >= 8:
        for i in password:
            val=ord(i)
            # print(val)
            if val >= 65 and val <= 91:
                Upper = 1;
            elif val >= 97 and val <= 123:
                Lower = 1
            else:
                numeric += 1;
    else:
        return False

    if Upper == 1 and Lower == 1 and numeric >= 3:
        return True
    else:
        return False
    # your code goes here
    # check the solution in the discord server.

print(is_password_valid("abcd3999994"))
