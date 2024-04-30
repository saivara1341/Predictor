import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

class GraphPlotter(tk.Toplevel):
    def __init__(self, master, data):
        super().__init__(master)
        self.title("Graph Plotter")
        self.geometry("800x600")

        self.data = data
        self.selected_attributes = []

        self.create_widgets()

    def create_widgets(self):
        container = tk.Frame(self, bg="#f2f2f2")
        container.pack(fill=tk.BOTH, expand=True)

        title_label = tk.Label(container, text="Predictor", font=("Arial", 24), bg="#f2f2f2", fg="#333")
        title_label.pack(pady=20)

        form_frame = tk.Frame(container, bg="#fff", padx=20, pady=20, bd=2, relief=tk.GROOVE)
        form_frame.pack(pady=20)

        browse_label = tk.Label(form_frame, text="Select File:", font=("Arial", 12), bg="#fff")
        browse_label.grid(row=0, column=0, sticky="w")

        browse_button = tk.Button(form_frame, text="Browse", command=self.browse_file)
        browse_button.grid(row=0, column=1, pady=10, padx=10, sticky="w")

        self.file_label = tk.Label(form_frame, text="", bg="#fff")
        self.file_label.grid(row=1, column=0, columnspan=2, sticky="w")

        plot_label = tk.Label(form_frame, text="Select Plot Type:", font=("Arial", 12), bg="#fff")
        plot_label.grid(row=2, column=0, sticky="w")

        self.plot_type = tk.StringVar(value="Cluster Plot")
        plot_options = ttk.Combobox(form_frame, textvariable=self.plot_type, values=["Cluster Plot", "Bar Plot", "Line Plot", "Scatter Plot"])
        plot_options.grid(row=2, column=1, pady=10, padx=10, sticky="w")

        plot_button = tk.Button(form_frame, text="Plot", command=self.plot_graphs)
        plot_button.grid(row=3, column=0, columnspan=2, pady=20)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", ".csv"), ("Excel files", ".xlsx")])
        if file_path:
            self.load_data(file_path)

    def load_data(self, file_path):
        try:
            if file_path.endswith('.csv'):
                self.data = pd.read_csv(file_path)
            elif file_path.endswith('.xlsx'):
                self.data = pd.read_excel(file_path)
            else:
                raise ValueError("Unsupported file format")

            self.file_label.config(text=file_path)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def plot_graphs(self):
        messagebox.showinfo("Message", "Plotting functionality will be implemented here.")

class CropYieldApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Predictor")
        self.geometry("400x300")

        self.data = None

        self.create_widgets()

    def create_widgets(self):
        container = tk.Frame(self, bg="#f2f2f2")
        container.pack(fill=tk.BOTH, expand=True)

        title_label = tk.Label(container, text="Predictor", font=("Arial", 24), bg="#f2f2f2", fg="#333")
        title_label.pack(pady=20)

        plotter_button = tk.Button(container, text="Open Graph Plotter", command=self.open_graph_plotter)
        plotter_button.pack(pady=20)

    def open_graph_plotter(self):
        if self.data is None:
            messagebox.showerror("Error", "Please select a file first.")
            return

        graph_plotter = GraphPlotter(self, self.data)
        graph_plotter.mainloop()

if __name__ == "__main__":
    app = CropYieldApp()
    app.mainloop()
