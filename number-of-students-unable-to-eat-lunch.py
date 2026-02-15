def g(array, index):
    """safe get"""
    try:
        return array[index]
    except:
        print("hey it actually demanded I handle this despite not specifying it!")
        # ^ I don't know if it would actually show me this output if this did happen...
        return None

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        new_queue = students.copy()
        curr_queue = []
        while curr_queue != new_queue:
            curr_queue = new_queue.copy()
            new_queue = []
            for s in curr_queue:
                if s == g(sandwiches,0):
                    sandwiches.pop(0)
                else:
                    # the unsatified student returns to the next queue
                    new_queue.append(s)
        return len(new_queue)
