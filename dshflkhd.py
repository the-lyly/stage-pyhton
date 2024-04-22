import plotly.figure_factory as ff
import datetime

#Définition des tâches avec leurs dates de début et de fin
tasks = [
    dict(Task="Préparation", Start='2023-02-27', Finish='2023-03-03', Resource='Planification'),
    dict(Task="Conception Topologie", Start='2023-03-06', Finish='2023-03-10', Resource='Développement'),
    dict(Task="Configuration Routeurs/Serveurs", Start='2023-03-13', Finish='2023-03-17', Resource='Configuration'),
    dict(Task="Configuration Clients VPN", Start='2023-03-20', Finish='2023-03-24', Resource='Configuration'),
    dict(Task="Optimisation et Tests", Start='2023-03-27', Finish='2023-03-31', Resource='Test'),
    dict(Task="Documentation", Start='2023-04-03', Finish='2023-04-07', Resource='Documentation'),
    dict(Task="Présentation Projet", Start='2023-04-10', Finish='2023-04-14', Resource='Présentation'),
    dict(Task="Clôture Stage", Start='2023-04-17', Finish='2023-04-18', Resource='Clôture')
]

#Création du diagramme de Gantt
fig = ff.create_gantt(tasks, index_col='Resource', show_colorbar=True, group_tasks=True)

#Affichage du graphique
fig.show()
