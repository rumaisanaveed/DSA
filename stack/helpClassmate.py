'''Professor X wants his students to help each other in the chemistry lab.
He suggests that every student should help out a classmate who scored
less marks than him in chemistry and whose roll number appears after
him. But the students are lazy and they don't want to search too far.' \
' They each pick the first roll number after them that fits the criteria.' \
' Find the marks of the classmate that each student picks.
Note: one student may be selected by multiple classmates.'''

class Solution:

    def help_classmate(self,arr,n):
        result = []
        for i in range(len(arr)):
            currentNum = arr[i]
            newArr = arr[i + 1:]
            result.append(self.checkSmallest(newArr, currentNum))
        return result

    def checkSmallest(self,newArr, num):
        for j in newArr:
            if j < num:
                return j
        return -1
s = Solution()
print(s.help_classmate([4 ,8 ,5 ,2 ,25],5))
