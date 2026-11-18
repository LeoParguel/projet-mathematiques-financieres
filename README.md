# Projet : Mathématiques Financières

Projet réalisé par **Marvin Verrelli** et **Léo Parguel** dans le cadre du Master 1 MBFA (janvier 2025).

Ce programme Python met en œuvre plusieurs concepts de mathématiques financières : valorisation d'obligations, modèles d'évaluation d'actions, alpha de Jensen, optimisation de portefeuille et simulation de Monte Carlo.

📄 **Rapport complet :** [Projet_Mathematiques_Financieres.pdf](Projet_Mathematiques_Financieres.pdf)

## Contenu

| Partie | Ce qui est calculé |
|---|---|
| Obligations | Valeur actuelle, montant futur et duration modifiée (comparaison Grèce / France) |
| Actions | Prix théorique (modèle de Gordon-Shapiro) et rendement attendu (CAPM) pour Apple, Microsoft, Visa et Tesla |
| Performance | Alpha de Jensen de chaque action |
| Portefeuille | Données de marché via Yahoo Finance (2020-2023), minimisation de la volatilité (SLSQP) |
| Simulation | 10 000 simulations de Monte Carlo des rendements du portefeuille |

## Résultats principaux

| Pays | Valeur actuelle | Montant futur | Duration modifiée |
|---|---|---|---|
| Grèce (6 %) | 4 632,00 € | 8 295,20 € | 7,57 |
| France (2 %) | 6 347,39 € | 7 737,43 € | 8,19 |

| Action | Alpha de Jensen |
|---|---|
| Apple | -0,0760 |
| Microsoft | -0,0587 |
| Visa | -0,0135 |
| Tesla | 0,0000 |

## Lancer le projet

```bash
pip install -r requirements.txt
python projet_mathematiques_financieres.py
```

La dernière partie télécharge des données depuis Yahoo Finance : une connexion internet est nécessaire.

## Outils

Python · NumPy · Pandas · Matplotlib · SciPy · yfinance
