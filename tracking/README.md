# Tracking

## 18020979 - Ngô Sách Nhật 

### Mô tả

#### Question 1: Exact Inference Observation

- thêm vào hàm `observe` ở `ExactInference` trong `inference.py` để cập nhật xác suất phân bố vị trí của ghost qua cảm biến của PacMan

```python
  python autograder.py -q q1
```

#### Question 2: Exact Inference with Time Elapse

- thêm hàm `elapseTime` ở `ExactInference` trong `inference.py`
- nhờ vào phân phối hành động của ghost qua `getPositionDistribution` và vị trí trước của ghost để đánh giá vị trí của ghost có thể đi tiếp qua mỗi bước thời gian

Example of GoSouthGhostAgent:

```python
  python autograder.py -t test_cases/q2/2-ExactElapse
```

```python
  python autograder.py -q q2 --no-graphics
```

#### Question 3: Exact Inference Full Test

- sử dụng đồng thời 2 tính năng `observe` và `elapseTime` để săn ma
- thêm tính năng `chooseAction` ở `GreedyBustersAgent` trong `bustersAgents.py`
- sử dụng chiên thuật tham lam để tới con ma gần nhất theo vị trí được đánh giá (belief)

```python
  python autograder.py -q q3 --no-graphics
```

#### Question 4: Approximate Inference Observation

- thêm `initializeUniformly`, `getBeliefDistribution`, and `observe` cho class `ParticleFilter` trong `inference.py` để thêm 1 thuật toán bộ lọc particle để định vị ghost
- nếu thêm tính năng đúng thì sẽ:
  (1) Khi tất cả particles nhận sức nặng bằng 0 dựa trên chứng cứ thì lấy các hạt từ trước để khôi phục
  (2) Khi một con ghost bị ăn, cập nhật tất cả các particles để con ghost đấy ở vị trí nhốt như mô tả trong `observe`

```python
  python autograder.py -q q4 --no-graphics
```

#### Question 5: Approximate Inference with Time Elapse

- thêm `elapseTime` cho class `ParticleFilter` trong `inference.py` để so sánh với `ExactInference`
- việc test sẽ test `elapseTime` tách biệt và sự dùng tính năng cả bộ lọc particle bằng việc kết hợp `elapseTime` và `observe`

Example of GoSouthGhostAgent:

```python
  python autograder.py -t test_cases/q5/2-ParticleElapse
```

```python
  python autograder.py -q q5 --no-graphics
```

#### Question 6: Joint Particle Filter Observation

- đối phó với ghost `DispersingGhost` dùng hành động là tránh những con ma khác. Vì việc mô hình chuyển tiếp không còn độc lập => tất cả ma phải được theo dỗi ở mạng lưới Baynet
- thêm bộ lọc particle mà liên tục theo dõi nhiều ma
- thêm `initializeParticles`, `getBeliefDistribution`, and `observeState` trong `JointParticleFilter` để đánh giá và lấy lại các mẫu của particles dựa trên bằng chứng
- nếu thêm tính năng đúng thì sẽ:
  (1) Khi tất cả particles nhận sức nặng bằng 0 dựa trên chứng cứ thì lấy các hạt từ trước để khôi phục
  (2) Khi một con ghost bị ăn, cập nhật tất cả các particles để con ghost đấy ở vị trí nhốt như mô tả trong `observe`

```python
  python autograder.py -q q6 --no-graphics
```

#### Question 7: Joint Particle Filter with Elapse Time

- hoàn thành `elapseTime` trong `JointParticleFilter` để lấy mẫu cho mỗi particle cho lưới Baynet

```python
  python autograder.py -q q7 --no-graphics
```
