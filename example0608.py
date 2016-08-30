# coding=utf-8

"""
An example of reading and writing Unicode string:Writes
a Unicode string to a file in UTF-8 and reads it back in.
"""

CODEC = 'utf-8'
File = 'unicode.txt'

hello_out = u'ありがとう　大家'
bytes_out = hello_out.encode(CODEC)
f = open(File, 'w')
f.write(bytes_out)
f.close()

f = open(File, 'r')
bytes_in = f.read()
f.close()

hello_in = bytes_in.decode(CODEC)
print hello_in
