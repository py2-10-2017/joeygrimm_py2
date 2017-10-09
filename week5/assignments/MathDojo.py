class MathDojo(object):
    def __init__(self,total=0):
        self.total=total
    def add(self, *args):
        for arg in args:
            if type(arg) is list or type(arg) is tuple:
                for num in arg:
                    self.total += num
            else:
                self.total += arg
        return self
    def subtract(self, *args):
        for arg in args:
            if type(arg) is list or type(arg) is tuple:
                for num in arg:
                    self.total -= num
            else:
                self.total -= arg
        return self
    def displaytotal(self):
        print "You have a total of {}\n".format(self.total)
        return self

md = MathDojo()

md.displaytotal().add(2, 8).displaytotal().subtract(3,7).displaytotal()