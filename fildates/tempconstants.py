from dataclasses import dataclass, field


@dataclass
class BasisOpl:
    pathroot: str = r"C:\Filkassen"


@dataclass
class NatureMan(BasisOpl):
    pathbase: str = r"LIFE-NatureMan Financial Reporting"
    pathspec: str = r"Fase 3 2022og2023\1. Financial Report"
    distspec: dict = field(default_factory=lambda: {
        "Jam": "1. Jammerbugt Kommune",
        "Mar": "2. Mariagerfjord Kommune",
        "Ran": "3. Randers Kommune",
        "Reb": "4. Rebild Kommune",
        "Ski": "5. Skive Kommune",
        "Vhi": "6. VestHimmerland Kommune",
        "Vib": "7. Viborg Kommune",
        "Aal": "8. Aalborg Kommune",
        "NST": "91. Naturstyrelsen",
        "LBST": "92. Landbrugsstyrelsen",
        "MST": "93. Miljostyrelsen",
    })


@dataclass
class Openwood(BasisOpl):
    pathbase: str = r"LIFE-OpenWoods  Financial Reporting"
    pathspec: str = r"1. Financial Report"
    distspec: dict = field(default_factory=lambda: {
        "AMPHI": "1. Amphi",
        "AVJF": "2. AageVJensen",
        "DEP": "3. MST",
        "FLC": "4. SkovSkolen",
        "SN": "5. StiftungNatur",
        "DNA": "6. NST",
    })



@dataclass
class ForFit(BasisOpl):
    pathbase: str = r"LIFE-ForFit Financial Reporting"
    pathspec: str = r"1. Financial Report"
    distspec: dict = field(default_factory=lambda: {
        "DSK": "1. Dansk Skovforening",
        "EPA": "2. Miljøstyrelsen",
        "HD": "3. HedeSelskabet\\1. HD",
        "HJØ": "3. HedeSelskabet\\2. StoreHjollund",
        "HØL": "3. HedeSelskabet\\3. HollundSogaard",
        "GRI": "3. HedeSelskabet\\4. GrindstedPlantage",
        "BRØ": "3. HedeSelskabet\\5. BronsSkov",
        "FÆR": "3. HedeSelskabet\\6. FaerchsPlantage",
        "SON": "3. HedeSelskabet\\7. SondrupPlantage",
        "CLA": "3. HedeSelskabet\\9. Clasonborg",
        "IGN": "4. Københavns Universitet",
        "SLS": "5. Salten Langsø",
        "SHLF": "6. Landesforsten Schleswig-Holstein",
        "SKD": "7. Skovdyrkerne",
        "LOV": "8. Løvenholm - NST",
        "SOR": "9. Sorø - NST",
        "STI": "10. Stilde - NST",
        "NST": "20. Naturstyrelsen",
    })