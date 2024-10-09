class Stack:
    def __init__(self, limit_stack): #Hàm tạo để khởi tạo Stack với limit nhất định
        self.limit_stack = limit_stack
        self.stack = []
        self.count = 0

    def push(self, item): #Hàm thêm một phần tử vào Stack
        if self.isFull():
            print("Stack đầy")
        else:
            self.stack.append(item)
            self.count += 1

    def pop(self): #Hàm lấy một phần tử ra từ đỉnh Stack
        if self.isEmpty():
            print("Stack trống")
            return None
        else:
            self.count -= 1
            return self.stack.pop()

    def isEmpty(self): #Hàm để kiểm tra Stack có trống không
        return self.count == 0

    def isFull(self): #Hàm để kiểm tra Stack có đầy không
        return self.count == self.limit_stack

    def count(self): #Hàm trả về số phần tử hiện tại trong Stack
        return self.count

    def printStack(self): #Hàm in nội dung của Stack
        print("Nội dung của Stack:", self.stack)

#Nhập các giá trị bất kì để sử dụng lớp Stack và in ra kết quả:
stack = Stack(4)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.printStack()  
print("Số phần tử của Stack:", stack.pop())  
stack.printStack()  