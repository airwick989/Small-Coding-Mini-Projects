import sys
sys.setrecursionlimit(10*2000)    #Was running into runtime errors for too many recursive calls, this solved it.
#10*2000 because lets assume absolutely worst case, trying 10 passwords (max passwords constraint), for every character of loginAttempt (max constraint is 2000)
#so max recusrion limit should be 10*2000?? This was a guess

validCache = []  #Using a cache of valid loginAttempt sections to improve speed, it was taking WAAAYY too long before implementing caching, to the point where it timed out
output = [] 

def crack(passwords, loginAttempt):

    global output
    global validCache

    isValid = False

    if len(loginAttempt) == 0:
        
        return True
    elif loginAttempt not in validCache:   #Only steps into recursion if the loginAttempt section is not already cached
        
        for password in passwords:
            
            login_section = loginAttempt[len(loginAttempt) - len(password):]

            if password == login_section:

                reducedloginAttempt = loginAttempt[:len(loginAttempt) - len(password)]
                
                validCache.append(loginAttempt)  #If this login section is a password, cache it
                
                isValid = crack(passwords, reducedloginAttempt)
                
            if isValid == True:
                
                output += [login_section]
                return True
    else:

        return False




def passwordCracker(passwords, loginAttempt):
    # Write your code here
    global output
    global validCache

    output = []
    validCache = []
    
    isValid  = crack(passwords, loginAttempt)

    if isValid == True:

        result = ""

        for word in output:

            result += f"{word} "

        result = result.strip()

        return result
    else:

        return "WRONG PASSWORD"
    


Passwords = ["ba", "ab","baab", "baabbaab", "baabba" ,"abbaab", "abbaabab", "ababbaab", "baabbaabba","abbaabbaab"]

LoginAttempt = "baabbaabbabaabbaabbabaabbabababaabbabaabbaabababbaabbaabbaabbaabbaabbaababbaabbaabbaabbaabababbaababbaabbababaabbaababbaababbaabbaabbaabbaabbaababbaababbaababbaababbaababbaabbabaabbaabababbaababbaababbaabababbaababbaabbaabbabaabbaababbaababbaabbaababbaabbaabbaabababbaabbaabbaabbaabababbaabbaabbaababbaabbaabbaababbaabbaabbaabbaabababbaabababbaababbaababbaabbaabbabaabababbaababbaababbaababbaabbaabbaabbaabababbaababbaabababbaabababbaabbaabbaababbaabababbaabbaabbaabbaabbaabbaabbaabbaababbaabbabaabbaabbaabbaababbabaabbaabbaabbaabbaabbabaabbaabbaabbaabbaabbaabbaabababbaababbaababababbaababbaabbaabbaababbaababbaababbaabbaabbaabbaabbaabbaabbaababbaababbaababbaabbaabbabaabbaabbabaabbaababbaababababbaabbaabbabaabbaababbaababbaabbaabbabaabbaababbaabababbaabbaabbaabbaabbaabbaabbabaabbaabbaabbaabbaabbabaabababbaababbaabbaabbaabbaabbaabbaababbaabbaabbaabbabaabbaabbaabbaabababbaababbaabbaabbaabababbaabbaabbabaabbaabbaabababbaabbaabbabaabbaabbabaabbaabbaabababbaabbaabbaababbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabababbaababbaabababbaabababbaabbabaababbaabbabaabbaababbaabababbaababbaabbaabababbaababbaababbaabbaabbaabababbaababbaabbaabbaabbabaababbaababbaababbaabbaabababbaabbaabbaabbaabababbaabababbaabbaababbaabbaababbaababbaabbaabbabaabbaabababbaabbaabbaababbaabbaabbaabbaabbaababbaababbaabbaabbabaabbaabbabaabbaababbaababbaabbaababbaabbaabbaabbaababbaabbabaabbaabbaababbaababbaabbaabbaabbabaabbabaabbaabababbaabbaabbabaabbaabbaabbaabbaabbaabbaabbabaabbaabbabaabbaabbaabbaababbaabababbaabbaababbaabbaabbaabbabaababbaababbababaabbabaabbaabababbaababababbaababbaababababbaabbabaabbaabbaabbaabbaabbaabbaabbaabbaababababbaababbaabbaabbaabbaabbaabbaababbaababbaabbaabbaabbaabbabaababbaabbaabbaabbaabababbaabbaabbaabbaabbaabbaababbaabbabaabbaabbaabbabaabbaabbaabbaabbaababbaababbaabbaababbaabababababbaabbaabbaabbababaabbaabababbaabbaabababbaabbaabbaabbaabbaabbaababbaabbaababbaabbaababbaabbaababbaababababbaababababbaababbaabababbaabababbaababbaabbabaabbabaabbaabbaababbaababbaabababbaabbaabbaabbabaabab"

print(passwordCracker(Passwords, LoginAttempt))