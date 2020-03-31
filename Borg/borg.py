class Borg(object):
    __shared_state = {}
    def __init__(self):
        self.__dict__ = self.__shared_state

class IBorg(Borg):
    def __init__(self):
        Borg.__init__(self)
        self.state = 'init'
    
    def __str__(self):
        return self.state

def main():
    i1 = IBorg()
    i2 = IBorg()

    print(i1.state, i2.state)

    print("i1 id={} state={} i1.state id = {}".format(id(i1), i1, id(i1.state)))
    print("i2 id={} state={} i2.state id = {}".format(id(i2), i2, id(i2.state)))

if __name__=="__main__":
    main()