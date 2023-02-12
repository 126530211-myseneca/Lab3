#!/usr/bin/env python3 

def write_text_file(file_name, c_name):
	f = open(file_name, 'w')
	f.write('Line 1\nLine 2 is a little longer\nLine 3 is as well\n')
	f.write('This is the 4th line\n')
	f.write('Last line in file\n')
	f.write('copyright@' + c_name)
	f.close()
	print("File written successfully!")

def read_file_string(file_name):
        #Takes file_name as string for a file name, returns its entire contents as a string 
        f = open(file_name, 'r')
        return f.read()

def helloWorld():
    print("Hello World")


if __name__ == '__main__':
	file_name = input("Enter the file name you want to write .txt:")
	c_name = input("Enter your name: ")
	write_text_file(file_name, c_name)
	print(read_file_string(file_name))                                                                                                      
    	helloWorld()
