import requests


class GradeClient:
    def __init__(self, base_url='http://localhost:8000'):
        self.base_url = base_url
    
    def add_grade(self, discipline, grade):
        data = {
            'discipline': discipline,
            'grade': grade
        }
        try:
            response = requests.post(f"{self.base_url}/add", data=data)
            response.encoding = 'utf-8'
            print(f"Ответ сервера: {response.text}")
        except requests.exceptions.ConnectionError:
            print("Ошибка: Не удалось подключиться к серверу")

def main():
    client = GradeClient()
    print("Консольный клиент для добавления оценок по дисциплинам")
    print("Команды:")
    print("  add - добавить оценку")
    print("  exit - выход")
    print()

    while True:
        try:
            command = input("> ").strip()
            if not command:
                continue

            if command == 'add':
                print("\nДобавление новой оценки:")
                discipline = input("Введите название дисциплины: ").strip()
                grade = input("Введите оценку: ").strip()
                if discipline and grade:
                    client.add_grade(discipline, grade)
                else:
                    print("Ошибка: Все поля должны быть заполнены")
                print()

            elif command == 'exit':
                break
            else:
                print("Неизвестная команда.")
        
        except KeyboardInterrupt:
            print("\nВыход...")
            break
        except Exception as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
