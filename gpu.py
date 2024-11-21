import torch
import torch.nn as nn
import torch.optim as optim

# SimpleModel 정의
class SimpleModel(nn.Module):
    def __init__(self, input_size, output_size=512):
        super(SimpleModel, self).__init__()
        self.fc1 = nn.Linear(input_size, 1024)  # 중간 계층 추가
        self.fc2 = nn.Linear(1024, output_size)  # 최종 출력 크기

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# 데이터 생성
batch_size = 8  # 배치 크기를 줄여 메모리 사용량 감소
input_size = 2048  # 입력 크기 조정
data = torch.randn(batch_size, input_size).to('cuda')  # GPU로 데이터 이동

# 모델 초기화
output_size = 512
model = SimpleModel(input_size, output_size).to('cuda')  # 모델도 GPU로 이동

# 혼합 정밀도 활성화
scaler = torch.cuda.amp.GradScaler()

# 손실 함수와 옵티마이저 설정
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 타겟 데이터 생성
target = torch.randn(batch_size, output_size).to('cuda')

# 학습 루프
num_epochs = 5
for epoch in range(num_epochs):
    # 순전파 및 역전파 (혼합 정밀도 사용)
    with torch.cuda.amp.autocast():  # 혼합 정밀도 활성화
        outputs = model(data)
        loss = criterion(outputs, target)
    
    optimizer.zero_grad()
    scaler.scale(loss).backward()  # 스케일링된 그래디언트로 역전파
    scaler.step(optimizer)
    scaler.update()

    print(f"Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}")

# 결과 확인
print("Training complete!")
