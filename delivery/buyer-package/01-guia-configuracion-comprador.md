# Guía de configuración para el comprador

Producto: Agente IA para WhatsApp en n8n
Precio de lanzamiento: $100 USD
Sitio: https://pymesconia.com
Checkout: https://buy.stripe.com/dRm3cub7nbGj0oq3BX2ZO01

## Qué estás instalando

Este paquete instala un primer agente para WhatsApp que ayuda a una PYME a responder más rápido, ordenar prospectos y dejar seguimiento listo.

El flujo base hace esto:

1. Recibe un mensaje entrante desde WhatsApp Cloud API.
2. Lee una base de conocimiento simple de tu negocio.
3. Responde preguntas frecuentes en español.
4. Clasifica la conversación: nuevo lead, interesado, comprador listo, soporte, humano requerido.
5. Guarda el lead en Google Sheets o en un CSV local si todavía no tienes Sheets conectado.
6. Avisa al dueño cuando la conversación necesita intervención humana.

## Archivos incluidos

- `../whatsapp-agent-n8n/pymes-whatsapp-lead-response-agent.workflow.json` — workflow importable en n8n.
- `../whatsapp-agent-n8n/.env.example` — variables necesarias, sin secretos reales.
- `../whatsapp-agent-n8n/lead-log-template.csv` — CSV base para registro local.
- `03-plantilla-faq-base-conocimiento.md` — contenido que debes adaptar a tu negocio.
- `04-plantilla-registro-leads.md` — guía para Google Sheets o CSV.
- `05-reglas-handoff-escalamiento.md` — reglas para pasar una conversación a humano.
- `06-troubleshooting.md` — problemas comunes y solución.
- `07-materiales-youtube-whatsapp.md` — textos para atraer leads desde YouTube a WhatsApp.

## Requisitos antes de empezar

Necesitas:

- Una cuenta de n8n Cloud o una instalación propia de n8n.
- Una cuenta de Meta Business con WhatsApp Business Platform activo.
- Un número de WhatsApp conectado a Meta.
- Un token vigente de Meta WhatsApp Cloud API.
- Una API key de OpenAI o proveedor compatible.
- Una cuenta de Google para registrar leads en Sheets, o usar el CSV local al inicio.

## Paso 1 — Importar el workflow en n8n

1. Entra a n8n.
2. Ve a Workflows.
3. Haz clic en Import from File.
4. Sube `pymes-whatsapp-lead-response-agent.workflow.json`.
5. Guarda el workflow.
6. Déjalo inactivo mientras configuras credenciales.

No actives el workflow antes de conectar Meta, OpenAI y la hoja de leads.

## Paso 2 — Configurar variables del negocio

Usa `.env.example` como referencia. Estas variables no deben compartirse públicamente.

Variables principales:

- `BUSINESS_NAME`: nombre de tu negocio.
- `OWNER_WHATSAPP`: teléfono del dueño o equipo en formato internacional, sin `+`.
- `META_PHONE_NUMBER_ID`: ID del número de WhatsApp en Meta.
- `META_ACCESS_TOKEN`: token vigente de Meta.
- `META_VERIFY_TOKEN`: palabra secreta que tú eliges para verificar el webhook.
- `OPENAI_API_KEY`: API key del modelo.
- `OPENAI_MODEL`: modelo sugerido: `gpt-4o-mini`.
- `SHEET_ID`: ID de tu Google Sheet de leads.
- `SHEET_TAB`: pestaña sugerida: `Leads`.

## Paso 3 — Configurar Meta WhatsApp Business

El comprador debe usar sus propias credenciales de Meta. Este paquete no incluye tokens ni acceso a una cuenta Meta interna.

En Meta Developers:

1. Crea o entra a una App conectada a WhatsApp.
2. Agrega el producto WhatsApp.
3. Conecta tu WhatsApp Business Account.
4. Copia el `Phone Number ID`.
5. Genera un access token vigente.
6. Crea una URL pública del webhook desde n8n.
7. En la configuración de Webhooks de WhatsApp, pega:
   - Callback URL: URL pública del webhook de n8n.
   - Verify token: el mismo valor que pusiste en `META_VERIFY_TOKEN`.
8. Suscribe el webhook al evento `messages`.
9. Envía un mensaje de prueba al número.

Importante: los tokens temporales de Meta expiran. Para producción, usa un token permanente o un sistema de refresh según tu configuración de Meta Business.

## Paso 4 — Adaptar la FAQ del negocio

Abre el nodo `Structured FAQ / Knowledge Base` dentro de n8n y reemplaza la información de ejemplo con datos reales:

- Qué vendes.
- Horarios.
- Ciudad o zona de atención.
- Precios o rangos.
- Políticas básicas.
- Preguntas frecuentes.
- Qué debe hacer el agente cuando no sepa una respuesta.

Usa `03-plantilla-faq-base-conocimiento.md` para preparar ese contenido antes de pegarlo en n8n.

## Paso 5 — Configurar registro de leads

Opción recomendada: Google Sheets.

1. Crea una hoja llamada `Leads`.
2. Copia los encabezados de `../whatsapp-agent-n8n/lead-log-template.csv`.
3. Conecta credenciales de Google Sheets en n8n.
4. Pega el `SHEET_ID` en tus variables.
5. Haz una prueba y confirma que aparece una fila nueva.

Opción rápida: CSV local.

Si todavía no tienes Google Sheets, usa `lead-log-template.csv` para registrar manualmente los leads mientras pruebas. No es ideal para producción, pero sirve para validar el flujo.

## Paso 6 — Probar antes de activar

Prueba mínima:

1. En n8n, usa el Test URL del webhook.
2. Envía `sample-meta-webhook-payload.json` al webhook.
3. Confirma que el workflow procesa el mensaje.
4. Confirma que la respuesta del agente se genera.
5. Confirma que el lead se guarda en Sheets o que sabes dónde registrarlo manualmente.
6. Recién después prueba envío/recepción real desde WhatsApp.

## Paso 7 — Activar

Activa el workflow solo cuando:

- Meta webhook responde correctamente.
- El token de Meta está vigente.
- OpenAI responde sin error.
- Google Sheets guarda filas.
- Las reglas de handoff humano están claras.
- El dueño sabe cuándo intervenir.

## Nota sobre nuestro demo dogfood

PYMEs con IA usa el mismo principio como demo: YouTube educa, WhatsApp demuestra el agente y el checkout entrega el paquete de $100.

Nuestro demo público se activa después de refrescar el token Meta de PYMEs. Hasta ese refresh, no se debe prometer respuesta live desde nuestro número. El paquete sí se puede importar, editar y probar localmente con payloads de ejemplo.
