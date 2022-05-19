# Tasks
## Zadanie 1
Popraw błędy w kodzie tak, aby osiągnąć następujące cele.
1) Linia powinna złapać ramkę wideo, ją zdekodować i zwrócić wartość logiczną wskazującą, czy ramka została przechwycona. Kod do poprawienia:
```
ret, img = capture.open()
```
2) Dokonaj konwersji kolorowego obrazu do skali szarości. Kod do poprawienia:
```
gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
```
3) Fragment kodu ma poprawnie wykrywać twarz za pomocą kaskady. Kod do poprawienia:
```
if len(faces) >= 0:
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img, "Driver", (x - 10, y - 10), font, 1, (0, 255, 0), 1, cv2.LINE_AA)
```

## Zadanie 2
Twoim zadaniem jest zaimplementowanie gry "Kto pierwszy mrugnie".

Założenia:
- Po wykryciu pary oczu - wyświetlić napis "Press s to begin" 
- Jeśli nie wykryto oczu - wyświetlić napis "No eyes detected"
- Po naciśnięciu klawiszu 's' - początek gry
- Gdy oczy są otwarte, wyświetlać '.' - ilość kropek to ilość zdobytych punktów
- Po mrugnięciu - otrzymujemy informację, że przegraliśmy. Koniec gry

Powodzenia!
