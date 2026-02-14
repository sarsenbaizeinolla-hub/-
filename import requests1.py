import requests
import json
import os
import tkinter as tk
from tkinter import messagebox


class JsonLoader:
    def __init__(self, url, folder):
        self.url = url
        self.folder = folder

    def load_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Ошибка загрузки данных")

    def save_items(self, items):
        os.makedirs(self.folder, exist_ok=True)

        for item in items:
            filename = os.path.join(self.folder, f"post_{item['id']}.json")
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(item, f, indent=4, ensure_ascii=False)


class AppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("JSON Loader")
        self.root.geometry("300x150")

        self.loader = JsonLoader(
            "https://jsonplaceholder.typicode.com/posts",
            "json_data"
        )

        self.label = tk.Label(root, text="Загрузка JSON в файлы", font=("Arial", 12))
        self.label.pack(pady=15)

        self.button = tk.Button(
            root,
            text="Загрузить и сохранить",
            command=self.run
        )
        self.button.pack(pady=10)

    def run(self):
        try:
            data = self.loader.load_data()
            self.loader.save_items(data)
            messagebox.showinfo("Успех", "Файлы успешно сохранены")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = AppGUI(root)
    root.mainloop()
