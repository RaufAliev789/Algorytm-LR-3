import heapq
import random


class Packet:
    def __init__(self, arrival_time, duration):
        self.arrival_time = arrival_time
        self.duration = duration
        self.process_start_time = -1  # Время начала обработки
        self.handled = False  # Статус пакета

    def __lt__(self, other):
        # Правило приоритета: приоритет отрицателен, чтобы пакеты с более высоким приоритетом (меньшее значение) обрабатывались первыми
        return self.arrival_time < other.arrival_time


def simulate(size, packets):
    buffer = []
    output = []
    current_time = 0
    index = 0

    while index < len(packets) or buffer:
        # Добавление пакетов в буфер
        while index < len(packets) and packets[index].arrival_time <= current_time:
            if len(buffer) < size:
                heapq.heappush(buffer, packets[index])
            else:
                # Отброс пакета
                output.append(-1)
            index += 1

        if buffer:
            # Извлечение пакета с наивысшим приоритетом (по времени поступления)
            packet = heapq.heappop(buffer)
            # С шансом на сбой 10%
            if random.random() < 0.1:  # 10% шанс на сбой
                output.append(-1)  # Пакет отклонен
                continue  # Пропускаем текущий пакет
            else:
                # Обработка пакета
                packet.process_start_time = current_time
                output.append(current_time)
                current_time += packet.duration
        else:
            # Если буфер пуст, просто увеличиваем время до следующего пакета
            current_time += 1

    # Заполнение результатов для неотобранных пакетов, если таковые имеются
    while index < len(packets):
        output.append(-1)
        index += 1

    return output


# Чтение входных данных
def main():
    size, n = map(int, input().split())
    packets = []

    for _ in range(n):
        arrival_time, duration = map(int, input().split())
        packets.append(Packet(arrival_time, duration))

    results = simulate(size, packets)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
