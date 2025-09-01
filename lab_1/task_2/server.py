import socket

def calculate_trapezoid_area(a, b, h):
    return ((a + b) / 2) * h

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 8080)
    server_socket.bind(server_address)

    server_socket.listen(5)
    print(f"TCP-сервер запущен на {server_address}. Ожидание подключений...")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Подключился клиент: {client_address}")

            data = client_socket.recv(1024).decode()
            print(f"Получено от {client_address}: {data}")

            try:
                a, b, h = map(float, data.split(','))
                response = ""
                if (a <= 0) or (b <= 0) or (h <= 0):
                    response = "Ошибка: a,b,h должны быть положительными числами"
                else:
                    area = calculate_trapezoid_area(a, b, h)
                    response = f"Площадь трапеции: {area:.2f}"

            except ValueError:
                response = "Ошибка: Неверный формат данных. Ожидается: a,b,h"
            except Exception as e:
                response = f"Ошибка при вычислении: {str(e)}"
            
            client_socket.send(response.encode())
            print(f"Отправлен ответ: {response}")
            
            client_socket.close()

    except KeyboardInterrupt:
        print("\nСервер остановлен")
    except Exception as e:
        print(f"\nВозникла ошибка: {str(e)}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
