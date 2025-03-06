def truy_cap_phan_tu(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element, last_element
#Nhập tupple từ người dùng
input_tuple = eval(input("Nhập tupple, ví dụ (1 ,2 , 3):  "))
first, last = truy_cap_phan_tu(input_tuple)
#in kết quả
print("Phần tử đầu tiên :", first)
print("Phần tử cuối cùng :", last)