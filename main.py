def main():
  path = "books/frankenstein.txt"
  text = get_text(path)
  print(word_count(text))
  print(char_count(text))

def get_text(path):
  with open(path) as f:
    return f.read()

def word_count(text):
  return len(text.split())

def char_count(text):
  char_count = {}

  for char in text.lower():
    if char in char_count:
      char_count[char] += 1
    else:
      char_count[char] = 1

  return char_count

main()