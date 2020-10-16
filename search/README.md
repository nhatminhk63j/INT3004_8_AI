# INT3004_8_AI Thầy Trần Quốc Long

## Tài liệu tham khảo :
- Slide bài giảng.
- Google (Python tutorial, Search algorithms).
- Berkeley AI Materials.

## Giải quyết vấn đề

### 1. Search

#### Problem 1 : Finding a Fixed Food Dot using Depth First Search
Tìm kiếm theo chiều sâu : Sử dụng một stack lưu trữ các node có thể di chuyển và cho agent có thể di chuyển liên tục theo hướng của các node này. 
Hàm dừng lại khi stack rỗng ( hết đường đi ) hoặc đã tìm được thức ăn.

### Problem 2 : Breadth First Search
Tìm kiếm theo chiều rộng : Sử dụng một queue lưu trữ các nước đi có thể của agent. Agent sẽ thử đi lần lượt từng nước đi có thể theo chiều rộng.
Hàm dừng lại khi queue rỗng ( hết đường đi ) hoặc đã tìm được thức ăn.
Sử dụng một trace state lưu lại trạng thái di chuyển của các trường hợp theo kiểu linkedlist trace[current_node] = (next_node, action). Lấy ra hướng di chuyển của agent từ trace.

### Problem 3 : Varying the Cost Function
Sử dụng thuật toán A* với hueristic = 0

### Problem 4 : A* search
Sử dụng một priority queue để lưu trạng thái nước đi có thể của agent theo đối số cost + hueristic ( trong trường hợp này thì hueristic = 0 ). Các hướng di chuyển của agent sẽ được pop ra từ hàng đợi. Kết quả sẽ đưa ra được đường đi tới thức ăn có đường đi ngắn nhất. (Tương tự thuật toán Dijkstra ).

### Problem 5 : Finding All the Corners
Sử dụng trạng thái ban đầu bao gồm : vị trí, mảng boolean visited_corner = (Fasle, False, Fasle, Fasle). Khi di chuyển qua corner nào thì sẽ đặt giá trị của nó tương ứng về True.
Viết hàm getSuccessors để lấy ra nước đi ( kiểm tra va chạm tường, kiểm tra xem đã đi qua corner chưa, trả về state ( bao gồm vị trí mới và trạng thái của visited_corner mới ), action và cost = 1 )

### Problem 6 : Corners Problem: Heuristic
Sử dụng khoảng cách manhatan từ corner[index] -> position (lấy từ state)

### Problem 7 : Eating All The Dots
Sử thuật toán A* và tạo một custom problem search (có goals : mảng boolean khi ăn thức ăn ở vị trí index thì goals[index] sẽ Fasle, bao giờ mảng này true hết thì hàm isGoalState() return True.

### Problem 8 : Suboptimal Search
Tương tự pr 
