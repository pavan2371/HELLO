# class method only we must use cls
class person:                                   
    def __init__(self,fname,lname,age):
        self.fname = fname
        self.lname = lname
        self.age = age


# getter and setter in python

    def getfname(self):
        return self.fname

    def setfname(self,newfname):
        self.fname= newfname


    def getlname(self):
        return self.lname

    def setlname(self,newlname):
        self.lname=newlname

    def getage(self):
        return self.age

    def setage(self,newage):
        self.age = newage