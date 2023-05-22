## The function class_allocation takes the number of students as input
def class_allocation(total_students):
    #to find out the minimum number of classes needed.
    # here the max function is taking the maximum number of classes starting from 2  as stated in the requirement.
    # 29 is added with total students so that the remaining students are grouped into different class.and as the maximum class size is 30.
   number_of_classes: int = max(2, (total_students+29) // 30)

      #calculate approximate number of students per class using integer division for whole number.
   class_size= total_students // number_of_classes
#it calculates the number of classes which can have extra student.
   large_class= total_students % number_of_classes
   allocation = {}
   for i in range(1, number_of_classes + 1):
        if i <= large_class:
            allocation[f"Class {i}"] = class_size + 1  # allocate extra student to first few classes
        else:
            allocation[f"Class {i}"] = class_size
   print(f"Proposed Allocation: {number_of_classes} classes")
   print(allocation)
class_allocation(31)
class_allocation(59)
class_allocation(87)
