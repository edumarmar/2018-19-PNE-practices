# Example of reading a file located
# in our local file system

name = 'mynotes.txt'

# open the file
file = open(name, 'r')
print('File opened: {}'.format(file.name))

contents = file.read()

print('the file contents are: {}'.format(contents))

file.close()

f= open(name, 'a')
f.write('This is the text that i am going to add to my file')
f.close()
print('the end')