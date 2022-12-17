import json

class Answers:
    def __init__(self) -> None:
        self.file_path = "src/data/answers.json"
        with open(self.file_path, "r", encoding='utf-8-sig') as file:
            self.json_input = json.load(file)
            print(self.json_input)

    def get_info(self):
        return self.json_input

    def get_reply(self, id: int):
        return self.json_input[id]['reply']

    def set_reply(self, id: str, value: bool):
        with open(self.file_path, "w+", encoding='utf-8-sig') as file:
            self.json_input[id]['reply'] = value
            json.dump(self.json_input, file, ensure_ascii=False, indent=4)

    def all_replied(self) -> bool:
        for item in self.json_input.values():
            if item['reply'] == '❌ Не отправил':
                return False
        return True
