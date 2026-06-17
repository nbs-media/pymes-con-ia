# PYMEs con IA — paquete de entrega al comprador

Producto MVP: agente IA para WhatsApp en n8n.
Precio de lanzamiento: $100 USD.
Dominio: https://pymesconia.com
Checkout: https://buy.stripe.com/dRm3cub7nbGj0oq3BX2ZO01

## Qué recibe el comprador

1. Workflow importable de n8n:
   - `../whatsapp-agent-n8n/pymes-whatsapp-lead-response-agent.workflow.json`
2. Guía de configuración:
   - `01-guia-configuracion-comprador.md`
3. Checklist rápido:
   - `02-checklist-inicio-rapido.md`
4. Plantilla de FAQ / base de conocimiento:
   - `03-plantilla-faq-base-conocimiento.md`
5. Plantilla de registro de leads:
   - `04-plantilla-registro-leads.md`
   - `lead-log-template.csv`
6. Reglas de traspaso humano:
   - `05-reglas-handoff-escalamiento.md`
7. Troubleshooting:
   - `06-troubleshooting.md`
8. Materiales de adquisición YouTube -> WhatsApp:
   - `07-materiales-youtube-whatsapp.md`

## Resultado esperado

El comprador importa el workflow en n8n, conecta sus credenciales de Meta WhatsApp, OpenAI y Google Sheets, carga su FAQ básica, prueba el flujo con mensajes reales y activa un primer agente que:

- responde preguntas frecuentes por WhatsApp,
- clasifica la intención del prospecto,
- registra leads,
- dirige a compra/cita/siguiente paso,
- avisa al dueño cuando se necesita intervención humana.

## Nota crítica sobre credenciales Meta WhatsApp

El paquete no incluye credenciales Meta del comprador. Cada negocio debe tener o crear su propio WhatsApp Business Platform en Meta y generar:

- `META_PHONE_NUMBER_ID`,
- `META_ACCESS_TOKEN`,
- `META_VERIFY_TOKEN`,
- URL pública del webhook de n8n.

Nuestro demo de PYMEs con IA se activa como dogfood del mismo producto cuando el token Meta de PYMEs sea refrescado. Hasta ese refresh, el paquete se puede importar, editar y probar con payloads locales, pero no se debe prometer envío/recepción live desde nuestro número.

## Ruta recomendada de entrega

Enviar al comprador este folder completo más el workflow n8n:

- `delivery/buyer-package/`
- `delivery/whatsapp-agent-n8n/`

No enviar secretos, tokens, `.env` reales ni credenciales internas.
