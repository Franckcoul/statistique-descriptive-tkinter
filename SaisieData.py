import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import pandas as pd

class FenetreSaisieMesures(tk.Toplevel):
    """
    Fenêtre Tkinter permettant la saisie de mesures
    sous forme de ligne, colonne ou matrice.
    """

    def __init__(self, parent):
        super().__init__(parent)
        self.title("Saisie des mesures numériques")
        self.geometry("800x500")

        self.entries = []
        self._creer_interface()

    def _creer_interface(self):
        # Choix du type de données
        frame_type = ttk.LabelFrame(self, text="Type de données")
        frame_type.pack(fill="x", padx=10, pady=5)

        self.type_var = tk.StringVar(value="ligne")

        ttk.Radiobutton(frame_type, text="Ligne", variable=self.type_var, value="ligne").pack(side="left", padx=5)
        ttk.Radiobutton(frame_type, text="Colonne", variable=self.type_var, value="colonne").pack(side="left", padx=5)
        ttk.Radiobutton(frame_type, text="Matrice", variable=self.type_var, value="matrice").pack(side="left", padx=5)

        # Dimensions
        frame_dim = ttk.LabelFrame(self, text="Dimensions")
        frame_dim.pack(fill="x", padx=10, pady=5)

        ttk.Label(frame_dim, text="Lignes :").pack(side="left")
        self.ent_lignes = ttk.Entry(frame_dim, width=5)
        self.ent_lignes.pack(side="left", padx=5)

        ttk.Label(frame_dim, text="Colonnes :").pack(side="left")
        self.ent_colonnes = ttk.Entry(frame_dim, width=5)
        self.ent_colonnes.pack(side="left", padx=5)

        ttk.Button(frame_dim, text="Générer la grille", command=self.generer_grille).pack(side="left", padx=10)

        # Zone grille
        self.frame_grille = ttk.LabelFrame(self, text="Saisie des valeurs")
        self.frame_grille.pack(fill="both", expand=True, padx=10, pady=5)

        # Boutons actions
        frame_action = ttk.Frame(self)
        frame_action.pack(fill="x", padx=10, pady=5)

        ttk.Button(frame_action, text="Valider les données", command=self.valider).pack(side="left", padx=5)
        ttk.Button(frame_action, text="Fermer", command=self.destroy).pack(side="right", padx=5)

    def generer_grille(self):
        for widget in self.frame_grille.winfo_children():
            widget.destroy()

        self.entries.clear()

        try:
            lignes = int(self.ent_lignes.get())
            colonnes = int(self.ent_colonnes.get())
        except ValueError:
            messagebox.showerror("Erreur", "Dimensions invalides.")
            return

        if self.type_var.get() == "ligne":
            lignes, colonnes = 1, colonnes
        elif self.type_var.get() == "colonne":
            lignes, colonnes = lignes, 1

        for i in range(lignes):
            ligne_entries = []
            for j in range(colonnes):
                e = ttk.Entry(self.frame_grille, width=10)
                e.grid(row=i, column=j, padx=3, pady=3)
                ligne_entries.append(e)
            self.entries.append(ligne_entries)

    def valider(self):
        try:
            data = [
                [float(e.get()) for e in row]
                for row in self.entries
            ]
        except ValueError:
            messagebox.showerror("Erreur", "Toutes les valeurs doivent être numériques.")
            return

        self.array = np.array(data)
        self.dataframe = pd.DataFrame(self.array)

        messagebox.showinfo(
            "Succès",
            "Données enregistrées avec succès.\n"
            f"Dimensions : {self.array.shape}"
        )

        # Exemple d'affichage console
        print("NumPy array :\n", self.array)
        print("DataFrame pandas :\n", self.dataframe)

class ApplicationPrincipale(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Application scientifique")
        self.geometry("400x200")

        ttk.Button(
            self,
            text="Saisir des mesures",
            command=self.ouvrir_fenetre_saisie
        ).pack(pady=50)

    def ouvrir_fenetre_saisie(self):
        FenetreSaisieMesures(self)

if __name__ == "__main__":
    app = ApplicationPrincipale()
    app.mainloop()
