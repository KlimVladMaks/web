import socket
import threading


class ChatClient:
    def __init__(self, host='localhost', port=8000):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.running = True
    
    def receive_messages(self):
        while self.running:
            try:
                message = self.client_socket.recv(4096).decode('utf-8')
                if message:
                    print(f"\r{message}\n[Вы] ", end="", flush=True)
            except:
                print("\r[СЕРВЕР] Соединение разорвано")
                self.running = False
                break
    
    def send_message(self, message):
        try:
            self.client_socket.send(message.encode('utf-8'))
        except:
            print("[ОШИБКА] Не удалось отправить сообщение")
    
    def start(self):
        print("Многопользовательский чат")
        username = input("Введите ваше имя: ")
        
        try:
            self.client_socket.connect((self.host, self.port))
            self.send_message(username)

            receive_thread = threading.Thread(target=self.receive_messages)
            receive_thread.daemon = True
            receive_thread.start()

            print("\nДобро пожаловать в чат! Для выхода введите '/exit'")
            print("[Вы] ", end="")

            while self.running:
                try:
                    message = input()
                    if message.lower() == '/exit':
                        self.running = False
                        break
                    if message.strip():
                        self.send_message(message)
                    print("[Вы] ", end="")

                except KeyboardInterrupt:
                    self.running = False
                    break
                except Exception as e:
                    print(f"[ОШИБКА] {e}")
                    break
        
        except ConnectionRefusedError:
            print("[ОШИБКА] Не удалось подключиться к серверу")
        except Exception as e:
            print(f"[ОШИБКА] {e}")
        finally:
            self.running = False
            self.client_socket.close()
            print("\nДо свидания!")


if __name__ == "__main__":
    client = ChatClient()
    client.start()
