import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import numpy as np

class TableauSaisieLibre(tk.Tk):
    """
    Tableau de saisie type Excel avec ajout dynamique
    de lignes et de colonnes.
    """

    def __init__(self):
        super().__init__()
        self.title("Tableau de saisie libre des mesures")
        self.geometry("800x500")

        self.tableau = []
        self.nb_lignes = 0
        self.nb_colonnes = 0

        self._creer_interface()
        self.ajouter_ligne()
        self.ajouter_colonne()

    def _creer_interface(self):
        frame_btn = ttk.Frame(self)
        frame_btn.pack(fill="x", padx=10, pady=5)

        ttk.Button(frame_btn, text="➕ Ajouter une ligne", command=self.ajouter_ligne).pack(side="left", padx=5)
        ttk.Button(frame_btn, text="➕ Ajouter une colonne", command=self.ajouter_colonne).pack(side="left", padx=5)
        ttk.Button(frame_btn, text="Valider les données", command=self.valider).pack(side="right", padx=5)

        self.frame_tableau = ttk.Frame(self)
        self.frame_tableau.pack(fill="both", expand=True, padx=10, pady=5)

    def ajouter_ligne(self):
        ligne = []

        for j in range(self.nb_colonnes):
            e = ttk.Entry(self.frame_tableau, width=12)
            e.grid(row=self.nb_lignes, column=j, padx=2, pady=2)
            ligne.append(e)

        self.tableau.append(ligne)
        self.nb_lignes += 1

    def ajouter_colonne(self):
        for i in range(self.nb_lignes):
            e = ttk.Entry(self.frame_tableau, width=12)
            e.grid(row=i, column=self.nb_colonnes, padx=2, pady=2)
            self.tableau[i].append(e)

        self.nb_colonnes += 1

    def valider(self):
        donnees = []

        try:
            for ligne in self.tableau:
                ligne_valeurs = []
                for cell in ligne:
                    val = cell.get().strip()
                    ligne_valeurs.append(float(val) if val else np.nan)
                donnees.append(ligne_valeurs)

        except ValueError:
            messagebox.showerror(
                "Erreur de saisie",
                "Toutes les valeurs doivent être numériques."
            )
            return

        array = np.array(donnees)
        dataframe = pd.DataFrame(array)

        messagebox.showinfo(
            "Succès",
            f"Données enregistrées\nDimensions : {array.shape}"
        )

        # Sortie exploitable pour analyses
        print("NumPy array :\n", array)
        print("DataFrame pandas :\n", dataframe)

if __name__ == "__main__":
    app = TableauSaisieLibre()
    app.mainloop()