# Proyecto-Arquitectura-de-nube-Talento-Tech

# Asistente Virtual con Reconocimiento de Voz

## Descripción

Este proyecto es un asistente virtual que utiliza el servicio de reconocimiento de voz de Azure Cognitive Services para convertir la voz en texto. La aplicación está dividida en dos partes principales: un backend en Python con Flask y un frontend en React.

## Tecnologías Utilizadas

- **Backend**:
  - [Flask](https://flask.palletsprojects.com/en/2.1.x/): Framework web en Python.
  - [Azure Cognitive Services - Speech](https://azure.microsoft.com/en-us/services/cognitive-services/speech-to-text/): Servicio de reconocimiento de voz.

- **Frontend**:
  - [React](https://reactjs.org/): Biblioteca para construir interfaces de usuario.
  - [Axios](https://axios-http.com/): Cliente HTTP para realizar solicitudes al backend.

## Estructura del Proyecto
my-voice-assistant/
│
├── backend/
│ ├── app.py
│ ├── voice_routes.py
│ ├── .env
│ ├── requirements.txt
│ └── ...
│
└── frontend/
├── public/
│ ├── index.html
│ └── ...
├── src/
│ ├── components/
│ ├── App.js
│ ├── index.js
│ └── ...
├── package.json
├── package-lock.json
└── ...

## Instalación

### Backend

1. **Clonar el Repositorio**:

    ```bash
    git clone https://github.com/yourusername/your-repository.git
    ```

2. **Navegar al Directorio del Backend**:

    ```bash
    cd my-voice-assistant/backend
    ```

3. **Crear y Activar el Entorno Virtual**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

4. **Instalar Dependencias**:

    ```bash
    pip install -r requirements.txt
    ```

5. **Configurar Variables de Entorno**:
   - Crea un archivo `.env` en el directorio del backend con las siguientes variables:

    ```env
    SPEECH_KEY=your_speech_key
    SPEECH_REGION=your_speech_region
    ```

6. **Iniciar el Servidor**:

    ```bash
    python app.py
    ```

### Frontend

1. **Navegar al Directorio del Frontend**:

    ```bash
    cd my-voice-assistant/frontend
    ```

2. **Instalar Dependencias**:

    ```bash
    npm install
    ```

3. **Iniciar el Servidor de Desarrollo**:

    ```bash
    npm start
    ```

   - La aplicación se abrirá en `http://localhost:3000`.

## Uso

1. **Iniciar el Backend**: Asegúrate de que el backend esté corriendo en `http://localhost:5000`.

2. **Iniciar el Frontend**: Asegúrate de que el frontend esté corriendo en `http://localhost:3000`.

3. **Interactuar con la Aplicación**:
   - Usa el frontend para enviar comandos de voz al backend.
   - El backend procesará los comandos y enviará las respuestas de vuelta al frontend.

## Contribución

Si deseas contribuir al proyecto, por favor sigue estos pasos:

1. **Haz un Fork del Repositorio**.
2. **Crea una Rama para tu Cambio**:
    ```bash
    git checkout -b my-feature-branch
    ```
3. **Realiza tus Cambios y Realiza un Commit**:
    ```bash
    git commit -am 'Añadí una nueva característica'
    ```
4. **Sube tu Rama**:
    ```bash
    git push origin my-feature-branch
    ```
5. **Crea una Solicitud de Extracción (Pull Request)** en GitHub.

## Licencia

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE).



