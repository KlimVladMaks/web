import socket


def main():
    host = 'localhost'
    port = 8080

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"Сервер запущен на http://{host}:{port}")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Подключение от: {client_address}")
            client_socket.settimeout(5.0)

            try:
                request = client_socket.recv(1024).decode('utf-8')
                print(f"Получен запрос:\n{request}")

                response_headers = [
                    "HTTP/1.1 200 OK",
                    "Content-Type: text/html; charset=utf-8",
                    "Connection: close"
                ]

                try:
                    with open('index.html', 'r', encoding='utf-8') as file:
                        html_content = file.read()
                except FileNotFoundError:
                    html_content = "<h1>Ошибка: файл index.html не найден</h1>"
                
                response = "\r\n".join(response_headers) + "\r\n\r\n" + html_content
                client_socket.sendall(response.encode('utf-8'))
                print("Ответ с HTML-страницей отправлен")
            
            except socket.timeout:
                    print(f"Таймаут при чтении данных от {client_address}")
            except Exception as e:
                print(f"Ошибка при обработке запроса: {e}")
            finally:
                client_socket.close()
                print(f"Соединение с {client_address} закрыто\n")
    
    except KeyboardInterrupt:
        print("\nСервер остановлен")
    except Exception as e:
        print(f"Ошибка сервера: {e}")
    finally:
        server_socket.close()


if __name__ == "__main__":
    main()
