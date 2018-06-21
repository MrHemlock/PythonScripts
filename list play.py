import tkinter

tkinter.Scroll

test = ['apple', 'pear', 'orange', 'grape']
print(test)

while True:
  try:
    test.remove(input())
    print(test)
    
    
  except ValueError:
    print("Invalid removal")
    
  finally:
    print("Remove another?")
    if input() in "no": break
    
print(test)
