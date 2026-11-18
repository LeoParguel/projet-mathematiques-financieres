import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd
from scipy import stats
import scipy.optimize as sco

def calcul_valeur_obligation(coupons_obligation, prix_nominal, annees_obligation, taux_interet):
    flux_actualises = np.array([coupons_obligation] * (annees_obligation - 1) + [coupons_obligation + prix_nominal])
    return np.sum(flux_actualises / (1 + taux_interet) ** np.arange(1, annees_obligation + 1))

def calcul_duration(prix_obligation, coupons_obligation, annees_obligation, taux_interet):
    flux_de_tresorerie = np.array([coupons_obligation] * (annees_obligation - 1) + [coupons_obligation + prix_obligation])
    flux_actualises = flux_de_tresorerie / (1 + taux_interet) ** np.arange(1, annees_obligation + 1)
    duration = np.sum(flux_actualises * np.arange(1, annees_obligation + 1)) / np.sum(flux_actualises)
    return duration / (1 + taux_interet)

def montant_futur(coupons_obligation, prix_nominal, annees_obligation, taux_interet):
    flux_futurs = np.array([coupons_obligation] * (annees_obligation - 1) + [coupons_obligation + prix_nominal])
    return np.sum(flux_futurs * (1 + taux_interet) ** (annees_obligation - np.arange(1, annees_obligation + 1)))

prix_nominal = 5000
coupons_obligation = 250
annees_obligation = 10
taux_interets_grecque = 0.06
taux_interets_Francais = 0.02
pays_obligations = ["Grèce", "France"]

valeur_obligation_grecque = calcul_valeur_obligation(coupons_obligation, prix_nominal, annees_obligation, taux_interets_grecque)
montant_futur_grecque = montant_futur(coupons_obligation, prix_nominal, annees_obligation, taux_interets_grecque)
duration_grecque = calcul_duration(prix_nominal, coupons_obligation, annees_obligation, taux_interets_grecque)

valeur_obligation_francaise = calcul_valeur_obligation(coupons_obligation, prix_nominal, annees_obligation, taux_interets_Francais)
montant_futur_francaise = montant_futur(coupons_obligation, prix_nominal, annees_obligation, taux_interets_Francais)
duration_francaise = calcul_duration(prix_nominal, coupons_obligation, annees_obligation, taux_interets_Francais)

print(f"{'Pays':<15}{'Valeur Obligation (€)':<25}{'Montant Futur (€)':<25}{'Duration Modifiée':<20}")
print(f"{'Grèce':<15}{valeur_obligation_grecque:<25.2f}{montant_futur_grecque:<25.2f}{duration_grecque:<20.2f}")
print(f"{'France':<15}{valeur_obligation_francaise:<25.2f}{montant_futur_francaise:<25.2f}{duration_francaise:<20.2f}")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
ax1.bar(pays_obligations, [valeur_obligation_grecque, valeur_obligation_francaise], color=['blue', 'orange'], alpha=0.7)
ax1.set_xlabel("Pays")
ax1.set_ylabel("Valeur Obligation (€)")
ax1.set_title("Valeur des Obligations")
ax2.bar(pays_obligations, [montant_futur_grecque, montant_futur_francaise], color=['green', 'red'], alpha=0.7)
ax2.set_xlabel("Pays")
ax2.set_ylabel("Montant Futur (€)")
ax2.set_title("Montant Futur Total")
plt.tight_layout()
plt.show()

def gordon_shapiro(croissance_dividendes, rendement_exige, dividende_actuel):
    return (dividende_actuel * (1 + croissance_dividendes)) / (rendement_exige - croissance_dividendes)

def capm(taux_risk_free, beta, rendement_marche):
    return taux_risk_free + beta * (rendement_marche - taux_risk_free)

actions = ['Apple', 'Microsoft', 'Visa', 'Tesla']

dividende_apple = 0.88
beta_apple = 1.2
croissance_apple = 0.05
rendement_exige_apple = 0.08
taux_risk_free_apple = 0.07
rendement_marche_apple = 0.2

prix_action_apple = gordon_shapiro(croissance_apple, rendement_exige_apple, dividende_apple)
rendement_attendu_apple = capm(taux_risk_free_apple, beta_apple, rendement_marche_apple)

dividende_microsoft = 2.48
beta_microsoft = 0.992
croissance_microsoft = 0.06
rendement_exige_microsoft = 0.12
taux_risk_free_microsoft = 0.05
rendement_marche_microsoft = 0.18

prix_action_microsoft = gordon_shapiro(croissance_microsoft, rendement_exige_microsoft, dividende_microsoft)
rendement_attendu_microsoft = capm(taux_risk_free_microsoft, beta_microsoft, rendement_marche_microsoft)

dividende_visa = 1.66
beta_visa = 0.95
croissance_visa = 0.07
rendement_exige_visa = 0.095
taux_risk_free_visa = 0.34
rendement_marche_visa = 0.14

prix_action_visa = gordon_shapiro(croissance_visa, rendement_exige_visa, dividende_visa)
rendement_attendu_visa = capm(taux_risk_free_visa, beta_visa, rendement_marche_visa)

dividende_tesla = 5
beta_tesla = 2.0
croissance_tesla = 0.10
rendement_exige_tesla = 0.12
taux_risk_free_tesla = 0.02
rendement_marche_tesla = 0.0
def alpha_jensen(rendement_portefeuille, taux_risk_free, beta, rendement_marche):
    alpha = rendement_portefeuille - (taux_risk_free + beta * (rendement_marche - taux_risk_free))
    return alpha

# Données pour chaque action
actions_data = {
    "Apple": {"rendement_portefeuille": 0.15, "beta": 1.2, "taux_risk_free": 0.07, "rendement_marche": 0.2},
    "Microsoft": {"rendement_portefeuille": 0.12, "beta": 0.99, "taux_risk_free": 0.05, "rendement_marche": 0.18},
    "Visa": {"rendement_portefeuille": 0.14, "beta": 0.95, "taux_risk_free": 0.03, "rendement_marche": 0.16},
    "Tesla": {"rendement_portefeuille": 0.18, "beta": 2.0, "taux_risk_free": 0.02, "rendement_marche": 0.1}
}

# Calcul de l'alpha pour chaque action
for action, data in actions_data.items():
    alpha = alpha_jensen(data['rendement_portefeuille'], data['taux_risk_free'], data['beta'], data['rendement_marche'])
    print(f"Alpha de Jensen pour {action} : {alpha:.4f}")

prix_action_tesla = gordon_shapiro(croissance_tesla, rendement_exige_tesla, dividende_tesla)
rendement_attendu_tesla = capm(taux_risk_free_tesla, beta_tesla, rendement_marche_tesla)

prix_actions = [prix_action_apple, prix_action_microsoft, prix_action_visa, prix_action_tesla]
rendements_attendus = [rendement_attendu_apple, rendement_attendu_microsoft, rendement_attendu_visa, rendement_attendu_tesla]

fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.bar(actions, prix_actions, color='skyblue', alpha=0.7)
ax1.set_xlabel("Actions")
ax1.set_ylabel("Prix estimé de l'action (USD)")
ax2 = ax1.twinx()
ax2.plot(actions, rendements_attendus, color="green", marker='o', linewidth=2)
ax2.set_ylabel("Rendement attendu (%)", color="green")
plt.title("Comparaison du Prix Estimé et du Rendement Attendu des Actions")
plt.tight_layout()
plt.show()

actions = ['AAPL', 'MSFT', 'GOOG', 'TSLA', 'V', 'BTC-USD', 'GLD']
data = yf.download(actions, start='2020-01-01', end='2023-01-01')
rendements = data.pct_change().dropna()
rendement_moyen = rendements.mean()
covariance = rendements.cov()

def portefeuille_volatilite(poids, rendement_moyen, covariance):
    return np.sqrt(np.dot(poids.T, np.dot(covariance, poids)))

def optimisation_portefeuille(rendement_moyen, covariance):
    n = len(rendement_moyen)
    contraintes = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    bornes = [(0, 1) for _ in range(n)]
    poids_initiaux = [1. / n] * n
    return sco.minimize(portefeuille_volatilite, poids_initiaux, args=(rendement_moyen, covariance), method='SLSQP', bounds=bornes, constraints=contraintes).x

poids_optimal = optimisation_portefeuille(rendement_moyen, covariance)
np.random.seed(42)
portefeuille_simule = []

for _ in range(10000):
    rendements_simule = np.random.multivariate_normal(rendement_moyen, covariance, size=len(rendements))
    portefeuille_simule.append(np.dot(rendements_simule, poids_optimal).sum())

plt.hist(portefeuille_simule, bins=50, alpha=0.7)
plt.title("Simulation de Monte Carlo des rendements du portefeuille")
plt.xlabel("Rendement cumulé")
plt.ylabel("Fréquence")
plt.show()
