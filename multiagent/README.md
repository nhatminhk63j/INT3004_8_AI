# MultiAgent

#### Question 1:

Hàm Reflex Agent xét đến các yếu tố:
    
* Khoảng cách manhattan đến con ma gần mình nhất (`x`)
* Số lượng thức ăn của trạng thái đó (`y`) 
* Khoảng thời gian con ma đang sợ mình (`z`)

Score sẽ xét đến các yếu tố sao cho con ma càng gần mình thì score càng thấp, 
nếu con ma đang sợ mình `(y>0)`), đồng thời số lượng thức ăn càng ít thì điểm càng cao.
Sau khi chọn tham số, dùng công thức `-(10/x + 50 * z)` nếu `y = 0` và 
`50 * z` nếu `y > 2` (`2` được xem là khoảng cách an toàn đến ghost).
Score cuối cùng được cộng với score của game khi đó (`gameState.getScore()`)

#### Question 2,3,4:

Cài đặt theo các thuật toán đã học trên lớp và trang chủ, căn chỉnh những 
điều kiện phù hợp với bài toán.

#### Question5:

Sau khi sử dụng bfs, gọi khoảng cách đến thức ăn ngắn nhất là `x`

* Nếu số lượng thức ăn là `0`, hàm trả về `infinity` (tốt nhất có thể)
    
* Nếu pacman quá gần ghost trong khi `scaredTime = 0`, hàm sẽ trả
về `-infinity` (trạng thái tệ, không được phép đến)
    
* Ngược lại, score được tính theo công thức: `gameState.getScore() * 1000 + number_of_foods * 100 + x * 50 `
Hàm này ưu tiên việc lấy được nhiều điểm nhất, sau đó là giảm 
thiểu số lượng thức ăn, tiếp theo là giảm thiểu khoảng cách 
gần nhất đến một thức ăn.