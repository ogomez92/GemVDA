# GemVDA - Google Gemini AI fuer NVDA

## Uebersicht

GemVDA integriert die Faehigkeiten von Google Gemini AI direkt in NVDA und bietet blinden und sehbehinderten Benutzern leistungsstarke KI-Unterstuetzung. Die Erweiterung unterstuetzt mehrere Gemini-Modelle, darunter Gemini 3, Gemini 2.5 Pro und Flash-Varianten fuer Chat, Bildbeschreibung, Videoanalyse und mehr.

## Funktionen

* **KI-Chat**: Fuehren Sie Gespraeche mit Gemini AI direkt aus NVDA
* **Bildschirmbeschreibung**: Erfassen und beschreiben Sie den gesamten Bildschirm
* **Objektbeschreibung**: Beschreiben Sie das aktuelle Navigatorobjekt
* **Videoanalyse**: Bildschirmvideo aufnehmen und von Gemini analysieren lassen
* **Bilder anhaengen**: Bilddateien zur KI-Beschreibung anhaengen
* **Konversationsverlauf**: Kontext ueber mehrere Nachrichten beibehalten
* **Mehrere Modelle**: Waehlen Sie aus verschiedenen Gemini-Modellen nach Ihren Beduerfnissen
* **Auswahl zusammenfassen**: Text auswaehlen und von Gemini die wichtigsten Punkte zusammenfassen lassen
* **Anpassbare Einstellungen**: Temperatur, Tokens, Streaming und mehr konfigurieren

## Anforderungen

* NVDA 2023.1 oder neuer
* Google Gemini API-Schluessel (kostenlose Stufe verfuegbar)
* Internetverbindung

## Einrichtung

### API-Schluessel erhalten

1. Besuchen Sie [Google AI Studio](https://aistudio.google.com/apikey)
2. Melden Sie sich mit Ihrem Google-Konto an
3. Erstellen Sie einen neuen API-Schluessel
4. Kopieren Sie den Schluessel zur Verwendung in der Erweiterung

### API-Schluessel konfigurieren

1. Druecken Sie NVDA+N, um das NVDA-Menue zu oeffnen
2. Gehen Sie zu Einstellungen > Optionen
3. Waehlen Sie die Kategorie "Gemini AI"
4. Klicken Sie auf "API-Schluessel konfigurieren..."
5. Fuegen Sie Ihren API-Schluessel ein und druecken Sie OK

## Tastenkuerzel

| Kuerzel | Aktion |
|---------|--------|
| NVDA+G | Gemini AI-Dialog oeffnen |
| NVDA+Umschalt+E | Gesamten Bildschirm beschreiben |
| NVDA+Umschalt+O | Navigatorobjekt beschreiben |
| NVDA+V | Videoaufnahme zur Analyse starten/stoppen |
| NVDA+Umschalt+U | Ausgewaehlten Text zusammenfassen |

## Den Gemini-Dialog verwenden

Wenn Sie den Gemini-Dialog mit NVDA+G oeffnen:

1. **Modell**: Waehlen Sie das zu verwendende Gemini-Modell
2. **Systemaufforderung**: Optionale Anweisungen, wie Gemini antworten soll
3. **Verlauf**: Konversationsverlauf anzeigen
4. **Nachricht**: Geben Sie Ihre Nachricht oder Frage ein
5. **Senden**: Senden Sie Ihre Nachricht an Gemini
6. **Bild anhaengen**: Bilddatei zur Analyse durch Gemini hinzufuegen
7. **Loeschen**: Konversationsverlauf loeschen
8. **Antwort kopieren**: Letzte Antwort in die Zwischenablage kopieren

### Tipps fuer den Dialog

* Druecken Sie ctrl+enter im Nachrichtenfeld zum schnellen Senden
* Verwenden Sie Tab, um zwischen Steuerelementen zu navigieren
* Der Verlauf aktualisiert sich automatisch waehrend des Chats
* Angehaengte Bilder werden mit Ihrer naechsten Nachricht gesendet

## Einstellungen

Zugriff auf Einstellungen ueber NVDA-Menue > Einstellungen > Optionen > Gemini AI:

* **Standardmodell**: Waehlen Sie Ihr bevorzugtes Gemini-Modell
* **Temperatur (0-200)**: Steuert die Kreativitaet der Antworten (0=fokussiert, 200=kreativ)
* **Max. Ausgabe-Tokens**: Maximale Laenge der Antworten
* **Antworten streamen**: Antworten anzeigen, waehrend sie ankommen
* **Konversationsmodus**: Chat-Verlauf fuer Kontext einbeziehen
* **Systemaufforderung merken**: Ihre benutzerdefinierte Aufforderung speichern
* **Escape-Taste blockieren**: Versehentliches Schliessen des Dialogs verhindern
* **Markdown filtern**: Markdown-Formatierung aus Antworten entfernen

### Akustische Rueckmeldung

* **Ton bei Anfrage abspielen**: Audiobestaetigung beim Senden der Nachricht
* **Ton waehrend des Wartens abspielen**: Fortschrittston waehrend der KI-Verarbeitung
* **Ton bei Antwort abspielen**: Benachrichtigung bei Ankunft der Antwort

## Verfuegbare Modelle

* **Gemini 3 Pro (Preview)**: Leistungsfaehigstes Modell mit Denkfaehigkeiten
* **Gemini 3 Flash (Preview)**: Schnelles Modell mit Denkfaehigkeiten
* **Gemini 2.5 Pro**: Produktionsbereites leistungsstarkes Modell
* **Gemini 2.5 Flash**: Schnell und effizient fuer die meisten Aufgaben
* **Gemini 2.5 Flash-Lite**: Leichtgewichtig und schnellste Antworten
* **Gemini 2.5 Flash Image**: Optimiert fuer bildbezogene Aufgaben

## Bild- und Videofunktionen

### Bildschirmbeschreibung (NVDA+Umschalt+E)

Erfasst Ihren gesamten Bildschirm und sendet ihn an Gemini fuer eine detaillierte Beschreibung. Nuetzlich fuer:

* Unbekannte Oberflaechen verstehen
* Einen Ueberblick ueber visuellen Inhalt erhalten
* Elemente identifizieren, die NVDA nicht beschreiben kann

### Objektbeschreibung (NVDA+Umschalt+O)

Erfasst nur das aktuelle Navigatorobjekt. Nuetzlich fuer:

* Bestimmte UI-Elemente beschreiben
* Bilder oder Symbole verstehen
* Details zu fokussierten Steuerelementen erhalten

### Videoanalyse (NVDA+V)

1. Druecken Sie NVDA+V, um die Aufnahme zu starten
2. Fuehren Sie die Aktionen aus, die Sie analysieren moechten
3. Druecken Sie erneut NVDA+V, um zu stoppen
4. Warten Sie, bis Gemini das Video analysiert

Nuetzlich fuer:

* Visuelle Arbeitsablaeufe verstehen
* Schritt-fuer-Schritt-Beschreibungen erhalten
* Dynamische Inhalte analysieren

### Auswahl zusammenfassen (NVDA+Umschalt+U)

Waehlen Sie Text in einer beliebigen Anwendung aus und lassen Sie Gemini die wichtigsten Punkte zusammenfassen. Funktioniert im Lesemodus (Webbrowser, PDF-Betrachter) und in normalen Textfeldern. Die Zusammenfassungsaufforderung kann in den Erweiterungseinstellungen angepasst werden.

## Fehlerbehebung

### "Google GenAI-Bibliothek nicht installiert"

Fuehren Sie den Abhaengigkeitsinstaller aus:
1. Navigieren Sie zu %APPDATA%\nvda\addons\GemVDA
2. Fuehren Sie install_deps.bat oder install_deps.py aus
3. Starten Sie NVDA neu

### "Kein API-Schluessel konfiguriert"

Konfigurieren Sie Ihren API-Schluessel unter Optionen > Gemini AI > API-Schluessel konfigurieren

### Antworten sind zu kurz oder abgeschnitten

Erhoehen Sie die Einstellung "Max. Ausgabe-Tokens"

### Antworten sind zu zufaellig

Reduzieren Sie die Temperatureinstellung (versuchen Sie 50-100)

## Datenschutzhinweis

* Ihre Nachrichten und Bilder werden an die Google Gemini API gesendet
* API-Schluessel werden lokal in Ihrer NVDA-Konfiguration gespeichert
* Keine Daten werden mit dem Erweiterungsentwickler geteilt
* Lesen Sie die KI-Datenschutzrichtlinie von Google fuer Details

## Support

* Probleme melden: [GitHub Issues](https://github.com/ogomez92/GemVDA/issues)
* Quellcode: [GitHub Repository](https://github.com/ogomez92/GemVDA)

## Lizenz

Diese Erweiterung wird unter der GNU General Public License v2 veroeffentlicht.

## Autor

Oriol Gomez Sentis
