class reverse():
    def __init__(self, str):
        self.str = str
        self.index = len(str)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.str[self.index]
    
n = input().strip()
rev = reverse(n)
for chr in rev:
    print(chr, end="")