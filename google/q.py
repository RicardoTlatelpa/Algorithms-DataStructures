'''
Imagine you want to design a conference booking system

book(start,end)
return bool

book(10,20) -> return true
book(20,30) -> return True
book(5,15) -> return false


We need a datastructure that keeps track of pairs
interval problem


'''
class BookingSystem:
    def __init__(self):
        self.booking = []
    def book(self,start,end):
        if start >= end:
            #invalid interval
            return False
        if len(self.booking) == 0:
            self.booking.append((start,end))
            return True
        else:
            left = 0
            right = len(self.booking)
            
            while(left < right):
                mid = (left + right)//2

                #print(left,right,mid,(start,end))
                (s2,e2) = self.booking[mid]
                # check collision
                # if the input intervals start is within the range of the current interval
                # if the intput intervals end is within the range of the current interval
                # if the current interval start is within the range of the input interval
                # if the current interval end is within the range of the input interval
                if (s2,e2) == (start,end):
                    return False
                if (start >= s2 and start < e2) or (end >= s2 and end <= e2) or (s2 <= end and s2 >= start) or (e2 <= end and e2 > start):
                    print('merge', (start,end))
                    return False
                if start > e2:
                    left = mid + 1
                else:
                    right = mid - 1
        # assuming I know the idx after the bs
        # check for collision here
        print((start,end), self.booking[left])
        if start >= self.booking[0][1]:
            self.booking.insert(left+1,(start,end)) # O(n) time complexity
        else:
            self.booking.insert(left,(start,end))
        return True
    def seeBooking(self):
        print(self.booking)
        

b = BookingSystem()
print(b.book(10,20))
b.seeBooking()
print(b.book(20,30))
b.seeBooking()
print(b.book(1,2))
b.seeBooking()
print(b.book(99,100))
b.seeBooking()
print(b.book(1,100))
b.seeBooking()
print(b.book(20,30))
b.seeBooking()
print(b.book(5,15))
b.seeBooking()
print(b.book(25,30))
b.seeBooking()
