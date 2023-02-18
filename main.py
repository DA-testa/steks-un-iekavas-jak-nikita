from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
  return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
  opening_brackets_stack = []
  for i, next in enumerate(text):
    if next in "([{":
      opening_brackets_stack.append(Bracket(next, i+1))

    if next in ")]}":
      if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
        return i+1
      opening_brackets_stack.pop()
      
  if opening_brackets_stack:
    return opening_brackets_stack[0].position
  return "Success"

def main():
  text = None
  while not text:
    mode = input("Enter input mode (F/I): ")
    if mode == "F":
      file = input("Enter filename: ")
      f = open(file, "r")
      text = f.readline()
    elif mode == "I":
      text = input("Enter text: ")
    else:
      print("Wrong mode")
  
  print(find_mismatch(text))

if __name__ == "__main__":
  main()
