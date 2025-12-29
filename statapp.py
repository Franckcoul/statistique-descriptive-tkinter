import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path

class DataLoader:
    def __init__(self, chemin_fichier, separateur=None):
        self.chemin = Path(chemin_fichier)
        self.separateur = separateur

    def charger(self):
        ext = self.chemin.suffix.lower()

        if ext in [".xlsx", ".xls"]:
            return pd.read_excel(self.chemin)
        elif ext == ".csv":
            return pd.read_csv(self.chemin)
        elif ext in [".txt", ".dat"]:
            if self.separateur is None:
                raise ValueError("Séparateur requis pour fichier texte.")
            return pd.read_csv(self.chemin, sep=self.separateur)
        else:
            raise ValueError("Format non pris en charge.")

class TypeVariable:
    @staticmethod
    def detecter(variable):
        variable = variable.dropna()
        if pd.api.types.is_numeric_dtype(variable):
            return "quantitative_discrete" if variable.nunique() <= 20 else "quantitative_continue"
        return "qualitative"

class AnalyseStatistique:
    def __init__(self, data, variable):
        self.data = data
        self.nom_variable = variable
        self.variable = data[variable].dropna()
        self.type_variable = TypeVariable.detecter(self.variable)

    def analyser(self):
        if self.type_variable.startswith("quantitative"):
            return self._quantitative()
        return self._qualitative()

    def _quantitative(self):
        res = {
            "Type": self.type_variable,
            "Effectif": self.variable.count(),
            "Moyenne": self.variable.mean(),
            "Médiane": self.variable.median(),
            "Mode": self.variable.mode().iloc[0],
            "Écart-type": self.variable.std(),
            "Variance": self.variable.var(),
            "Min": self.variable.min(),
            "Max": self.variable.max()
        }

        if self.variable.count() >= 3:
            _, p = stats.shapiro(self.variable)
            res["Shapiro p-value"] = p
            res["Normalité"] = "Normale" if p > 0.05 else "Non normale"

        return pd.DataFrame.from_dict(res, orient="index", columns=["Valeur"])

    def _qualitative(self):
        eff = self.variable.value_counts()
        freq = self.variable.value_counts(normalize=True) * 100
        df = pd.DataFrame({"Effectif": eff, "Fréquence (%)": freq})
        df.loc["Total"] = [eff.sum(), freq.sum()]
        return df

    def graphique(self):
        if self.type_variable.startswith("quantitative"):
            plt.hist(self.variable, bins=15)
        else:
            self.variable.value_counts().plot(kind="bar")
        plt.title(self.nom_variable)
        plt.show()

class FenetreEditionCode(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Éditeur du code d’analyse")
        self.geometry("800x500")

        self.zone_code = tk.Text(self, wrap="none")
        self.zone_code.pack(fill="both", expand=True)

        code_defaut = """
# Variables disponibles :
# data      -> DataFrame pandas
# variable  -> Série pandas sélectionnée
# plt, np, pd, stats disponibles

# Exemple :
resultats = variable.describe()
print(resultats)

plt.hist(variable, bins=15)
plt.title("Histogramme personnalisé")
plt.show()
"""
        self.zone_code.insert("1.0", code_defaut)

        ttk.Button(
            self,
            text="Exécuter le code",
            command=self.executer_code
        ).pack(pady=5)

        self.data = None
        self.variable = None

    def executer_code(self):
        try:
            exec(self.zone_code.get("1.0", tk.END), {
                "pd": pd,
                "np": np,
                "plt": plt,
                "stats": stats,
                "data": self.data,
                "variable": self.variable
            })
        except Exception as e:
            messagebox.showerror("Erreur d'exécution", str(e))

class ApplicationStatistique(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Analyse statistique descriptive avancée")
        self.geometry("900x650")

        self.data = None
        self.analyse = None

        self._interface()

    def _interface(self):
        frame_top = ttk.LabelFrame(self, text="Données")
        frame_top.pack(fill="x", padx=10, pady=5)

        ttk.Button(frame_top, text="Ouvrir fichier", command=self.ouvrir).pack(side="left")
        self.label = ttk.Label(frame_top, text="Aucun fichier")
        self.label.pack(side="left", padx=10)

        frame_var = ttk.LabelFrame(self, text="Variable")
        frame_var.pack(fill="x", padx=10, pady=5)

        self.combo = ttk.Combobox(frame_var, state="readonly", width=40)
        self.combo.pack(side="left", padx=5)

        ttk.Button(frame_var, text="Analyser", command=self.analyser).pack(side="left", padx=5)
        ttk.Button(frame_var, text="Graphique", command=self.graphique).pack(side="left", padx=5)
        ttk.Button(frame_var, text="Modifier le code", command=self.editeur).pack(side="left", padx=5)

        frame_res = ttk.LabelFrame(self, text="Résultats")
        frame_res.pack(fill="both", expand=True, padx=10, pady=5)

        self.texte = tk.Text(frame_res)
        self.texte.pack(fill="both", expand=True)

    def ouvrir(self):
        chemin = filedialog.askopenfilename()
        if chemin:
            sep = ";" if chemin.endswith((".txt", ".dat")) else None
            self.data = DataLoader(chemin, sep).charger()
            self.label.config(text=Path(chemin).name)
            self.combo["values"] = list(self.data.columns)

    def analyser(self):
        var = self.combo.get()
        if not var:
            return
        self.analyse = AnalyseStatistique(self.data, var)
        res = self.analyse.analyser()
        self.texte.delete("1.0", tk.END)
        self.texte.insert(tk.END, res.to_string())

    def graphique(self):
        if self.analyse:
            self.analyse.graphique()

    def editeur(self):
        if not self.analyse:
            messagebox.showwarning("Attention", "Analyse requise.")
            return
        fen = FenetreEditionCode(self)
        fen.data = self.data
        fen.variable = self.analyse.variable

if __name__ == "__main__":
    app = ApplicationStatistique()
    app.mainloop()
