import cv2

camera = cv2.VideoCapture(0)
print("Vision Inspection Script Active... Press 'q' to exit.")

while True:
    ret, frame = camera.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    cv2.imshow("Live Video Feed", frame)
    cv2.imshow("Automated Defect Tracking", edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()

