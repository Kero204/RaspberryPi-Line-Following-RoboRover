# Raspberry Pi Line Follower Robot

Projekt til faget **Udvidede indlejrede systemer**.

## Formål

Formålet med projektet er at bygge og programmere en autonom line-following robot baseret på en Raspberry Pi 3.

Robotten skal kunne følge en bane markeret med sort tape ved hjælp af to IR-sensorer. Sensorerne registrerer robotens placering i forhold til banen, hvorefter Raspberry Pi'en behandler signalerne og styrer de to DC-motorer gennem en L298N motor-driver.

Robotten skal kunne korrigere sin kørselsretning automatisk, så den bliver på banen under hele kørslen.

Projektet omfatter derfor både:

- Hardwareopbygning og forbindelse af komponenter
- GPIO-forbindelser mellem Raspberry Pi, sensorer og motor-driver
- Motorstyring
- Registrering af banen med IR-sensorer
- Python-programmering
- Test og fejlfinding
- Justering og optimering af robotens kørsel

## Konkurrence

Når robotten er færdig, skal den deltage i en konkurrence, hvor den skal gennemføre **3 omgange på banen på kortest mulige tid**.

Robotten skal blive på banen under hele kørslen. Testkørsler og omgangstider bruges under udviklingen til at forbedre robotens styring og hastighed.

## Hardware

Projektet anvender følgende hovedkomponenter:

- Raspberry Pi 3b+
- L298N motor-driver
- 2 × DC-motorer
- 2 × IR-sensorer
  - MH-B
  - HW-201
- 2WD robot-chassis
- 2 × 3,6 V batterier til motorforsyning
- Powerbank til Raspberry Pi
- Jumper wires og øvrige forbindelser
- Breadboard rail

Raspberry Pi'en fungerer som robotens controller og kører Python-programmet.

IR-sensorerne bruges som input til at registrere den sorte bane, mens L298N fungerer som mellemled mellem Raspberry Pi'en og de to DC-motorer.

## Software

Robotten programmeres i **Python**.

Python-koden kører direkte på Raspberry Pi'en og bruger GPIO-forbindelserne til at:

1. Læse signalerne fra IR-sensorerne
2. Bestemme robotens position i forhold til banen
3. Styre motorernes retning og hastighed gennem L298N
4. Korrigere robotens bevægelse under kørslen

Projektets Python-afhængigheder dokumenteres i `requirements.txt`, så Python-miljøet kan genskabes efter eksempelvis en geninstallation af Raspberry Pi'en.

## Projektstruktur

```text
robot-project/
├── README.md
├── requirements.txt
├── .gitignore
│
├── src/
│   └── Python-kode til robotten
│
├── docs/
│   └── Hardware- og GPIO-dokumentation
│
└── setup/
    └── Scripts til opsætning af Raspberry Pi
```

### `src/`

Indeholder selve Python-koden, der styrer robotten, motorerne og IR-sensorerne.

### `docs/`

Indeholder dokumentation for projektets hardwareopsætning, herunder GPIO-forbindelser, motor-driver, motorer, sensorer og strømforsyning.

### `setup/`

Indeholder scripts, der bruges til at gøre en Raspberry Pi klar til projektet eller hjælpe med at genskabe softwareopsætningen efter en geninstallation.

### `requirements.txt`

Indeholder de Python-pakker og dependencies, som robotkoden kræver.

### `.gitignore`

Angiver lokale filer og mapper, som Git ikke skal tracke eller pushe til GitHub, eksempelvis projektets virtuelle Python-miljø `.venv/`.

## Udviklingsmiljø

Projektet udvikles på Raspberry Pi'en via **VS Code Remote SSH**.

VS Code kører på udviklerens computer, mens projektfilerne, Python-miljøet og selve programkørslen ligger på Raspberry Pi'en.

Projektet anvender desuden et virtuelt Python-miljø (`.venv`), så projektets Python-pakker holdes adskilt fra Raspberry Pi'ens globale Python-installation.

## Versionsstyring

Projektet versionsstyres med **Git** og opbevares på **GitHub**.

Det gør det muligt at:

- Gemme projektets udviklingshistorik
- Dele ændringer mellem gruppemedlemmer
- Gendanne projektfiler efter en geninstallation
- Dokumentere ændringer gennem commits
- Arbejde videre på projektet uden at være afhængig af én bestemt installation af Raspberry Pi'en

## Kørsel

Python-koden placeres i:

```text
src/
```

Den konkrete kommando til at starte robotprogrammet dokumenteres her, når den endelige Python-kode og filstruktur er fastlagt.
