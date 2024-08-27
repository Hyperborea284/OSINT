import tkinter as tk
from tkinter import ttk
from main import Main
import threading
import schedule
import time

class MainGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Interface Gráfica para Main")
        self.geometry("400x200")

        self.main_instance = Main()
        self.agendamento_ativo = False

        self.create_widgets()

    def create_widgets(self):
        ttk.Button(self, text="Ativar Agendamento", command=self.ativar_agendamento).pack(pady=10)
        ttk.Button(self, text="Desativar Agendamento", command=self.desativar_agendamento).pack(pady=10)
        ttk.Button(self, text="Configurar Agendamento", command=self.configurar_agendamento).pack(pady=10)

    def ativar_agendamento(self):
        if not self.agendamento_ativo:
            self.agendamento_ativo = True
            threading.Thread(target=self.main_instance.agendar_tarefas).start()

    def desativar_agendamento(self):
        self.agendamento_ativo = False

    def configurar_agendamento(self):
        # Adicione aqui a lógica para configurar o agendamento, se necessário
        pass

if __name__ == "__main__":
    gui = MainGUI()
    gui.mainloop()
