import sys

number_map = {
   "one": "1",
   "two": "2",
   "three": "3",
   "four": "4",
   "five": "5",
   "six": "6",
   "seven": "7",
   "eight": "8",
   "nine": "9",
}

def isItTextNumber(input):
   for k in number_map:
     if (input.startswith(k)):
         return k
   return None


def process(line):
  result = ''
  while len(line) > 0:
    if line[0].isdigit():
      result += line[0]
      line = line[1:]
      continue

    num = isItTextNumber(line)
    if num is None:
      line = line[1:]
      continue

    result += number_map[num]
    # If words couldn't share letter, we would skip all the letters "used"
    # line = line[len(num):]

    # Since words CAN share letters, we move just 1 letter, so that rest of word can be reused.
    line = line[1:]

  return result

for line in sys.stdin:
  print(process(line))
