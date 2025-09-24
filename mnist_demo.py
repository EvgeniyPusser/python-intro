import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms

# 1. Настройка данных (MNIST картинки 28x28)
transform = transforms.Compose([
    transforms.ToTensor(),                # переводим картинку в тензор
    transforms.Normalize((0.5,), (0.5,))  # нормализация (от -1 до 1)
])

train_dataset = datasets.MNIST(
    root="./data", train=True, download=True, transform=transform
)
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=64, shuffle=True)

test_dataset = datasets.MNIST(
    root="./data", train=False, download=True, transform=transform
)
test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=1000, shuffle=False)

# 2. Определяем простую нейросеть
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(28*28, 128)   # вход: 784 пикселя → скрытый слой
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 10)       # выход: 10 цифр (0-9)

    def forward(self, x):
        x = x.view(-1, 28*28)  # превращаем картинку в вектор
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

model = Net()

# 3. Функция потерь и оптимизатор
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 4. Обучение (1 эпоха для примера)
for epoch in range(1):
    for batch_idx, (data, target) in enumerate(train_loader):
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()

        if batch_idx % 200 == 0:
            print(f"Train Epoch: {epoch} [{batch_idx*len(data)}/{len(train_loader.dataset)}]  Loss: {loss.item():.6f}")

# 5. Проверка на тестовых данных
correct = 0
total = 0
with torch.no_grad():
    for data, target in test_loader:
        output = model(data)
        pred = output.argmax(dim=1, keepdim=True)
        correct += pred.eq(target.view_as(pred)).sum().item()
        total += target.size(0)

print(f"\nTest accuracy: {100. * correct / total:.2f}%")
