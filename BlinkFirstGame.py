import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

first_read = True

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
ret, img = capture.read()

while ret:
    ret, img = capture.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 5, 1, 1)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5, minSize=(200, 200))
    if len(faces) > 0:
        for (x, y, w, h) in faces:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            roi_face = gray[y:y + h, x:x + w]
            roi_face_clr = img[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_face, 1.3, 5, minSize=(50, 50))

            # TWOJE ROZWIAZANIE
    else:
        text = "no face detected"
        text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_PLAIN, 1, 2)[0]
        textX = (img.shape[1] - text_size[0]) // 2
        cv2.putText(img, "no face detected", (textX, 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1,
                    cv2.LINE_AA)

    cv2.imshow('img', img)
    a = cv2.waitKey(1)
    if a == ord('q'):
        break
    # TWOJE ROZWIAZANIE

capture.release()
cv2.destroyAllWindows()
