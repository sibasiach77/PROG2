<h1>Trainingsplaner</h1>

<h2>1 Ausganslage</h2>

Aktuell plane ich die Trainings für den Turnverein spontan und kurzfristig vor dem Training.

<h2>2 Projektidee</h2>

Die Webapplikation soll mir die Planung der Trainings erleichtern, in dem ich anhand von verschiedenen Kriterien einen Vorschlag erhalte. Auf der Übersicht möchte ich sehen, was in den letzten Trainings gemacht wurde, um abwechslungsreiche Trainings zu gestalten.

<h2>3 Anleitung</h2>

<h3>Home</h3>
<ul>
    <li>Durch das Anwählen des jeweiligen Buttons gelangt der User auf die Seiten Abfrage, Erfassen oder Übersicht</li>
</ul>

<h3>Erfassen</h3>
<ul>
    <li>Der User kann eine neue Trainingseinheit erfassen. Folgende Daten müssen eingegeben werden:</li>
        <ul>
            <li>Name (Text)</li>
            <li>Typ (Auswahl)</li>
                <ul>
                    <li>Spiel</li>
                    <li>Krafttraining</li>
                    <li>Ausdauertraining</li>
                    <li>externe Aktivität</li>
                </ul>
            <li>Ort (Auswahl)</li>
                <ul>
                    <li>Drinnen</li>
                    <li>Draussen</li>
                </ul>
            <li>Gruppengrösse (Zahl) </li>
                <ul>
                    <li>maximale Gruppengrösse</li>
                    <li>minimale Gruppengrösse</li>
                </ul>
            <li>Dauer (Zahl) </li>
                <ul>
                    <li>minimale Dauer</li>
                    <li>maximale Dauer</li>
                </ul>
        </ul>
    <li>Die Eingabe wird mit Klick auf den Button "neue Trainingseinheit erfassen" in einem Dictonary in einer Json-Datei gespeichert</li>
        <ul>
            <li>Wird ein Feld leer gelassen, erscheint eine Fehlermeldung</li>
            <li>Die Felder welche eine Zahl benötigen, müssen einen Wert grösser gleich 1 haben, ansonsten erscheint eine Fehlermeldung</li>
        </ul>
</ul>

<h3>Abfrage</h3>
<ul>
    <li>Der User kann eine Abfrage starten. Folgende Daten müssen eingegeben werden:</li>
        <ul>
            <li>Datum</li>
            <li>Typ (Auswahl)</li>
                <ul>
                    <li>Spiel</li>
                    <li>Krafttraining</li>
                    <li>Ausdauertraining</li>
                    <li>externe Aktivität</li>
                </ul>
            <li>Ort (Auswahl)</li>
                <ul>
                    <li>Drinnen</li>
                    <li>Draussen</li>
                </ul>
            <li>Gruppengrösse (Zahl) </li>
            <li>Dauer (Zahl) </li>
        </ul>
    <li>Wird der Button "Vorschläge angezeigen" angewählt, werden die Angaben des Users mittels einer For-Schleife mit den Einträgen in der Datenbank verglichen</li>
        <ul>
            <li>Wird ein Feld leer gelassen, erscheint eine Fehlermeldung</li>
            <li>Die Felder welche eine Zahl benötigen, müssen einen Wert grösser gleich 1 haben, ansonsten erscheint eine Fehlermeldung</li>
        </ul>
    <li>Übereinstimmende Trainingseinheiten werden in der Json Datenbank gespeichert und ausgegebenen</li>
    <li>Gibt es kein passendes Training, kann der User die Abfrage erneut starten</li>
    <li>Gibt es ein passendes Training, kann der User dieses mit anwählen und auf "Vorschlag speichern" klicken</li>
    <li>Die Trainingseinheit wird in einer Json Datenbank gespeichert</li>
    <li>Es können mehrere Trainingseinheit auf ein Datum bezogen erfasst werden, das Datum ist der äusserste Wert des Dictonarys</li>
</ul>

<h3>Übersicht</h3>
<ul>
    <li>Die gespeicherten Trainings werden mithilfe einer For-Schleife auf der Seite Übersicht ausgegeben</li>
    <ul>Die Dauer der einzelnen Traingseinheiten wird addiert und als Dauer gesamt ausgegeben</ul>
</ul>

<h2>Workflow</h2>