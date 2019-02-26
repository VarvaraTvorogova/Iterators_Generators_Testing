class RangeIterator:

    def __init__(self, *args):
        self.args = args
        if len(args) == 0:
            raise Exception('At least one argument required')
        if len(args) == 1:
            self.begin = 0
            self.end = self.args[0]
            self.step = 1
        if len(args) == 2:
            self.begin = self.args[0]
            self.end = self.args[1]
            self.step = 1
        if len(args) == 3:
            if self.args[2] == 0:
                raise Exception('RangeIterator arg 3 must not be zero')
            self.begin = self.args[0]
            self.end = self.args[1]
            self.step = self.args[2]
        self.flag = False
        self.lst = []

    def __iter__(self):
        return self

    def   __next__(self):
        if self.flag == False:
            self.flag = True
            if self.begin < self.end and self.step > 0 or self.begin > self.end and self.step < 0:
                self.lst.append(self.begin)
                return self.begin
            else:
                raise StopIteration
        if self.step > 0:
            if self.begin < self.end - self.step:
                self.begin += self.step
                self.lst.append(self.begin)
                return self.begin
            else:
                raise StopIteration
        else:
            if self.begin > self.end - self.step:
                self.begin += self.step
                self.lst.append(self.begin)
                return self.begin
            else:
                raise StopIteration

    def __getitem__(self, index):
        for i in self:
            pass
        return self.lst[index]



class RangeGenerator:

    def __init__(self, *args):
        self.args = args
        if len(args) == 0:
            raise Exception('At least one argument required')
        if len(args) == 1:
            self.begin = 0
            self.end = self.args[0]
            self.step = 1
        if len(args) == 2:
            self.begin = self.args[0]
            self.end = self.args[1]
            self.step = 1
        if len(args) == 3:
            if self.args[2] == 0:
                raise Exception('RangeGenerator arg 3 must not be zero')
            self.begin = self.args[0]
            self.end = self.args[1]
            self.step = self.args[2]
        self.flag = False
        self.lst = []

    def __iter__(self):
        return RangeGenerator.gener(self)

    def gener(self):
        if self.flag == False and self.begin < self.end:
            self.flag = True
            self.lst.append(self.begin)
            yield self.begin
        if self.step > 0:
            while self.begin < self.end - self.step:
                self.begin += self.step
                self.lst.append(self.begin)
                yield self.begin
        else:
            while self.begin > self.end - self.step:
                self.begin += self.step
                self.lst.append(self.begin)
                yield self.begin

    def __getitem__(self, index):
        for i in self:
            pass
        return self.lst[index]


