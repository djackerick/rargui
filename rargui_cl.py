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
        self.root.geometry("600x390")
        self.root.resizable(True, True)

        self.origen = tk.StringVar()
        self.destino_dir = tk.StringVar()
        self.comando = tk.StringVar(value="(selecciona un origen primero)")
        self.comando_visible = False

        self.crear_interfaz()

    def crear_interfaz(self):
        padding = {"padx": 12, "pady": 6}

        # --- Origen ---
        frame_origen = ttk.LabelFrame(self.root, text="Paso 1", padding=10)
        frame_origen.pack(fill="x", **padding)

        frame_botones_origen = ttk.Frame(frame_origen)
        frame_botones_origen.pack(fill="x", pady=(0, 6))

        ttk.Button(frame_botones_origen, text="Elige un archivo",
                   command=self.elegir_archivo).pack(side="left", expand=True, fill="x", padx=(0, 4))
        ttk.Button(frame_botones_origen, text="Elige una carpeta",
                   command=self.elegir_carpeta).pack(side="left", expand=True, fill="x", padx=(4, 0))

        ttk.Entry(frame_origen, textvariable=self.origen, state="readonly").pack(fill="x")

        # --- Destino ---
        frame_destino = ttk.LabelFrame(self.root, text="Paso 2 (si querí no más)", padding=10)
        frame_destino.pack(fill="x", **padding)

        ttk.Button(frame_destino, text="Cambia la carpeta de salida",
                   command=self.elegir_destino).pack(fill="x", pady=(0, 6))

        ttk.Entry(frame_destino, textvariable=self.destino_dir).pack(fill="x")

        # --- Botón para mostrar/ocultar comando ---
        self.btn_toggle_cmd = ttk.Button(self.root, text="⏬  Muéstrame qué wea voy a hacer:", command=self.toggle_comando)
        self.btn_toggle_cmd.pack(fill="x", padx=12, pady=(6, 0))

        # --- Comando (oculto por defecto) ---
        self.frame_cmd = ttk.LabelFrame(self.root, text="Comando que se ejecutará", padding=10)
        ttk.Entry(self.frame_cmd, textvariable=self.comando, state="readonly").pack(fill="x")
        # No hacemos .pack() todavía → queda oculto

        # --- Botones inferiores ---
        frame_botones = ttk.Frame(self.root)
        frame_botones.pack(fill="x", padx=12, pady=15)

        ttk.Button(frame_botones, text="Paso 3: Estruja", command=self.comprimir).pack(side="left", expand=True, fill="x", padx=(0, 6))
        ttk.Button(frame_botones, text="Salir", command=self.root.destroy).pack(side="left", expand=True, fill="x", padx=(6, 0))

        # Versión abajo a la derecha
        version_label = ttk.Label(self.root, text="v1.0.1 by D'JackeRick", foreground="gray")
        version_label.pack(side="right", padx=12, pady=(0, 8))

    def elegir_archivo(self):
        ruta = filedialog.askopenfilename(title="Elige un archivo")
        if ruta:
            self.origen.set(ruta)
            self.actualizar_destino_por_defecto()
            self.actualizar_comando()

    def elegir_carpeta(self):
        ruta = filedialog.askdirectory(title="Elige una carpeta")
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
        ruta = filedialog.askdirectory(title="Cambia la carpeta de salida")
        if ruta:
            self.destino_dir.set(ruta)
            self.actualizar_comando()

    def toggle_comando(self):
        if self.comando_visible:
            self.frame_cmd.pack_forget()
            self.btn_toggle_cmd.config(text="⏬  Muéstrame qué wea voy a hacer:")
            self.comando_visible = False
        else:
            self.frame_cmd.pack(fill="x", padx=12, pady=6)
            self.btn_toggle_cmd.config(text="⏫  Ok, ocúltalo, no entendí ni pico.")
            self.comando_visible = True

    # Auto-ajustar el tamaño de la ventana
            self.root.update_idletasks()
            nueva_altura = self.root.winfo_reqheight()
            ancho_actual = self.root.winfo_width()
            self.root.geometry(f"{ancho_actual}x{nueva_altura}")

    def actualizar_comando(self):
        origen = self.origen.get()
        destino_dir = self.destino_dir.get()

        if not origen or not destino_dir:
            self.comando.set("(primero elige qué wea querí comprimir y dónde dejarlo)")
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
            messagebox.showwarning("Completa la weá", "Elige tu wea de archivo y dónde vai a dejarlo.")
            return

        if not Path(origen).exists():
            messagebox.showerror("Aweonao", "Desconectaste el pendrai o me moviste\nel archivo que iba a comprimir.")
            return

        if not os.access(destino_dir, os.W_OK):
            messagebox.showerror("Aweonao", "No puedo escribir en la carpeta culiá que elegiste\npa' guardar tu cagá de archivo")
            self.elegir_destino()
            return
            self.actualizar_comando()
        cmd = self.comando.get()

        try:
            resultado = subprocess.run(cmd, shell=True, capture_output=True, text=True)

            if resultado.returncode == 0:
                messagebox.showinfo("Ya acabé", "¿Un puchito ahora?")
            else:
                messagebox.showerror("Error de RAR", 
                    f"Código de salida: {resultado.returncode}\n\n{resultado.stderr or resultado.stdout}")
        except FileNotFoundError:
            messagebox.showerror("Aweonao", "Te dije que instalarai la wea de 'rar' primero.\nRevisa tu distro, capaz te toque meter esta wea en el terminal:\nsudo apt install rar -y")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style()
    style.theme_use("clam")
    app = RarCompressorApp(root)
    root.mainloop()