import cv2
from fer import FER

def translate_emotion(emotion) -> str:
    try:
        emotions = {
            'angry': "Bravo", 
            'disgust': "Desgostoso",
            'fear': "Medo",
            'happy': "Feliz",
            'sad': "Triste",
            'surprise': "Surpreso",
            'neutral': "Neutro"
        }
        return emotions[emotion]
    except KeyError:
        return "Desconhecido"

try:

    detector = FER()
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

        # Detecta emoções faciais no frame
        emotions = detector.detect_emotions(frame)
        for emotion in emotions:
            box = emotion.get('box', (0, 0, 0, 0))
            (x, y, w, h) = box
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
            
            dominant_emotion = ""
            actual_dominant = 0

            for emotion_captured, value in emotion['emotions'].items():
                if value > actual_dominant:
                    dominant_emotion = translate_emotion(emotion_captured)
                    actual_dominant = value

            cv2.putText(frame, dominant_emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)

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
