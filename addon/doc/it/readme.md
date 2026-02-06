# GemVDA - Google Gemini AI per NVDA

## Panoramica

GemVDA integra le capacita di Google Gemini AI direttamente in NVDA, fornendo agli utenti ciechi e ipovedenti un'assistenza AI potente. L'addon supporta diversi modelli Gemini tra cui Gemini 3, Gemini 2.5 Pro e le varianti Flash per chat, descrizione di immagini, analisi video e altro.

## Funzionalita

* **Chat AI**: Conversazioni con Gemini AI direttamente da NVDA
* **Descrizione schermo**: Cattura e descrivi l'intero schermo
* **Descrizione oggetto**: Descrivi l'oggetto corrente del navigatore
* **Analisi video**: Registra video dello schermo e fallo analizzare da Gemini
* **Allega immagini**: Allega immagini da file per la descrizione AI
* **Cronologia conversazione**: Mantieni il contesto attraverso piu messaggi
* **Modelli multipli**: Scegli tra vari modelli Gemini in base alle tue esigenze
* **Riassumi selezione**: Seleziona il testo e Gemini riassumera i punti chiave
* **Impostazioni personalizzabili**: Configura temperatura, token, streaming e altro

## Requisiti

* NVDA 2023.1 o successivo
* Chiave API Google Gemini (livello gratuito disponibile)
* Connessione Internet

## Configurazione

### Ottenere una chiave API

1. Visita [Google AI Studio](https://aistudio.google.com/apikey)
2. Accedi con il tuo account Google
3. Crea una nuova chiave API
4. Copia la chiave per usarla nell'addon

### Configurare la chiave API

1. Premi NVDA+N per aprire il menu NVDA
2. Vai su Preferenze > Impostazioni
3. Seleziona la categoria "Gemini AI"
4. Clicca su "Configura chiave API..."
5. Incolla la tua chiave API e premi OK

## Scorciatoie da tastiera

| Scorciatoia | Azione |
|-------------|--------|
| NVDA+G | Apri finestra di dialogo Gemini AI |
| NVDA+Shift+E | Descrivi l'intero schermo |
| NVDA+Shift+O | Descrivi l'oggetto del navigatore |
| NVDA+V | Avvia/ferma registrazione video per analisi |
| NVDA+Shift+U | Riassumi il testo selezionato |

## Usare la finestra di dialogo Gemini

Quando apri la finestra di dialogo Gemini con NVDA+G:

1. **Modello**: Seleziona quale modello Gemini usare
2. **Prompt di sistema**: Istruzioni opzionali su come Gemini deve rispondere
3. **Cronologia**: Visualizza la cronologia della conversazione
4. **Messaggio**: Scrivi il tuo messaggio o domanda
5. **Invia**: Invia il tuo messaggio a Gemini
6. **Allega immagine**: Aggiungi un file immagine per l'analisi di Gemini
7. **Pulisci**: Pulisci la cronologia della conversazione
8. **Copia risposta**: Copia l'ultima risposta negli appunti

### Suggerimenti per la finestra di dialogo

* Premi ctrl+invio nel campo messaggio per inviare rapidamente
* Usa Tab per navigare tra i controlli
* La cronologia si aggiorna automaticamente mentre chatti
* Le immagini allegate vengono inviate con il tuo prossimo messaggio

## Impostazioni

Accedi alle impostazioni tramite menu NVDA > Preferenze > Impostazioni > Gemini AI:

* **Modello predefinito**: Scegli il tuo modello Gemini preferito
* **Temperatura (0-200)**: Controlla la creativita delle risposte (0=concentrato, 200=creativo)
* **Token di output massimi**: Lunghezza massima delle risposte
* **Risposte in streaming**: Mostra le risposte mentre arrivano
* **Modalita conversazione**: Includi cronologia chat per contesto
* **Ricorda prompt di sistema**: Salva il tuo prompt personalizzato
* **Blocca tasto Escape**: Previeni chiusura accidentale della finestra
* **Filtra markdown**: Rimuovi formattazione markdown dalle risposte

### Feedback sonoro

* **Riproduci suono all'invio richiesta**: Conferma audio quando il messaggio viene inviato
* **Riproduci suono durante l'attesa**: Suono di progresso durante l'elaborazione AI
* **Riproduci suono alla ricezione risposta**: Notifica all'arrivo della risposta

## Modelli disponibili

* **Gemini 3 Pro (Preview)**: Modello piu capace con capacita di ragionamento
* **Gemini 3 Flash (Preview)**: Modello veloce con capacita di ragionamento
* **Gemini 2.5 Pro**: Modello potente pronto per la produzione
* **Gemini 2.5 Flash**: Veloce ed efficiente per la maggior parte dei compiti
* **Gemini 2.5 Flash-Lite**: Leggero e risposte piu veloci
* **Gemini 2.5 Flash Image**: Ottimizzato per compiti relativi alle immagini

## Funzionalita immagini e video

### Descrizione schermo (NVDA+Shift+E)

Cattura l'intero schermo e lo invia a Gemini per una descrizione dettagliata. Utile per:

* Capire interfacce sconosciute
* Ottenere una panoramica del contenuto visivo
* Identificare elementi che NVDA non puo descrivere

### Descrizione oggetto (NVDA+Shift+O)

Cattura solo l'oggetto corrente del navigatore. Utile per:

* Descrivere elementi specifici dell'interfaccia
* Capire immagini o icone
* Ottenere dettagli sui controlli focalizzati

### Analisi video (NVDA+V)

1. Premi NVDA+V per avviare la registrazione
2. Esegui le azioni che vuoi analizzare
3. Premi di nuovo NVDA+V per fermare
4. Attendi che Gemini analizzi il video

Utile per:

* Capire flussi di lavoro visivi
* Ottenere descrizioni passo per passo
* Analizzare contenuti dinamici

### Riassumi selezione (NVDA+Shift+U)

Seleziona il testo in qualsiasi applicazione e Gemini riassumera i punti chiave. Funziona in modalita navigazione (browser web, lettori PDF) e nei campi di testo normali. Il prompt di riassunto puo essere personalizzato nelle impostazioni dell'addon.

## Risoluzione problemi

### "Libreria Google GenAI non installata"

Esegui l'installatore delle dipendenze:
1. Naviga a %APPDATA%\nvda\addons\GemVDA
2. Esegui install_deps.bat o install_deps.py
3. Riavvia NVDA

### "Nessuna chiave API configurata"

Configura la tua chiave API in Impostazioni > Gemini AI > Configura chiave API

### Le risposte sono troppo corte o tagliate

Aumenta l'impostazione "Token di output massimi"

### Le risposte sono troppo casuali

Riduci l'impostazione Temperatura (prova 50-100)

## Nota sulla privacy

* I tuoi messaggi e immagini vengono inviati all'API Gemini di Google
* Le chiavi API sono memorizzate localmente nella tua configurazione NVDA
* Nessun dato viene condiviso con lo sviluppatore dell'addon
* Consulta la politica sulla privacy AI di Google per dettagli

## Supporto

* Segnala problemi: [GitHub Issues](https://github.com/ogomez92/GemVDA/issues)
* Codice sorgente: [GitHub Repository](https://github.com/ogomez92/GemVDA)

## Licenza

Questo addon e rilasciato sotto la Licenza Pubblica Generale GNU v2.

## Autore

Oriol Gomez Sentis
