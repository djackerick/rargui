#!/usr/bin/env python3
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import subprocess
from pathlib import Path
import os

class RarCompressorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RARGUI")
        self.root.geometry("600x440")
        self.root.resizable(True, False)

        self.origen = tk.StringVar()
        self.destino_dir = tk.StringVar()
        self.comando = tk.StringVar(value="(select a source first)")

        self.crear_interfaz()

    def crear_interfaz(self):
        padding = {"padx": 12, "pady": 6}

        # --- Origen ---
        frame_origen = ttk.LabelFrame(self.root, text="Input file/folder", padding=10)
        frame_origen.pack(fill="x", **padding)

        frame_botones_origen = ttk.Frame(frame_origen)
        frame_botones_origen.pack(fill="x", pady=(0, 6))

        ttk.Button(frame_botones_origen, text="Select file",
                   command=self.elegir_archivo).pack(side="left", expand=True, fill="x", padx=(0, 4))
        ttk.Button(frame_botones_origen, text="Select folder",
                   command=self.elegir_carpeta).pack(side="left", expand=True, fill="x", padx=(4, 0))

        ttk.Entry(frame_origen, textvariable=self.origen, state="readonly").pack(fill="x")

        # --- Destino ---
        frame_destino = ttk.LabelFrame(self.root, text="Output folder", padding=10)
        frame_destino.pack(fill="x", **padding)

        ttk.Button(frame_destino, text="Select a different output folder",
                   command=self.elegir_destino).pack(fill="x", pady=(0, 6))

        ttk.Entry(frame_destino, textvariable=self.destino_dir).pack(fill="x")

        # --- Comando ---
        frame_cmd = ttk.LabelFrame(self.root, text="Command to be executed", padding=10)
        frame_cmd.pack(fill="x", **padding)

        ttk.Entry(frame_cmd, textvariable=self.comando, state="readonly").pack(fill="x")

        # --- Botones inferiores ---
        frame_botones = ttk.Frame(self.root)
        frame_botones.pack(fill="x", padx=12, pady=15)

        ttk.Button(frame_botones, text="Compress", command=self.comprimir).pack(side="left", expand=True, fill="x", padx=(0, 6))
        ttk.Button(frame_botones, text="Exit", command=self.root.destroy).pack(side="left", expand=True, fill="x", padx=(6, 0))

        # Versión abajo a la derecha
        version_label = ttk.Label(self.root, text="v1.0 by D'JackeRick", foreground="gray")
        version_label.pack(side="right", padx=12, pady=(0, 8))

    def elegir_archivo(self):
        ruta = filedialog.askopenfilename(title="Select a file")
        if ruta:
            self.origen.set(ruta)
            self.actualizar_destino_por_defecto()
            self.actualizar_comando()

    def elegir_carpeta(self):
        ruta = filedialog.askdirectory(title="Select a folder")
        if ruta:
            self.origen.set(ruta)
            self.actualizar_destino_por_defecto()
            self.actualizar_comando()

    def actualizar_destino_por_defecto(self):
        origen = self.origen.get()
        if not origen:
            return

        path = Path(origen)
        # Tanto si es archivo como carpeta → usamos la carpeta padre
        self.destino_dir.set(str(path.parent))

    def elegir_destino(self):
        ruta = filedialog.askdirectory(title="Select a different output folder")
        if ruta:
            self.destino_dir.set(ruta)
            self.actualizar_comando()

    def actualizar_comando(self):
        origen = self.origen.get()
        destino_dir = self.destino_dir.get()

        if not origen or not destino_dir:
            self.comando.set("(select input and output)")
            return

        nombre = Path(origen).name
        archivo_rar = f"{nombre}.rar"
        ruta_rar = str(Path(destino_dir) / archivo_rar)

        # -m5 = máxima compresión
        cmd = f'rar a -m3 "{ruta_rar}" "{origen}"'
        self.comando.set(cmd)

    def comprimir(self):
        origen = self.origen.get()
        destino_dir = self.destino_dir.get()

        if not origen or not destino_dir:
            messagebox.showwarning("Not enough info", "You must select an input file/folder and/or output directory.")
            return

        if not Path(origen).exists():
            messagebox.showerror("Error", "Source doesn't exist.\nHave you unmounted something?")
            return

        if not os.access(destino_dir, os.W_OK):
            messagebox.showerror("Error", "Output folder doesn't have write permissions")
            self.elegir_destino()
            return
            self.actualizar_comando()
        cmd = self.comando.get()

        try:
            resultado = subprocess.run(cmd, shell=True, capture_output=True, text=True)

            if resultado.returncode == 0:
                messagebox.showinfo("Process completed", "Compression successfully done.")
            else:
                messagebox.showerror("Error with RAR", 
                    f"Output code: {resultado.returncode}\n\n{resultado.stderr or resultado.stdout}")
        except FileNotFoundError:
            messagebox.showerror("Error", "'rar' not found.\nRemember to install it first.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style()
    style.theme_use("clam")
    app = RarCompressorApp(root)
    root.mainloop()
