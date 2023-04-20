# Implement a SnapshotArray that supports the following interface: 
# 
#  
#  SnapshotArray(int length) initializes an array-like data structure with the 
# given length. Initially, each element equals 0. 
#  void set(index, val) sets the element at the given index to be equal to val. 
# 
#  int snap() takes a snapshot of the array and returns the snap_id: the total 
# number of times we called snap() minus 1. 
#  int get(index, snap_id) returns the value at the given index, at the time we 
# took the snapshot with the given snap_id 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: ["SnapshotArray","set","snap","set","get"]
# [[3],[0,5],[],[0,6],[0,0]]
# Output: [null,null,0,null,5]
# Explanation: 
# SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
# snapshotArr.set(0,5);  // Set array[0] = 5
# snapshotArr.snap();  // Take a snapshot, return snap_id = 0
# snapshotArr.set(0,6);
# snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= length <= 5 * 10⁴ 
#  0 <= index < length 
#  0 <= val <= 10⁹ 
#  0 <= snap_id < (the total number of times we call snap()) 
#  At most 5 * 10⁴ calls will be made to set, snap, and get. 
#  
# 
#  Related Topics Array Hash Table Binary Search Design 👍 2161 👎 310


# leetcode submit region begin(Prohibit modification and deletion)
class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.lst = [[(0, 0)] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self.lst[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        lst = self.lst[index]
        l = 0
        r = len(lst)
        while l < r:
            mid = l + (r - l) // 2
            if lst[mid][0] > snap_id:
                r = mid
            else:
                l = mid + 1
        return lst[l - 1][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
# leetcode submit region end(Prohibit modification and deletion)
