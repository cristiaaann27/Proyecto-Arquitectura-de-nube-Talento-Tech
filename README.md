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

### Backend

- **`app.py`**: Archivo principal de la aplicación Flask que define las rutas y configura el servicio de reconocimiento de voz.
- **`voice_routes.py`**: Archivo que contiene las rutas específicas para manejar las solicitudes de reconocimiento de voz.
- **`.env`**: Archivo para almacenar variables de entorno como claves de API y configuraciones del servicio de voz.
- **`requirements.txt`**: Archivo de configuración que lista todas las dependencias necesarias para el backend.

### Frontend

- **`public/`**: Carpeta que contiene archivos estáticos como el `index.html` que sirve como punto de entrada para la aplicación React.
  - **`index.html`**: Archivo HTML principal que se carga en el navegador.
- **`src/`**: Carpeta que contiene el código fuente de la aplicación React.
  - **`components/`**: Carpeta para componentes React reutilizables.
    - **`VoiceCommand.js`**: Componente para manejar la interacción de comandos de voz.
  - **`App.js`**: Componente principal de la aplicación que define la estructura de la interfaz de usuario.
  - **`index.js`**: Archivo de entrada que renderiza la aplicación React en el DOM.
- **`package.json`**: Archivo de configuración para gestionar dependencias y scripts del proyecto frontend.
- **`package-lock.json`**: Archivo de bloqueo que asegura la versión consistente de las dependencias instaladas.

### Configuración Adicional

- **Archivos `.gitignore`**: Asegúrate de tener un archivo `.gitignore` en la raíz del proyecto para excluir archivos y carpetas no deseados, como `node_modules/` en el frontend y `venv/` en el backend.

Esta estructura te ayudará a mantener tu proyecto organizado y facilitará la colaboración con otros desarrolladores. Asegúrate de adaptar esta estructura según las necesidades específicas de tu proyecto.


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



