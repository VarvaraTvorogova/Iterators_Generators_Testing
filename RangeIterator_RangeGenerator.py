class RangeBase:

    def __init__(self, *args):
        self.args = args
        if len(args) == 0:
            raise Exception('At least one argument required')
        if len(args) == 1:
            self.begin = 0
            self.current = 0
            self.end = self.args[0]
            self.step = 1
        if len(args) == 2:
            self.begin = self.args[0]
            self.current = self.args[0]
            self.end = self.args[1]
            self.step = 1
        if len(args) == 3:
            if self.args[2] == 0:
                raise Exception('Third arg must not be zero')
            self.begin = self.args[0]
            self.current = self.args[0]
            self.end = self.args[1]
            self.step = self.args[2]


class RangeIterator(RangeBase):

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0:
            if self.current < self.end:
                self.current += self.step
                return self.current - self.step
            else:
                raise StopIteration
        else:
            if self.current > self.end:
                self.current += self.step
                return self.current - self.step
            else:
                raise StopIteration

    def __getitem__(self, index):
        if index >= 0:
            return self.begin + index * self.step
        else:
            return self.end + index * self.step


class RangeGenerator(RangeBase):

    def __iter__(self):
        return RangeGenerator.gener(self)

    def gener(self):
        if self.step > 0:
            while self.current < self.end:
                self.current += self.step
                yield self.current - self.step
        else:
            while self.current > self.end:
                self.current += self.step
                yield self.current - self.step

    def __getitem__(self, index):
        if index >= 0:
            return self.begin + index * self.step
        else:
            return self.end + index * self.step


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
            raise Exception('Third arg must not be zero')
        current = args[0]
        end = args[1]
        step = args[2]
    if step > 0:
        while current < end:
            current += step
            yield current - step
    else:
        while current > end:
            current += step
            yield current - step
