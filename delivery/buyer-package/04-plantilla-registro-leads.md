# Plantilla de registro de leads

El agente necesita guardar cada conversación útil. La opción recomendada es Google Sheets. Si todavía no tienes Sheets conectado, usa el CSV local como respaldo temporal.

## Campos recomendados

Usa estos encabezados, iguales al workflow n8n:

```csv
timestamp,business_name,customer_phone,customer_name,inbound_message,response_text,lead_stage,lead_need,urgency,handoff_required,handoff_reason,message_id
```

Archivos incluidos:

- `lead-log-template.csv` — copia dentro del paquete comprador.
- `../whatsapp-agent-n8n/lead-log-template.csv` — copia junto al workflow n8n.

## Significado de cada campo

- `timestamp`: fecha y hora del mensaje.
- `business_name`: nombre del negocio.
- `customer_phone`: WhatsApp del lead.
- `customer_name`: nombre si el lead lo dio.
- `inbound_message`: mensaje recibido.
- `response_text`: respuesta enviada por el agente.
- `lead_stage`: etapa del lead, por ejemplo nuevo, interesado, listo_para_comprar, soporte, humano_requerido.
- `lead_need`: necesidad principal del lead.
- `urgency`: baja, media o alta.
- `handoff_required`: true/false o sí/no, según tu hoja.
- `handoff_reason`: razón del traspaso humano si aplica.
- `message_id`: ID del mensaje de WhatsApp/Meta para rastreo.

## Opción A — Google Sheets

1. Crea una Google Sheet.
2. Nombra la primera pestaña `Leads`.
3. En la fila 1, pega los encabezados del CSV.
4. Copia el ID de la hoja desde la URL.
5. En n8n, conecta credenciales de Google Sheets.
6. Configura:
   - `SHEET_ID`: ID de la hoja.
   - `SHEET_TAB`: `Leads`.
7. Envia un mensaje de prueba y confirma que se agrega una fila.

## Opción B — CSV local temporal

Si todavía no usas Google Sheets:

1. Abre `lead-log-template.csv`.
2. Agrega cada lead manualmente después de revisar la conversación.
3. Guarda una copia diaria.
4. Migra a Google Sheets cuando el flujo esté validado.

El CSV sirve para empezar, pero no es ideal si varias personas revisan leads o si quieres reportes.

## Rutina diaria recomendada

Cada día revisa:

- Leads nuevos.
- Leads con `human_required = sí`.
- Leads con urgencia alta.
- Conversaciones sin nombre o siguiente paso.
- Preguntas repetidas que deberían agregarse a la FAQ.

## Ejemplo de fila

```csv
2026-06-17T10:30:00Z,PYMEs Demo,5215551234567,Ana,"Quiero saber el precio","El paquete cuesta $100 USD e incluye workflow, prompts y guía",interesado,"Quiere saber costo y tiempos",media,false,,wamid.HBgN...
```

## Reglas de calidad

- No guardes contraseñas ni datos sensibles.
- No uses el registro como CRM completo al inicio.
- Mantén el resumen corto.
- Si el lead pide humano, revisa ese caso primero.
- Si una pregunta se repite tres veces, agrégala a la FAQ.
