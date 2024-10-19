# Day-30
Errors, Exceptions and saving JSON Data: Improving the Password

try:
except:
else:
finally:
----------------------------------------try------------------------------------------------
-You try to open the toy box (like opening a file). If it works, you get to play with the toys
try:
    file = open("a_file.txt")
---------------------------------------except--------------------------------------------------
-But, what if the toy box is locked (FileNotFoundError) or you can't find the toy you want (KeyError)?

-You have two special friends to help.

1) FileNotFoundError Friend: If the box is locked, this friend CREATES a new box for you.

except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("whatever you want")
   
3) KeyError Friend: If you can't find the toy, this friend tells you which toy is missing.

except KeyError as error_message:
    print(f"the key {error_message} does not exist")

----------------------------------------else------------------------------------------------
-If you successfully opened the box and found the toy, you get to play!

else:
    content = file.read()
    print(content)

----------------------------------------finally------------------------------------------------
-No matter what happened, your mom reminds you to clean up!

finally:
    file.close()
    print("file was closed")


    Here's a simple summary:
Try: Attempt to do something.
Except: Handle problems that might occur.
Else: Do something if no problems occurred.
Finally: Always do this, no matter what.
Now, go play with your toys (code) and remember to clean up!
