import json

class Answers:
    def __init__(self) -> None:
        self.file_path = "src\\data\\answers.json"
        with open(self.file_path, "r", encoding='utf-8-sig') as file:
            self.json_input = json.load(file)
            print(self.json_input)

    def get_info(self, id=None):
        if id is not None:
            return self.json_input[id]['reply']
        return self.json_input

    def set_reply(self, id: str, value: bool):
        with open(self.file_path, "w+", encoding='utf-8-sig') as file:
            self.json_input[id]['reply'] = value
            json.dump(self.json_input, file, ensure_ascii=False, indent=4)
