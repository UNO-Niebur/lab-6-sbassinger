#WordIndex.py
#Name:Scott Bassinger
#Date:03/01/2026
#Assignment:Lab6-WordIndex

def main():
  #textFile = open("fish.txt", 'r')
  fileName = input("Enter filname: ")
  textFile = open(fileName, 'r')

  words = {} #create an empty dictionary
  line_num = 0

  for line in textFile:
    line_num += 1
    for word in line.split():
      word = word.lower().strip('.,!?;:"-')

      if word in words:
        if words[word][-1] != line_num: #check for duplicates
          words[word].append(line_num)
      else:
        words[word] = [line_num] #add a new word to the dictionary with a list of line numbers
  textFile.close()

  for word in sorted(words):
    print(f"{word}: {words[word]}")

  """print ("fish" in words) #is a word already in the dictionary?
  words["fish"] = [2]     #add a list to the dictionary
  print ("fish" in words) #is the word there now?
  words["fish"].append(5) #add to an existing list
  print(words)"""


if __name__ == '__main__':
  main()
