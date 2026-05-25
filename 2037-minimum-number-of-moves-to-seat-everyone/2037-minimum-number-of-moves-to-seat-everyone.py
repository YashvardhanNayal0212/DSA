class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        s=0
        for i in range (len(students)):
            n=abs(students[i]-seats[i])
            s+=n
        return s