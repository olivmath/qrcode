import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode
import os
from pyzbar.pyzbar import decode
from PIL import Image


class QRCodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator and Reader")

        self.generate_btn = tk.Button(
            root, text="Generate QR Code", command=self.generate_qr_code
        )
        self.generate_btn.pack(pady=10)

        self.read_btn = tk.Button(root, text="Read QR Code", command=self.read_qr_code)
        self.read_btn.pack(pady=10)

    def generate_qr_code(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Generate QR Code")

        tk.Label(dialog, text="Text for QR Code:").pack(pady=5)
        text_entry = tk.Entry(dialog, width=50)
        text_entry.pack(pady=5)

        tk.Label(dialog, text="File name (without extension):").pack(pady=5)
        name_entry = tk.Entry(dialog, width=50)
        name_entry.pack(pady=5)

        def save_qr_code():
            text = text_entry.get()
            filename = name_entry.get()
            if not text or not filename:
                messagebox.showerror("Error", "Please fill in both fields.")
                return

            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(text)
            qr.make(fit=True)
            img = qr.make_image(fill="black", back_color="white")

            home = os.path.expanduser("~")
            save_path = os.path.join(home, "Downloads", f"{filename}.png")
            img.save(save_path)
            messagebox.showinfo("Success", f"QR Code saved at {save_path}")
            dialog.destroy()

        tk.Button(dialog, text="Generate and Save", command=save_qr_code).pack(pady=10)

    def read_qr_code(self):
        file_path = filedialog.askopenfilename(
            title="Select a QR Code image",
            filetypes=[("Images", "*.png *.jpg *.jpeg")],
        )
        if not file_path:
            return

        try:
            img = Image.open(file_path)
            decoded_objects = decode(img)
            if decoded_objects:
                text = decoded_objects[0].data.decode("utf-8")
                msg = f"'{text}'\n\nClick OK to copy the text"
                messagebox.showinfo(
                    "QR Code Text", msg, command=self.copy_text(text)
                )
            else:
                messagebox.showerror("Error", "No QR Code found in the image.")
        except Exception as e:
            messagebox.showerror("Error", f"Error reading the image: {e}")

    def copy_text(self, text):
        self.root.tk.call("clipboard", "clear")
        self.root.tk.call("clipboard", "append", text)


def main():
    root = tk.Tk()
    app = QRCodeApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
