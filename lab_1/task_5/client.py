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
            print(f"Ответ сервера: {response.text}")
        except requests.exceptions.ConnectionError:
            print("Ошибка: Не удалось подключиться к серверу")
    
    def show_grades(self):
        try:
            response = requests.get(self.base_url)
            print("Оценки по дисциплинам:")
            print("=" * 30)
            for line in response.text.split('\n'):
                if '<td>' in line:
                    parts = line.strip().replace('<td>', '').replace('</td>', '').split()
                    if len(parts) >= 2:
                        print(f"{parts[0]:<20} {parts[1]}")
        except requests.exceptions.ConnectionError:
            print("Ошибка: Не удалось подключиться к серверу")


def main():
    client = GradeClient()
    print("Консольный клиент для добавления оценок по дисциплинам")
    print("Команды:")
    print("  add - добавить оценку")
    print("  show - показать все оценки")
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

            elif command == 'show':
                client.show_grades()
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
