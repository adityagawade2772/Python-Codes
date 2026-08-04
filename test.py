# Roxiler system coding que
def demo():
    students = [
      { "name": "John", "grade": "A" },
      { "name": "Alice", "grade": "B" },
      { "name": "Bob", "grade": "A" },
      { "name": "David", "grade": "C" }
    ]
    result = {}
    
    for std in students:
        grade = std["grade"]
        name = std["name"]
        
        if grade not in result:
            result[grade] = []
            
        result[grade].append(name)
    
    return result
    
    
a = demo()
print(a)