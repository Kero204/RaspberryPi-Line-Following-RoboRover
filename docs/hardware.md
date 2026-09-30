# Hardware

Denne fil dokumenterer hardwareopsætningen og GPIO-forbindelserne for Raspberry Pi Line Follower Robot.

## Komponenter

- Raspberry Pi 3B+
- L298N motor-driver
- 2 × DC-motorer
- 2 × MH-B IR-sensorer
- 2WD robot-chassis
- 2 × 3,6 V batterier
- 5 V powerbank
- Jumper wires og forbindelser

---

## Motorer

### Motor A — venstre motor

Motor A er monteret på robotens venstre side.

Forbindelse:

- L298N `OUT1` → Motor A
- L298N `OUT2` → Motor A

### Motor B — højre motor

Motor B er monteret på robotens højre side.

Forbindelse:

- L298N `OUT3` → Motor B
- L298N `OUT4` → Motor B

---

## Raspberry Pi → L298N

GPIO-numrene nedenfor bruger BCM-nummerering.

| Funktion | Raspberry Pi GPIO | Fysisk pin | L298N |
|---|---:|---:|---|
| Motor A retning 1 | GPIO17 | 11 | IN1 |
| Motor A retning 2 | GPIO27 | 13 | IN2 |
| Motor B retning 1 | GPIO22 | 15 | IN3 |
| Motor B retning 2 | GPIO23 | 16 | IN4 |
| Motor A hastighed | GPIO18 | 12 | ENA |
| Motor B hastighed | GPIO12 | 32 | ENB |

ENA- og ENB-jumperne fjernes, fordi hastigheden styres fra Raspberry Pi med PWM.

---

## IR-sensorer

Der anvendes to MH-B IR-sensorer monteret foran på robotten.

### Venstre MH-B

- VCC → Raspberry Pi 3,3 V
- GND → Raspberry Pi GND
- OUT → GPIO5 / fysisk pin 29

### Højre MH-B

- VCC → Raspberry Pi 3,3 V
- GND → Raspberry Pi GND
- OUT → GPIO6 / fysisk pin 31

Begge sensorer deler 3,3 V-forsyning og GND, men har hver deres GPIO-signal.

Sensorernes HIGH/LOW-logik kontrolleres med `src/test_sensors.py`, før den endelige line-following-logik testes.

---

## Strømforsyning

### Raspberry Pi

Raspberry Pi 3B+ forsynes separat:

Powerbank → USB → Micro-USB → Raspberry Pi 3B+

Powerbanken skal levere stabil 5 V.

### Motorer

De to 3,6 V batterier forbindes i serie og giver cirka:

7,2 V nominelt.

Batteripakken forbindes til:

- Batteri `+` → L298N `12V/Vs`
- Batteri `-` → L298N `GND`

Motorerne får dermed strøm gennem L298N.

### Fælles ground

Raspberry Pi og L298N skal dele samme ground:

Raspberry Pi GND → L298N GND

Dette giver GPIO-signalerne og L298N samme 0 V-reference.

### L298N logic power

L298N's `5V-EN` jumper fjernes.

- Raspberry Pi 5 V → L298N 5 V
- Raspberry Pi GND → L298N GND

Motorforsyningen og Raspberry Pi-forsyningen forbliver ellers separate.
