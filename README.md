# DBC
Repository file DBC RaceUP.

## Istruzioni per l'uso
La repo contiene i file .dbc che descrivono sia CAN1 (inverter) che CAN2 (vettura), e la libreria dbcc [(link)]('https://github.com/howerj/dbcc') per la generazione delle librerie/file.

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
