"""
Find the Median of a Number Stream (medium)

Problem Statement:
    Design a class to calculate the median of a number stream. The class should have the 
    following two methods:
        1. insertNum(int num): stores the number in the class
        2. findMedian(): returns the median of all numbers inserted in the class
    If the count of numbers inserted in the class is even, the median will be the average of the
    two middle numbers.

Example 1:
    insertNum(3)
    insertNum(1)
    findMedian(): output -> 2
    insertNum(5)
    findMedian(): output -> 3
    insertNum(4)
    findMedian(): output -> 3.5
"""

class MedianOfAStream:
  def insert_num(self, num):
   # TODO: Write your code here
   return -1

  def find_median(self):
    # TODO: Write your code here
    return 0.0


def main():
  medianOfAStream = MedianOfAStream()
  medianOfAStream.insert_num(3)
  medianOfAStream.insert_num(1)
  print("The median is: " + str(medianOfAStream.find_median()))
  medianOfAStream.insert_num(5)
  print("The median is: " + str(medianOfAStream.find_median()))
  medianOfAStream.insert_num(4)
  print("The median is: " + str(medianOfAStream.find_median()))


main()
