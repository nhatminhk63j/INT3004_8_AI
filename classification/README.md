# **Project 5: Classification**

#### Q1 (PASSED):
Câu 1 implement lại theo công thức đã được cho ở bài giảng. 
Ta sẽ cập nhập weight của vector dựa trên thuật toán đã cho qua một
số bước nhất định được quy định bởi autograder.

#### Q2 (PASSED):
Thực hiện trích chọn ra 100 features quan trọng nhất bằng cách sort theo score.
#### Q3 (PASSED):
Duyệt qua tất cả các C trong Cgrid, sau đó thực hiện tối ưu mô hình và chọn C
có accuracy lớn nhất. Weigted vector có giá trị bằng giá trị weighted vector 
ứng với C có accuracy lớn nhất.
#### Q4 (PASSED):
Dựa theo gợi ý của đề bài, ta sẽ thêm features mới dựa theo số thành phần bit 0 liên thông.
Ban đầu, sử dụng breath first searchh để đếm số lượng thành phần liên thông của một hình ảnh.
Gọi số lượng thành phần liên thông là n. Ta sẽ có thêm 3 features nhận giá trị 0 hoặc 1, ứng
với số lượng thành phần liên thông có lớn hơn 1 hay không, lớn hơn 3 hay không và lớn hơn 5 
hay không.
#### Q5 (PASSED):
Thực hiện cài đặt y như hướng dẫn trên đề bài.
#### Q6 (PASSED):
Các features được định nghĩa như sau:
* number_of_foods: Số lượng thức ăn hiện tại.
* minumum_scare_times: Thời gian nhỏ nhất mà con ma đang sợ mình
* stop: Có đang ở trạng thái dừng ở trạng thái sau đó hay không.
* nearest_ghost: Khoảng cách manhattan đến con ma gần nhất.
* nearest_food: Khoảng cách đến thức ăn gần nhất.
* optimize_num_capsules: Maximum của hiệu giữa khoảng cách manhattan giữa vị trí hiện
tại và capsules gần nhất giữa thời điểm hiện tại và thời điểm sau khi thực hiện actions.