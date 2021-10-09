
















def slist_min(self):
    min1 = self.head.data
    temp = self.head

    while temp is not None:
        if(temp.data>min1):
            pass
        elif(temp.data<min1):
            min1 = temp.data

        temp = temp.addr
    return min1