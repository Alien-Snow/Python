class PriorityQ(object):
    """This is a partial implementation of a priority queue"""
    def __init__(self) :
        self.q = []

    def Swap(self) :
        i = (len(self.q) - 1)
        while i > 0 :
            if (int(self.q[i]["priority"]) > int(self.q[i - 1]["priority"])) :
                temp = self.q[i - 1]
                self.q[i - 1] = self.q[i]
                self.q[i] = temp
            i -= 1
        return

    def push(self, key) :
        self.q.append(key)
        if len(self.q) > 1 :
            self.Swap()
        return