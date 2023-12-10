import numpy as np
import plotly.graph_objects as go
from scipy.optimize import curve_fit

# Задаємо лінійний тренд
def linear_trend(x):
    return 2 * x + 3

# Генеруємо 20 точок з лінійним трендом та додаванням шуму
np.random.seed(42)
x_values = np.linspace(1, 20, 20)
y_values = linear_trend(x_values) + np.random.normal(0, 3, size=20)

# Перетворюємо координати в список
data = list(zip(x_values, y_values))


# Розділення даних на x та y
data_np = np.array(data)
x = data_np[:, 0]
y = data_np[:, 1]

# Лінійна апроксимація
def linear_fit(x, a, b):
    return a * x + b

# Квадратична апроксимація
def quadratic_fit(x, a, b, c):
    return a * x**2 + b * x + c

# Кубічна апроксимація
def cubic_fit(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

# Поліноміальна апроксимація 5-го степеню
def poly_fit_5(x, a, b, c, d, e, f):
    return a * x**5 + b * x**4 + c * x**3 + d * x**2 + e * x + f

# Лінійна фільтрація
def linear_filter(x, y):
    return 0.5 * (x + y)

# Побудова графіків
fig = go.Figure()

# Точки
fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name='Точки'))

# Лінійна апроксимація
popt_linear, _ = curve_fit(linear_fit, x, y)
fig.add_trace(go.Scatter(x=x, y=linear_fit(x, *popt_linear), mode='lines', name='Лінійна апроксимація'))

# Квадратична апроксимація
popt_quadratic, _ = curve_fit(quadratic_fit, x, y)
fig.add_trace(go.Scatter(x=x, y=quadratic_fit(x, *popt_quadratic), mode='lines', name='Квадратична апроксимація'))

# Кубічна апроксимація
popt_cubic, _ = curve_fit(cubic_fit, x, y)
fig.add_trace(go.Scatter(x=x, y=cubic_fit(x, *popt_cubic), mode='lines', name='Кубічна апроксимація'))

# Поліноміальна апроксимація 5-го степеню
popt_poly_5, _ = curve_fit(poly_fit_5, x, y)
fig.add_trace(go.Scatter(x=x, y=poly_fit_5(x, *popt_poly_5), mode='lines', name='Поліноміальна апроксимація 5-го степеню'))

# Лінійна фільтрація
filtered_y = [y[0]]
for i in range(1, len(y)):
    filtered_y.append(linear_filter(y[i - 1], y[i]))
fig.add_trace(go.Scatter(x=x, y=filtered_y, mode='lines', name='Лінійна фільтрація'))

# Налаштування відображення
fig.update_layout(title='Точкові графіки та лінії трендів',
                  xaxis_title='X',
                  yaxis_title='Y')

# Показ графіка
fig.show()
