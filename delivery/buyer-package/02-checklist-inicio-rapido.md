# Checklist rápido de inicio

Usa esta lista para instalar y validar el agente sin perderte en detalles técnicos.

## Antes de importar

- [ ] Tengo acceso a n8n.
- [ ] Tengo acceso a Meta Business / WhatsApp Business Platform.
- [ ] Tengo un número de WhatsApp listo para usar con Meta.
- [ ] Tengo un token Meta vigente.
- [ ] Tengo una API key de OpenAI o proveedor compatible.
- [ ] Tengo una Google Sheet creada, o usaré CSV local al inicio.
- [ ] Tengo la información básica del negocio: horarios, ubicación, servicios, precios y reglas.

## Importación en n8n

- [ ] Importé `pymes-whatsapp-lead-response-agent.workflow.json`.
- [ ] Guardé el workflow.
- [ ] Dejé el workflow inactivo mientras configuro credenciales.
- [ ] Revisé el nodo `Structured FAQ / Knowledge Base`.
- [ ] Reemplacé la información de ejemplo con datos reales.

## Variables y credenciales

- [ ] Configuré `BUSINESS_NAME`.
- [ ] Configuré `OWNER_WHATSAPP`.
- [ ] Configuré `META_PHONE_NUMBER_ID`.
- [ ] Configuré `META_ACCESS_TOKEN`.
- [ ] Configuré `META_VERIFY_TOKEN`.
- [ ] Configuré `OPENAI_API_KEY`.
- [ ] Configuré `OPENAI_MODEL`.
- [ ] Configuré `SHEET_ID` y `SHEET_TAB`, si uso Google Sheets.
- [ ] Conecté credenciales de Google Sheets en n8n.

## Meta WhatsApp

- [ ] Copié el webhook público de n8n.
- [ ] Pegué el Callback URL en Meta.
- [ ] Pegué el Verify Token correcto en Meta.
- [ ] Suscribí el webhook al evento `messages`.
- [ ] Confirmé que Meta acepta la verificación.

## Prueba local

- [ ] Envié `sample-meta-webhook-payload.json` al Test URL del webhook.
- [ ] El workflow respondió sin errores.
- [ ] El agente generó una respuesta clara en español.
- [ ] El lead quedó guardado en Google Sheets o registrado en el CSV.
- [ ] El dueño recibe aviso cuando aplica handoff humano.

## Prueba live

- [ ] Envié un mensaje real al número de WhatsApp.
- [ ] El workflow recibió el mensaje.
- [ ] El agente respondió por WhatsApp.
- [ ] El lead quedó registrado.
- [ ] Probé un caso que requiere humano.
- [ ] Confirmé que la alerta llegó al dueño/equipo.

## Listo para activar

- [ ] El workflow está activo.
- [ ] Las respuestas no prometen cosas falsas.
- [ ] Los precios y horarios están correctos.
- [ ] Hay una persona responsable de revisar leads.
- [ ] Hay una rutina diaria para revisar Google Sheets o el CSV.

## Primeras 48 horas

Durante los primeros dos días, revisa cada conversación. No busques perfección automática. Busca esto:

- Preguntas que el agente no pudo responder.
- Respuestas demasiado largas o vagas.
- Leads buenos que necesitan seguimiento humano.
- Campos faltantes en el registro de leads.
- Errores por token, webhook o credenciales.

Ajusta la FAQ y las reglas de handoff después de ver conversaciones reales.
