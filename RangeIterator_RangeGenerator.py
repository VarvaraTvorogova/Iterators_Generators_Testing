class RangeFather:

    def __init__(self, *args):
        self.args = args
        if len(args) == 0:
            raise Exception('At least one argument required')
        if len(args) == 1:
            self.current = 0
            self.end = self.args[0]
            self.step = 1
        if len(args) == 2:
            self.current = self.args[0]
            self.end = self.args[1]
            self.step = 1
        if len(args) == 3:
            if self.args[2] == 0:
                raise Exception('Third arg must not be zero')
            self.current = self.args[0]
            self.end = self.args[1]
            self.step = self.args[2]
        self.flag = False
        self.lst = []


class RangeIterator (RangeFather):

    def __iter__(self):
        return self

    def   __next__(self):
        if not self.flag:
            self.flag = True
            if self.current < self.end and self.step > 0 or self.current > self.end and self.step < 0:
                self.lst.append(self.current)
                return self.current
            else:
                raise StopIteration
        if self.step > 0:
            if self.current < self.end - self.step:
                self.current += self.step
                self.lst.append(self.current)
                return self.current
            else:
                raise StopIteration
        else:
            if self.current > self.end - self.step:
                self.current += self.step
                self.lst.append(self.current)
                return self.current
            else:
                raise StopIteration

    def __getitem__(self, index):
        for i in self:
            pass
        return self.lst[index]



class RangeGenerator (RangeFather):

    def __iter__(self):
        return RangeGenerator.gener(self)

    def gener(self):
        if not self.flag and self.current < self.end:
            self.flag = True
            self.lst.append(self.current)
            yield self.current
        if self.step > 0:
            while self.current < self.end - self.step:
                self.current += self.step
                self.lst.append(self.current)
                yield self.current
        else:
            while self.current > self.end - self.step:
                self.current += self.step
                self.lst.append(self.current)
                yield self.current

    def __getitem__(self, index):
        for i in self:
            pass
        return self.lst[index]


def genert(*args):
    args = args
    if len(args) == 0:
        raise Exception('At least one argument required')
    if len(args) == 1:
        current = 0
        end = args[0]
        step = 1
    if len(args) == 2:
        current = args[0]
        end = args[1]
        step = 1
    if len(args) == 3:
        if args[2] == 0:
            raise Exception('arg 3 must not be zero')
        current = args[0]
        end = args[1]
        step = args[2]
    flag = False
    if not flag and current < end:
        flag = True
        yield current
    if step > 0:
        while current < end - step:
            current += step
            yield current
    else:
        while current > end - step:
            current += step
            yield current




