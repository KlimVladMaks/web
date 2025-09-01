import socket


def get_user_input():
    print("Введите параметры трапеции:")
    try:
        a = float(input("Длина первого основания (a): "))
        b = float(input("Длина второго основания (b): "))
        h = float(input("Высота (h): "))
        return f"{a},{b},{h}"
    except ValueError:
        print("Ошибка: Некорректный ввод (нужно ввести числовые значения)!")
        return None


def send_request(server_address, data, timeout=5.0):
    try:
        with socket.create_connection(server_address, timeout=timeout) as s:
            s.sendall(data.encode())
            resp = s.recv(1024).decode(errors='replace')
            return resp
    except Exception as e:
        return f"Ошибка соединения: {e}"


def main():
    server_address = ('localhost', 8080)

    try:
        while True:
            data = get_user_input()
            if data is None:
                continue

            print(f"Отправка: {data}")
            response = send_request(server_address, data)
            print(f"Ответ от сервера: {response}")

            choice = input("\nХотите выполнить ещё одно вычисление? (y/n): ").strip().lower()
            if choice != 'y':
                print("Завершение работы клиента")
                break
            print()
    
    except KeyboardInterrupt:
        print("\nКлиент остановлен")
    except Exception as e:
        print(f"\nВозникла ошибка: {e}")


if __name__ == "__main__":
    main()
