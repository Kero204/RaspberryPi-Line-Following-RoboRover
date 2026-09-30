# Permissions og ownership

Denne fil dokumenterer de forventede Linux-rettigheder og ejerskab for projektet.

## Bruger og gruppe

Projektet køres under Linux-brugeren:

`raspberrypik`

Projektfilerne ejes normalt af:

- Owner: `raspberrypik`
- Group: `raspberrypik`

Ejerskab kan kontrolleres med:

`ls -la`

## Mapper

Projektmapper har typisk permissions:

`drwxrwxr-x`

Dette svarer til:

- Owner: read, write, execute
- Group: read, write, execute
- Others: read, execute

På mapper betyder execute (`x`), at brugeren må traversere/gå ind i mappen.

## Almindelige filer

Dokumentations- og konfigurationsfiler har typisk:

`-rw-rw-r--`

Dette betyder:

- Owner: read + write
- Group: read + write
- Others: read

## setup.sh

`setup/setup.sh` skal også være executable.

Forventet eksempel:

`-rwxrwxr-x`

Execute-rettigheden tilføjes med:

`chmod +x setup/setup.sh`

## Kontrol

Projektets filer kan kontrolleres med:

`ls -la`

Setup-scriptet kan kontrolleres specifikt med:

`ls -l setup/setup.sh`
