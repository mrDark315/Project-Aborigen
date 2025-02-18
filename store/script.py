import json

# Загрузка данных из файла
input_filename = "store/data.json"
output_filename = "store/data2.json"

with open(input_filename, "r", encoding="utf-8") as file:
    data = json.load(file)

# Удаление ненужных ключей
keys_to_remove = ["pc_requirements", "mac_requirements", "linux_requirements"]

for entry in data:
    for key in keys_to_remove:
        entry.pop(key, None)

# Сохранение очищенного файла
with open(output_filename, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print(f"Очищенный файл сохранен как {output_filename}")
