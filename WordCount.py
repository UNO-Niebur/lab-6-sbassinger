#WordCount.py
#Name:Scott Bassinger
#Date:03/01/2026
#Assignment:Lab6-WordCount

def main():

  filename = input("Enter filename: ")
  try:

    #textFile = open("gettysberg.txt", 'r')
    textFile = open(filename, 'r')
    content = textFile.read()
    textFile.close()
    
    lines = len(content.split('\n'))
    words = len(content.split())
    chars = len(content)

    print(f"Lines: {lines}")
    print(f"Words: {words}")
    print(f"Characters: {chars}")
  
  except FileNotFoundError:
    print("Error:File not found")
  

if __name__ == '__main__':
  main()
