#import file_one

print("File two __name__ is set to: {}" .format(__name__))

def function_three():
    print("function three is executed")

def function_four():
    print("function four is executed")

if __name__ == "__main__":
    print("File two executed when run directly")
else:
    print("File two executed when imported")
