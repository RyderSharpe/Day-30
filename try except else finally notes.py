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
