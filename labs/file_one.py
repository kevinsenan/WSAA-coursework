#import file_two
from file_two import function_four

print("File one __name__ is set to: {}" .format(__name__))

def function_one():
    print("function one is executed")

def function_two():
    print("function two is executed")

if __name__ == "__main__":
    print("File one executed when run directly")                                           
    function_two()
    #file_two.function_three()
    function_four()
else:
    print("File one executed when imported")

