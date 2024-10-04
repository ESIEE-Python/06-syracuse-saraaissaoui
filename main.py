"""
Ce module contient des fonctions pour générer et analyser la suite de Syracuse,
ainsi que des visualisations de la suite.
"""

# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """
    Affiche un graphique de la suite de Syracuse.

    Args:
        lsyr (list): La liste des valeurs de la suite de Syracuse.
    """
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({
        'layout': {
            'title': {'text': title},
            'xaxis': {'title': {'text': "x"}},
            'yaxis': {'title': {'text': "y"}},
        }
    })

    x = list(range(len(lsyr)))  # Correction ici pour l'utilisation correcte de list
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color="blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')

#######################

def syracuse_l(n):
    """
    Renvoie la liste des valeurs de la suite de Syracuse.

    Args:
        n (int): La valeur initiale de la suite.

    Returns:
        list: La liste des valeurs de la suite de Syracuse jusqu'à 1.
    """
    suite = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        suite.append(n)
    return suite

def temps_de_vol(suite):
    """
    Renvoie le temps de vol d'une suite de Syracuse.

    Args:
        suite (list): La liste des valeurs de la suite de Syracuse.

    Returns:
        int: Le temps de vol (longueur de la suite - 1).
    """
    return len(suite) - 1

def temps_de_vol_en_altitude(suite):
    """
    Renvoie la somme des valeurs en altitude (supérieures à 1) dans la suite.

    Args:
        suite (list): La liste des valeurs de la suite de Syracuse.

    Returns:
        int: La somme des valeurs supérieures à 1 dans la suite.
    """
    n = 0
    for x in suite:
        if x > 1:
            n += x
    return n


def altitude_maximale(suite):
    """
    Renvoie l'altitude maximale atteinte dans la suite de Syracuse.

    Args:
        suite (list): La liste des valeurs de la suite de Syracuse.

    Returns:
        int: La valeur maximale dans la suite.
    """
    return max(suite)

def main():
    """
    Fonction principale pour exécuter les appels aux fonctions secondaires.
    """
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))

if __name__ == "__main__":
    main()
