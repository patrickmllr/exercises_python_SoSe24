def buchstaben_ändern(string, buchstabe):
    # Vokale, die als Ersatz verwendet werden sollen
    vokale = 'aeiou'
    # Konvertiere den Buchstaben zu Kleinbuchstaben für den Fall, dass er großgeschrieben ist
    buchstabe = buchstabe.lower()
    # Initialisiere den Ergebnisstring
    ergebnis = ''
    # Durchlaufe jeden Buchstaben im Eingabestring
    for char in string:
        # Überprüfe, ob der Buchstabe ein Vokal ist und ersetze ihn dann durch die anderen Vokale
        if char.lower() == buchstabe:
            for vokal in vokale:
                # Füge den ersetzen Vokal dem Ergebnisstring hinzu
                ergebnis += vokal
        else:
            # Füge den Buchstaben unverändert dem Ergebnisstring hinzu
            ergebnis += char
    return ergebnis

# Testen der Funktion
print(buchstaben_ändern(string="banana", buchstabe="a"))
print(buchstaben_ändern(string="Wie geht es Ihnen?", buchstabe="e"))

