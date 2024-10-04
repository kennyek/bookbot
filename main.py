def main():
  with open("books/frankenstein.txt") as f:
    text = f.read()
    print(word_count(text))

def word_count(text):
  return len(text.split())

main()