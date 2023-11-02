from dataclasses import dataclass, field


@dataclass
class BasisOpl:
    pathroot: str = r'C:\Billeder'


@dataclass
class NatureMan(BasisOpl):
    pathspec: str = 'Billeder2021'
    distspec: dict = field(default_factory=lambda: {
        "A": "20210318HestehaveSkov",
        "B": "20210326MolsBjerge",
        "C": "20210331RingelmoseSkov",
        "D": "20210410RugaardNordstrand",
        "E": "20210413Rugaard",
        "F": "20210419MolsBjerge",
        "G": "20210420MolsBjerge",
        "H": "20210424RingelmoseSkov",
    })


@dataclass
class Openwood(BasisOpl):
    pathspec: str = 'Billeder2021'
    distspec: dict = field(default_factory=lambda: {
        "I": "20210518Krakaer",
        "J": "20210522RingelmoseSkov",
        "K": "20210527MolsBjerge",
        "L": "20210528RugaardNordstrand",
        "M": "20210530ElsegaardeSyd",
        "N": "20210531StaksrodeSkov",
        "O": "20210604Havagervej",
        "P": "20210604MaardalsHus",
        "Q": "20210605LilleVildmose",
    })



@dataclass
class ForFit(BasisOpl):
    pathspec: str = 'Billeder2021'
    distspec: dict = field(default_factory=lambda: {
        "R": "20210605MaardalsHus",
        "S": "20210609GlatvedStrand",
        "T": "20210609RugaardNordstrand",
        "U": "20210627TvedKaer",
        "V": "20210630TornbyKlitpltg",
        "X": "20210707RugaardNordstrand",
        "Y": "20210711BredFjed",
        "Z": "20210711SoeholtStorskov",
        "AA": "20210712Hyllekrog",
        "AB": "20210712SoeholtStorskov",
        "AC": "20210713Hovblege",
        "AD": "20210713MoensKlint",
        "AE": "20210714Krenkerup",
        "AF": "20210715Bjergemark",
        "AG": "20210715Skovtaarnet",
        "AH": "20210716Dodekalitten",
        "AI": "20210716TaarsHavn",
        "AJ": "20210723MolsBjerge",
        "AK": "20210919MolsBjerge",
        "AL": "2021Uge42Sivota",
    })