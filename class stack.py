#pertama saya mengimprot library dari stack itu sendiri 
from collections import deque
stack = deque()
punctuation = (".,-[]''")
#memasukan contoh oprasi class stack
class Stack:
    def __init__(self):
        self.container = deque()
    def is_empty(self):
        return len(self.container) == 0 
    def push(self,val):
        self.container.append(val) 
    
    def pop(self):
        return self.container.pop()
    
    def top(self):
        return self.container[len(self.container)-1] 

    def size(self):
        return len(self.container)

hasil = Stack()

#open txt dari file yang kita download
n = open("D:python\\SAMPLE DATA.txt","r")
#dari hasil yang kita open lalu di read
text = n.read()
#disini program akan menginput txt nya
input = []
input.append(text)
#lalu selanjutnya kita memberi perintah untuk menghilangkan tanda baca dan memberi simbol apa saja yang harus di hilangkan 
punctuation = ".,-[]''"
punctuation_del = ""
#setelah memberi perintah menghilangkan tanda baca kita melakukan perulangan for 
for i in str(input):
    if i not in punctuation:
        punctuation_del = punctuation_del + i
print(punctuation_del)