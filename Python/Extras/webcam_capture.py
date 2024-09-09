import cv2

try:
    # Inicializando a webcam (0 é o ID padrão da webcam)
    cap = cv2.VideoCapture(0)

    # Verificando se a webcam foi aberta com sucesso
    if not cap.isOpened():
        print("Erro ao abrir a webcam")
        exit()

    # Definindo a resolução da webcam
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:
        # Captura frame por frame
        ret, frame = cap.read()

        if not ret:
            print("Falha ao capturar a imagem")
            break

        # Mostra o frame capturado
        cv2.imshow('Webcam - Pressione Q para sair', frame)

        # Pressione 'q' para sair do loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
except Exception as e:
    print(f"Erro: {e}")

# Libera a webcam e fecha todas as janelas abertas
if 'cap' in locals():
    cap.release()
cv2.destroyAllWindows()
