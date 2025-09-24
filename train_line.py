# import torch
# import torch.nn as nn
# import torch.optim as optim

# # Наши данные: две точки (x, y)
# X = torch.tensor([[1.0], [2.0]])
# y = torch.tensor([[5.0], [8.0]])

# # Модель: y = W*x + b
# model = nn.Linear(1, 1)

# # Функция ошибки и оптимизатор
# loss_fn = nn.MSELoss()
# optimizer = optim.SGD(model.parameters(), lr=0.1)

# # Обучение на 10 шагов
# for epoch in range(10):
#     y_pred = model(X)
#     loss = loss_fn(y_pred, y)

#     optimizer.zero_grad()
#     loss.backward()
#     optimizer.step()

#     W, b = model.parameters()
#     print(f"Epoch {epoch}: Loss={loss.item():.4f}, W={W.item():.4f}, b={b.item():.4f}")

import torch
import torch.nn as nn
import torch.optim as optim

# Данные: две точки (x, y)
X = torch.tensor([[1.0], [2.0]])
y = torch.tensor([[5.0], [8.0]])

# Модель: y = W*x + b
model = nn.Linear(1, 1)

# Функция ошибки и оптимизатор
loss_fn = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.1)

# Обучение на 50 шагов
for epoch in range(50):
    # 1. Предсказания
    y_pred = model(X)

    # 2. Ошибка
    loss = loss_fn(y_pred, y)

    # 3. Обновляем параметры
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    # 4. Смотрим параметры модели
    W, b = model.parameters()

    # 5. Печатаем прогресс
    print(
        f"Epoch {epoch:02d}: "
        f"Loss={loss.item():.4f}, "
        f"W={W.item():.4f}, b={b.item():.4f}, "
        f"Pred(x=1)={y_pred[0].item():.4f}, Pred(x=2)={y_pred[1].item():.4f}"
    )
