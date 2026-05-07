import cv2
import numpy as np
import time

erro = 0
erroA = 0

# def constrain(valor, minimo, maximo):
#     return max(min(valor, maximo), minimo)

# # Simulação dos motores (mostra valores no terminal)
# def motorE(vel):
#     vel = constrain(vel, -100, 100)
#     print(f"Motor E: {vel:.2f}")

# def motorD(vel):
#     vel = constrain(vel, -100, 100)
#     print(f"Motor D: {vel:.2f}")

# def segueLinha():

#     global erro
#     global erroA

#     kp = 1.5
#     kd = 1.2

#     velBase = 60
#     centro = 120

#     proporcional = erro * kp
#     derivada = (erro - erroA) * kd

#     controle = proporcional + derivada

#     velE = velBase + controle
#     velD = velBase - controle

#     velE = constrain(velE, -100, 100)
#     velD = constrain(velD, -100, 100)

#     motorE(velE)
#     motorD(velD)

#     erroA = erro

# Webcam (substitui Picamera2)
cap = cv2.VideoCapture(0)

centro = 120

while True:

    ret, im = cap.read()

    if not ret:
        print("Erro ao capturar imagem")
        break

    # Redimensiona para igual ao Raspberry
    im = cv2.resize(im, (240, 120))

    # Cortar parte inferior
    im = im[60:120, 0:240]

    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    gray = cv2.GaussianBlur(gray, (5,5), 0)

    _, thresh = cv2.threshold(
        gray,
        100,
        255,
        cv2.THRESH_BINARY_INV
    )

    contours, _ = cv2.findContours(
        thresh,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    if contours:

        c = max(contours, key=cv2.contourArea)

        if cv2.contourArea(c) > 200:

            M = cv2.moments(c)

            if M["m00"] != 0:

                cx = int(M["m10"] / M["m00"])

                erro = cx - centro

                cv2.circle(im, (cx, 30), 5, (0,255,0), -1)

        # segueLinha()
        print(erro)

    cv2.imshow("Camera", im)
    cv2.imshow("Thresh", thresh)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()