
#string slicing
# [start: stop: stepover]
#strings are immutable; except you create a new variable you cannot change.
# selfish = "01234567"
# selfish[0] =  "100"
# print(selfish)


username = input("what is your name?")

password = input("what is your password?")
password_len = len(password)
hash_password = int(len(password)) * "*"
print(f'hi {username}, your password {hash_password} is {password_len} letters long')