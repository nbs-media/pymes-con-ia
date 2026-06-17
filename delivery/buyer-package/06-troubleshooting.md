# Troubleshooting

Problemas comunes al instalar el agente de WhatsApp en n8n.

## Meta no verifica el webhook

Síntomas:

- Meta dice que el callback no responde.
- Meta dice que el verify token no coincide.
- El webhook nunca queda suscrito.

Revisa:

1. La URL pública de n8n debe ser accesible desde internet.
2. El webhook debe responder a la verificación de Meta.
3. El valor de `META_VERIFY_TOKEN` debe ser exactamente el mismo en Meta y n8n.
4. No debe haber espacios extra antes o después del token.
5. Si usas n8n local, necesitas túnel público o despliegue con HTTPS.

## El workflow no recibe mensajes

Revisa:

- El workflow está activo, no solo en modo test.
- El webhook de Meta está suscrito al evento `messages`.
- El número de WhatsApp correcto está conectado al `META_PHONE_NUMBER_ID`.
- El mensaje entra al número conectado a Meta, no a otro WhatsApp.
- Meta muestra eventos enviados en el panel de Webhooks.

## El agente no responde por WhatsApp

Revisa:

- `META_ACCESS_TOKEN` está vigente.
- `META_PHONE_NUMBER_ID` es correcto.
- La llamada HTTP a Meta no devuelve 401, 403 o 400.
- El teléfono del cliente está en formato correcto.
- La ventana de conversación de WhatsApp permite responder, o estás usando plantilla aprobada si aplica.

## Error 401 o 403 en Meta

Causas comunes:

- Token expirado.
- Token sin permisos suficientes.
- App de Meta mal configurada.
- WhatsApp Business Account no conectado al número.
- Estás usando un `Phone Number ID` que no corresponde al token.

Solución:

Genera un token vigente desde Meta Business / Developers y vuelve a probar.

## OpenAI no responde

Revisa:

- `OPENAI_API_KEY` está configurada.
- `OPENAI_BASE_URL` apunta al endpoint correcto.
- `OPENAI_MODEL` existe para tu proveedor.
- Hay saldo o facturación activa.
- La respuesta del modelo cumple JSON estricto.

Si el modelo devuelve texto no válido, baja la creatividad del modelo y refuerza el prompt para responder solo JSON.

## Google Sheets no guarda leads

Revisa:

- La credencial de Google Sheets está conectada en n8n.
- `SHEET_ID` es correcto.
- `SHEET_TAB` existe y se llama igual.
- La primera fila tiene los encabezados esperados.
- La cuenta conectada tiene permiso de edición.

Fallback:

Usa `lead-log-template.csv` para registrar leads manualmente mientras arreglas Sheets.

## El agente responde información incorrecta

Causa probable:

La FAQ/base de conocimiento está incompleta o demasiado vaga.

Solución:

1. Abre `03-plantilla-faq-base-conocimiento.md`.
2. Agrega la pregunta exacta que falló.
3. Escribe la respuesta correcta.
4. Define si debe pasar a humano.
5. Actualiza el nodo `Structured FAQ / Knowledge Base`.
6. Prueba de nuevo.

## El agente no pasa a humano cuando debería

Revisa:

- Las reglas de `05-reglas-handoff-escalamiento.md` están copiadas en el workflow.
- El prompt pide devolver `human_required`.
- El aviso al dueño usa `OWNER_WHATSAPP` correcto.
- La rama condicional del workflow detecta `human_required = true` o equivalente.

## Nuestro demo de PYMEs no responde live todavía

Esto es esperado si el token Meta de PYMEs está expirado.

El paquete se puede validar con payloads locales y pruebas de n8n. La demo pública de WhatsApp se activa después de refrescar el token Meta de PYMEs. Hasta entonces, no prometas respuesta live desde nuestro número.

## Checklist final de diagnóstico

Si algo falla, revisa en este orden:

1. ¿El mensaje llega al webhook?
2. ¿El workflow corre sin error?
3. ¿OpenAI genera respuesta?
4. ¿Sheets guarda el lead?
5. ¿Meta acepta el envío?
6. ¿El dueño recibe handoff si aplica?

No cambies cinco cosas a la vez. Corrige una, prueba, luego sigue.
