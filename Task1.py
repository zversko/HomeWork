# Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141 10^(-1) ≤ d ≤10^(-10)

from datetime import datetime
import time

def main():
    start_time = datetime.now()
    pi = 0
    for i in range(1, 100000000000, 12):
        pi = pi + 4/i - 4/(i+2) + 4/(i+4) - 4/(i+6) + 4/(i+8) - 4/(i+10)
        # Если сделать так 4/i - 4/(i+2), то до 100 млрд занимает 1 час и 20 минут
        # Если так 4/i - 4/(i+2) + 4/(i+4) - 4/(i+6) + 4/(i+8) - 4/(i+10), то занимает 41 минуту

    print(round(pi, 3))
    print(datetime.now() - start_time)
        
main()