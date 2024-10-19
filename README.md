# Day-30
Errors, Exceptions and saving JSON Data: Improving the Password

+------------------+-------------------------------------------------------------------------------+
|      Clause      |                             Explanation                                        |
+------------------+-------------------------------------------------------------------------------+
|      try         | - Try to do something (like opening a toy box).                               |
|                  | - If it works, you can proceed (e.g., open a file, play with toys).           |
|                  | Example:                                                                      |
|                  | try:                                                                          |
|                  |     file = open("a_file.txt")                                                  |
+------------------+-------------------------------------------------------------------------------+
|     except       | - Handle problems that might occur when trying to open the box.                |
|                  | - Two types of problems:                                                      |
|                  |     1) FileNotFoundError (toy box is missing/locked):                         |
|                  |        - Your friend creates a new toy box for you.                           |
|                  |        Example:                                                               |
|                  |        except FileNotFoundError:                                              |
|                  |            file = open("a_file.txt", "w")                                     |
|                  |            file.write("whatever you want")                                    |
|                  |                                                                               |
|                  |     2) KeyError (specific toy is missing):                                    |
|                  |        - Your friend tells you which toy is missing.                          |
|                  |        Example:                                                               |
|                  |        except KeyError as error_message:                                      |
|                  |            print(f"The toy '{error_message}' is missing.")                    |
+------------------+-------------------------------------------------------------------------------+
|      else        | - If no problems happened, you get to play with the toy (read the file).       |
|                  | Example:                                                                      |
|                  | else:                                                                         |
|                  |     content = file.read()                                                     |
|                  |     print(content)                                                            |
+------------------+-------------------------------------------------------------------------------+
|    finally       | - No matter what happens, clean up after playing (close the toy box).          |
|                  | Example:                                                                      |
|                  | finally:                                                                      |
|                  |     file.close()                                                              |
|                  |     print("Toy box closed. Clean up time!")                                   |
+------------------+-------------------------------------------------------------------------------+


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
