import tkinter as tk
from tkinter import filedialog

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Gelişmiş Not Defteri")
        self.text_area = tk.Text(root, wrap=tk.WORD)
        self.text_area.pack(expand="true", fill="both")

        # Liste kutusu oluştur
        self.listbox = tk.Listbox(root)
        self.listbox.pack(expand="true", fill="both")

        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Aç", command=self.open_file)
        file_menu.add_command(label="Kaydet", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Çıkış", command=self.root.quit)
        menubar.add_cascade(label="Dosya", menu=file_menu)
        self.root.config(menu=menubar)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Metin Dosyaları", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Metin Dosyaları", "*.txt")])
        if file_path:
            content = self.text_area.get(1.0, tk.END)
            with open(file_path, "w") as file:
                file.write(content)

if __name__ == "__main__":
    root = tk.Tk()
    app = Notepad(root)
    root.mainloop()
