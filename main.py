def main():
  path = "books/frankenstein.txt"
  text = get_text(path)
  word_count = get_word_count(text)

  print(f"--- Begin report of {path} ---")
  print(f"{word_count} words found in the document\n")

  for char_count in make_list(get_char_count(text)):
    print(f"The '{char_count["char"]}' character was found {char_count["count"]} times")
  
  print(f"\n--- End report ---")

def get_text(path):
  with open(path) as f:
    return f.read()

def get_word_count(text):
  return len(text.split())

def get_char_count(text):
  char_count = {}

  for char in text.lower():
    if not char.isalpha():
      continue
    if char in char_count:
      char_count[char] += 1
    else:
      char_count[char] = 1

  return char_count

def make_list(dict):
  list = []
  for key, value in dict.items():
    list.append({ "char": key, "count": value })
  list.sort(reverse=True, key=sort_on)
  return list

def sort_on(dict):
  return dict["count"]

main()