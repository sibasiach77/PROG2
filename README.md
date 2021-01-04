<h1>1 Ausganslage</h1>

Aktuell plane ich die Trainings für den Turnverein spontan und kurzfristig vor dem Training.

<h2>2 Projektidee</h2>

Die Webapplikation soll mir die Planung der Trainings erleichtern, in dem ich anhand verschiedenen Kriterien einen Vorschlag erhalte. Auf der Übersicht möchte ich sehen, was in den letzten Trainings gemacht wurde, um abwechslungsreiche Trainings zu gestalten.

<h2>3 Workflow</h2>

<h3>3.1 Erfassen</h3>

Im Formular "Erfassen" kann eine neue Trainingseinheit erfasst werden. Dazu müssen die Felder Name, Typ (Auswahl zwischen Spiel, Krafttraining, Ausdauertraining und externe Aktivität), Ort (drinnen/draussen), Gruppengrösse (minimale und maximale Personenanzahl) und Dauer (minimale und maximale Dauer) ausgefüllt werden. Die erfassten Traingseinheiten werden als Dictonary in einer Json-Datei gespeichert.

<h3>3.2 Abfrage</h3>

Im Formular Abfrage werden die Daten Datum, Typ, Ort, Gruppengrösse und Dauer anhand des anstehenden Trainings vom User befüllt. Klickt man auf "Vorschläge anzeigen", wird mithilfe einer For-Schleife überprüft, welche erfasste(n) Trainingseinheit(en) (Schritt 3.1) den eingegebenen Kriterien entsprechen. Eine Auswahl von passenden Trainingseinheiten werden angezeigt. Die Vorschläge werden in einer Json-Datei gespeichert und ausgegeben. Die Json-Datei wird jedoch immer wieder überschrieben, da die Daten nur bei einmalig verfügbar sein müssen. 

Nun kann eine Trainingseinheit ausgewählt und gespeichert werden. Diese wird wiederum in einer Datenbank gespeichert. Es können mehrere Trainingseinheiten pro Datum geplant werden. Die Dictonary Struktur ist so aufgebaut, dass das Datum der äusserste Wert ist.
Wurde eine Trainingseinheit gespeichert, kommt der User auf die Seite "Übersicht".

<h3>3.3 Übersicht</h3>

Auf der Seite Übersicht sind alle gespeicherten Traininseinheiten, welche auf ein Datum erfasst wurden, ersichtlich. 


<h1>Autorin</h1>
Nadine Hutter

<h1>Dozent</h1>
Fabian Odoni

<h1>Abgabe</h1>
22.01.2021