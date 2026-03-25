# TASK 01: GLOBAL VS LOCAL SCOPE
# A variable inside a function is "Local" (hidden). 
# A variable outside is "Global" (visible to everyone).

name = "Global Alex" # Global

def change_name():
    name = "Local Student" # Local
    print("Inside function:", name)

# 1. Run the code. 
# 2. Why does the print below still say "Global Alex"? 
# 3. Try to make the function change the global name (Research the 'global' keyword).

change_name()
print("Outside function:", name)
