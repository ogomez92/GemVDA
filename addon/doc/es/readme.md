# GemVDA - Google Gemini AI para NVDA

## Resumen

GemVDA integra las capacidades de Google Gemini AI directamente en NVDA, proporcionando a los usuarios ciegos y con discapacidad visual asistencia de IA potente. El complemento soporta varios modelos de Gemini incluyendo Gemini 3, Gemini 2.5 Pro y variantes Flash para chat, descripcion de imagenes, analisis de video y mas.

## Caracteristicas

* **Chat con IA**: Mantener conversaciones con Gemini AI directamente desde NVDA
* **Descripcion de pantalla**: Capturar y describir la pantalla completa
* **Descripcion de objeto**: Describir el objeto del navegador actual
* **Analisis de video**: Grabar video de pantalla y que Gemini lo analice
* **Adjuntar imagenes**: Adjuntar imagenes desde archivos para descripcion por IA
* **Historial de conversacion**: Mantener contexto a traves de multiples mensajes
* **Multiples modelos**: Elegir entre varios modelos de Gemini segun tus necesidades
* **Configuracion personalizable**: Configurar temperatura, tokens, streaming y mas

## Requisitos

* NVDA 2023.1 o posterior
* Clave API de Google Gemini (nivel gratuito disponible)
* Conexion a internet

## Configuracion

### Obtener una clave API

1. Visita [Google AI Studio](https://aistudio.google.com/apikey)
2. Inicia sesion con tu cuenta de Google
3. Crea una nueva clave API
4. Copia la clave para usarla en el complemento

### Configurar la clave API

1. Presiona NVDA+N para abrir el menu de NVDA
2. Ve a Preferencias > Opciones
3. Selecciona la categoria "Gemini AI"
4. Haz clic en "Configurar clave API..."
5. Pega tu clave API y presiona Aceptar

## Atajos de teclado

| Atajo | Accion |
|-------|--------|
| NVDA+G | Abrir dialogo de Gemini AI |
| NVDA+Shift+E | Describir la pantalla completa |
| NVDA+Shift+O | Describir el objeto del navegador |
| NVDA+V | Iniciar/detener grabacion de video para analisis |

## Usar el dialogo de Gemini

Cuando abres el dialogo de Gemini con NVDA+G:

1. **Modelo**: Selecciona que modelo de Gemini usar
2. **Indicacion del sistema**: Instrucciones opcionales sobre como debe responder Gemini
3. **Historial**: Ver el historial de conversacion
4. **Mensaje**: Escribe tu mensaje o pregunta
5. **Enviar**: Enviar tu mensaje a Gemini
6. **Adjuntar imagen**: Agregar un archivo de imagen para que Gemini analice
7. **Limpiar**: Limpiar el historial de conversacion
8. **Copiar respuesta**: Copiar la ultima respuesta al portapapeles

### Consejos para el dialogo

* Presiona Enter en el campo de mensaje para enviar rapidamente
* Usa Tab para navegar entre controles
* El historial se actualiza automaticamente mientras chateas
* Las imagenes adjuntas se envian con tu proximo mensaje

## Opciones

Accede a las opciones via menu de NVDA > Preferencias > Opciones > Gemini AI:

* **Modelo predeterminado**: Elige tu modelo de Gemini preferido
* **Temperatura (0-200)**: Controla la creatividad de respuesta (0=enfocado, 200=creativo)
* **Tokens maximos de salida**: Longitud maxima de respuestas
* **Transmitir respuestas**: Mostrar respuestas mientras llegan
* **Modo conversacion**: Incluir historial de chat para contexto
* **Recordar indicacion del sistema**: Guardar tu indicacion personalizada
* **Bloquear tecla Escape**: Prevenir cierre accidental del dialogo
* **Filtrar markdown**: Eliminar formato markdown de las respuestas

### Retroalimentacion sonora

* **Reproducir sonido al enviar solicitud**: Confirmacion de audio cuando se envia el mensaje
* **Reproducir sonido mientras espera**: Sonido de progreso durante el procesamiento de IA
* **Reproducir sonido al recibir respuesta**: Notificacion cuando llega la respuesta

## Modelos disponibles

* **Gemini 3 Pro (Preview)**: Modelo mas capaz con capacidades de razonamiento
* **Gemini 3 Flash (Preview)**: Modelo rapido con capacidades de razonamiento
* **Gemini 2.5 Pro**: Modelo potente listo para produccion
* **Gemini 2.5 Flash**: Rapido y eficiente para la mayoria de tareas
* **Gemini 2.5 Flash-Lite**: Ligero y respuestas mas rapidas
* **Gemini 2.5 Flash Image**: Optimizado para tareas relacionadas con imagenes

## Funciones de imagen y video

### Descripcion de pantalla (NVDA+Shift+E)

Captura tu pantalla completa y la envia a Gemini para una descripcion detallada. Util para:

* Entender interfaces desconocidas
* Obtener una vision general del contenido visual
* Identificar elementos que NVDA no puede describir

### Descripcion de objeto (NVDA+Shift+O)

Captura solo el objeto del navegador actual. Util para:

* Describir elementos especificos de la interfaz
* Entender imagenes o iconos
* Obtener detalles sobre controles enfocados

### Analisis de video (NVDA+V)

1. Presiona NVDA+V para iniciar la grabacion
2. Realiza las acciones que quieres analizar
3. Presiona NVDA+V de nuevo para detener
4. Espera a que Gemini analice el video

Util para:

* Entender flujos de trabajo visuales
* Obtener descripciones paso a paso
* Analizar contenido dinamico

## Solucion de problemas

### "Biblioteca Google GenAI no instalada"

Ejecuta el instalador de dependencias:
1. Navega a %APPDATA%\nvda\addons\GemVDA
2. Ejecuta install_deps.bat o install_deps.py
3. Reinicia NVDA

### "No hay clave API configurada"

Configura tu clave API en Opciones > Gemini AI > Configurar clave API

### Las respuestas son muy cortas o se cortan

Aumenta la configuracion de "Tokens maximos de salida"

### Las respuestas son muy aleatorias

Reduce la configuracion de Temperatura (intenta 50-100)

## Nota de privacidad

* Tus mensajes e imagenes se envian a la API de Gemini de Google
* Las claves API se almacenan localmente en tu configuracion de NVDA
* No se comparten datos con el desarrollador del complemento
* Revisa la politica de privacidad de IA de Google para mas detalles

## Soporte

* Reportar problemas: [GitHub Issues](https://github.com/ogomez92/GemVDA/issues)
* Codigo fuente: [GitHub Repository](https://github.com/ogomez92/GemVDA)

## Licencia

Este complemento se publica bajo la Licencia Publica General GNU v2.

## Autor

Oriol Gomez Sentis
