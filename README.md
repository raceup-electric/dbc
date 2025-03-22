# DBC
Repository file DBC RaceUP.

## Istruzioni per l'uso
La repo contiene i file .dbc che descrivono sia CAN1 (inverter) che CAN2 (vettura), e la libreria [dbcc](https://github.com/howerj/dbcc) per la generazione delle librerie/file in C, alternativamente per Rust si può usare [dbc-codegen](https://github.com/technocreatives/dbc-codegen).

1. Compilare dbcc (necessario compilatore C e make)
```
cd dbcc
make
```

2. Eseguire dbcc
  - Libreria C
    ```
    mkdir gen
    dbcc/dbcc -o gen [nomefile.dbc]
    ```
    Troverete l'output nella cartella gen pronto per essere utilizzato.
  - File Excel
    ```
    dbcc/dbcc -C [nomefile.dbc]
    ```
    Utile per avere un'idea generale dei messaggi CAN in vettura.
  - File JSON
    ```
    dbcc/dbcc -j [nomefile.dbc]
    ```

3. Profit

## Modifica dei file
Il formato e' testuale per cui potete modificarlo da un qualsiasi editor di testo ma consiglio l'utilizzo di Kvaser Database Editor 3 per agevolare le operazioni.
Poichè alcuni parser sono abbastanza rigidi si è pregati di seguire l'ordine fornito dallo [standard](https://web.archive.org/web/20191118081543/http://read.pudn.com/downloads766/ebook/3041455/DBC_File_Format_Documentation.pdf)

## Parser per rust

## Generare file di visualizzazione dbc
Usare lo script md_generator.md con
``` bash
python md_generator --in <file dbc> <nome file md>
```
Per ora è da fare in locale e poi pushare il file generato.
Se si modifica il dbc senza aggiornare il markdown, modificale il titolo dbc*.md in dbc*_outdate.md.
