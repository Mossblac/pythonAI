from functions.write_files import write_file

def main():
  print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
  print("--------------------------------------")
  print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor amet"))
  print("--------------------------------------")
  print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
  print("--------------------------------------")



main()
