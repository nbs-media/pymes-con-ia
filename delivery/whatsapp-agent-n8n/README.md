# PYMEs con IA — Workflow n8n: Agente de WhatsApp para leads

Paquete MVP para vender/importar un agente de respuesta por WhatsApp Cloud API en n8n.

## Archivos

- `pymes-whatsapp-lead-response-agent.workflow.json` — workflow importable en n8n.
- `.env.example` — variables requeridas. No contiene secretos reales.
- `lead-log-template.csv` — encabezados para el registro de leads si no se usa Google Sheets todavía.
- `sample-meta-webhook-payload.json` — payload local para probar el webhook sin token real de Meta.

## Qué hace el workflow

1. Recibe mensajes entrantes desde Meta WhatsApp Cloud API en `POST /webhook/pymesconia/whatsapp-agent/inbound`.
2. Responde 200 rápido a Meta para evitar retries.
3. Normaliza el payload y procesa solo mensajes de texto.
4. Busca coincidencias en una FAQ estructurada editable dentro del nodo `Structured FAQ / Knowledge Base`.
5. Construye un prompt de ventas/atención para una PYME en español.
6. Pide al LLM una respuesta JSON estricta con respuesta, etapa del lead, necesidad, urgencia y reglas de traspaso humano.
7. Guarda el lead en Google Sheets.
8. Envía la respuesta al cliente por WhatsApp Cloud API.
9. Si el lead requiere humano, avisa al dueño por WhatsApp.
10. Incluye Error Trigger para avisar al dueño si el workflow falla.

## Variables requeridas

Configurar en n8n como variables de entorno, o reemplazar las expresiones `$env.*` después de importar:

- `BUSINESS_NAME` — nombre del negocio comprador.
- `OWNER_WHATSAPP` — teléfono WhatsApp del dueño/equipo, formato internacional sin `+`.
- `META_PHONE_NUMBER_ID` — phone number ID de Meta WhatsApp Cloud API.
- `META_ACCESS_TOKEN` — token vigente de Meta. En PYMEs está pendiente refrescarlo; no se requiere para importar.
- `META_VERIFY_TOKEN` — token de verificación si se crea el workflow GET de verificación Meta.
- `OPENAI_API_KEY` — API key del proveedor LLM compatible con OpenAI.
- `OPENAI_MODEL` — default sugerido: `gpt-4o-mini`.
- `OPENAI_BASE_URL` — default: `https://api.openai.com/v1/chat/completions`.
- `SHEET_ID` — Google Sheet donde se registran leads.
- `SHEET_TAB` — pestaña, default `Leads`.

## Credenciales que debe conectar el comprador

- Google Sheets OAuth2 en el nodo `Append Lead to Google Sheets`.
- Variables/credenciales de Meta y OpenAI. El template usa headers con `$env.*` para evitar secretos hardcoded.

## Importación en n8n

1. n8n → Workflows → Import from File.
2. Subir `pymes-whatsapp-lead-response-agent.workflow.json`.
3. Abrir el nodo `Structured FAQ / Knowledge Base` y reemplazar horario, dirección, precios/políticas reales y reglas de agenda.
4. Conectar credencial de Google Sheets.
5. Crear una hoja con los encabezados de `lead-log-template.csv`.
6. Configurar env vars.
7. Probar con `sample-meta-webhook-payload.json` usando el Webhook Test URL.
8. Activar solo después de conectar Meta y probar envío/recepción con token vigente.

## Reglas de escalamiento humano

El agente marca handoff si el cliente pide hablar con una persona; hay urgencia, queja, reclamo, devolución/cancelación; el modelo no puede interpretar una respuesta segura; o la conversación necesita precio final, negociación, disponibilidad real o decisión humana.

## Nota sobre Meta

Este paquete no exige token Meta vivo para importarse. La verificación real de envío/recepción se debe hacer cuando Dr E refresque el token Meta.

## Validación KIRA

- Validación local: `./validate_workflow.py` devuelve `VALID`, 17 nodos, 12 fuentes de conexión y placeholders requeridos presentes.
- JSON parseado con `python3 -m json.tool` sin errores.
- Import n8n API probado contra PGFormula n8n: workflow de prueba creado inactivo con ID `xt4vC2fSJ3ot4by0`, 17 nodos recuperados por API. El borrado por API devolvió `403 Forbidden`, así que queda como workflow inactivo de validación para limpieza manual/admin.
- No se hizo prueba live de Meta send/receive porque el token Meta está expirado y esa verificación está diferida.
