# AI-Automation-Agentur – Plan & Notizen

> Zusammenfassung unserer Besprechung. In einer neuen Sitzung einfach diese Datei
> öffnen und sagen: „Lies AI-AGENTUR-PLAN.md, wir machen da weiter."

## Geschäftsmodell
AI-Agenten als **Dienstleistung an lokale Unternehmen verkaufen**:
Kosmetikstudios, Coaches, Restaurants, Friseure, Hotels usw.

---

## Die 3 Agenten (Produkte)

### 1. 💬 AI Chatbot (Website) — START, am einfachsten ✅
- Beantwortet Website-Chats 24/7 (Termine, Öffnungszeiten, Preise, FAQ)
- **Voll baubar, keine Plattform-Genehmigung nötig**
- Braucht: KI-API-Key (Claude) + eine Website zum Einbinden
- Claude Code baut: Chat-Widget + Backend + Branding

### 2. 📞 AI Voice Agent (verpasste Anrufe) — mittel-schwer 🟡
- Beantwortet verpasste Anrufe, sichert Kundenanfragen
- Braucht: Telefonie-Dienst (Vapi / Retell AI / Twilio), Telefonnummer
- Kostet **pro Minute** Gesprächszeit
- ⚠️ Bei Anruf-Aufzeichnung: Ansage-/Einwilligungspflicht (DSGVO)

### 3. 📱 Social Media AI — am schwersten + riskant 🔴
- Posts vorplanen ✅ (erlaubt)
- Auto-Antworten auf DMs/Kommentare ⚠️ braucht Meta-API-Freigabe
  UND kann gegen Plattformregeln verstoßen → **Konto-Sperrgefahr** (auch beim Kunden!)
- Sicherer Teil: Post-Planung (ManyChat / Meta-Tools)

---

## Wichtige Realitäten (weil wir es VERKAUFEN)
1. **Muss zuverlässig laufen** – keine Bastel-Skripte, sonst wütende Kunden.
2. **Laufende Kosten pro Kunde** (Voice/Minute, LLM/Anfrage, Nummern, Hosting)
   → Preis so kalkulieren, dass Kosten gedeckt + Gewinn bleibt.
3. **🇩🇪 DSGVO**: Kundendaten werden verarbeitet → Auftragsverarbeitungsverträge (AVV),
   Einwilligungen, Datenschutzerklärungen nötig. Haftung liegt bei dir.
4. **Profi-Weg**: NICHT alles von Null bauen. Fertige Plattformen (Vapi, Retell,
   ManyChat) + eigene Anpassung kombinieren. Claude Code baut die individuellen Teile.

### Grenzen von Claude Code
- Schreibt den **Code**, kann aber **nichts dauerhaft hosten** (nur pro Sitzung da).
- Agenten müssen auf einem **Server/PC** laufen.
- Plattform-Sperren (Pinterest/Etsy/Meta-API) lassen sich nicht „wegcoden".

---

## Akquise-Stack (Kunden gewinnen)

### A. 🗂️ Lead-Listen-Tool — baubar
- Zieht **öffentliche Firmendaten** (z. B. Friseure einer Stadt) aus
  Google Maps / Google Places API: Name, Adresse, Website, Telefon.

### B. ✍️ KI-Nachrichten-/E-Mail-Texter — leicht baubar
- Personalisierte Ansprache pro Firma (Branche + Name).

### C. 🤖 Vollautomatischer Versand (Instantly-Style) — ⚠️ VORSICHT
- **In Deutschland rechtlich riskant!**
  - Kalte Werbe-E-Mails an Firmen ohne Einwilligung = **§7 UWG verboten** (auch B2B)
    → Abmahngefahr (mehrere hundert € pro Fall).
  - Kalt anrufen nur bei „mutmaßlicher Einwilligung" (Graubereich).
  - Adress-Scraping berührt DSGVO.
- **Sauberere Wege**: Kontakte mit Einwilligung (Lead-Magnet/Website),
  persönliche statt Massen-Mails, LinkedIn/Telefon mit Augenmaß.

---

## Empfohlene Reihenfolge (Roadmap)
1. ✅ **Chatbot-Demo bauen** (zeigbares Produkt für erste Kunden)
2. **Lead-Listen-Tool** (Google Maps → Firmenliste)
3. **KI-Texter** für die Ansprache
4. Später: Voice Agent, dann Social-Media-Planung
> Ohne vorzeigbares Produkt bringt der beste Outreach nichts → erst Produkt, dann Akquise.

---

## Offene Punkte / als Nächstes klären
- [ ] Anthropic/Claude-**API-Key** vorhanden? (Wenn nicht: einrichten)
- [ ] **Branche** für die erste Chatbot-Demo (z. B. Friseur)?
- [ ] Hosting-Frage klären (wo sollen die Agenten laufen?)
- [ ] DSGVO-Grundlagen vorbereiten (Datenschutzerklärung, AVV-Vorlage)

## Nächster Schritt
👉 **AI Chatbot (Website) als funktionierende Demo bauen.**
