# Reglas de handoff y escalamiento humano

El agente debe resolver lo simple y pasar rápido a humano cuando hay riesgo, urgencia o intención fuerte de compra.

## Objetivo

Evitar dos errores:

1. Que el agente invente o prometa cosas que no sabe.
2. Que un lead listo para comprar se quede hablando con una automatización cuando necesita una persona.

## Estados recomendados

Usa estos estados en el workflow:

- `nuevo`: primer contacto o información insuficiente.
- `interesado`: el lead pregunta por servicio, precio, horarios o disponibilidad.
- `listo_para_comprar`: el lead pide comprar, pagar, reservar, agendar o avanzar.
- `soporte`: el contacto ya es cliente o tiene un problema.
- `humano_requerido`: el agente debe avisar al dueño/equipo.

## Cuándo responder automáticamente

El agente puede responder si:

- La pregunta está en la FAQ.
- La respuesta no requiere promesa específica.
- El cliente solo pide información general.
- El cliente está comparando opciones.
- El siguiente paso es claro: dejar datos, abrir checkout, pedir cita o esperar humano.

## Cuándo pasar a humano

Marcar `human_required = sí` si ocurre cualquiera de estos casos:

- El cliente pide hablar con una persona.
- El cliente quiere comprar o pagar ahora.
- El cliente pide precio final que depende de evaluación humana.
- El cliente solicita descuento, negociación o excepción.
- El cliente está molesto, reclama o amenaza con mala reseña.
- Hay cancelación, devolución o disputa.
- La pregunta tiene riesgo legal, médico, financiero o reputacional.
- El agente no tiene información suficiente.
- El mensaje es confuso después de una aclaración.
- El cliente comparte información sensible.
- Hay urgencia real.

## Mensaje al cliente cuando se pasa a humano

Usa una respuesta corta:

"Te entiendo. Para ayudarte bien y no darte información incorrecta, voy a pasar esto al equipo. Déjame tu nombre y el mejor horario para contactarte."

Si es intención de compra:

"Perfecto. Para avanzar, voy a pasar tus datos al equipo y te contactamos para confirmar el siguiente paso. ¿Me compartes tu nombre y el mejor horario?"

Si hay molestia:

"Lamento que hayas tenido esa experiencia. Lo correcto es que lo revise una persona del equipo. Ya lo marco como urgente para seguimiento."

## Aviso interno al dueño/equipo

El aviso debe incluir:

- Nombre si existe.
- Teléfono.
- Urgencia.
- Necesidad.
- Resumen de la conversación.
- Siguiente paso recomendado.

Plantilla:

"Lead requiere humano. Tel: {{phone}}. Nombre: {{name}}. Urgencia: {{urgency}}. Necesidad: {{need}}. Resumen: {{summary}}. Siguiente paso: {{next_step}}."

## Tiempos de respuesta recomendados

- Compra lista: responder en menos de 15 minutos.
- Reclamo o cliente molesto: responder en menos de 30 minutos.
- Pregunta normal: responder en el mismo día hábil.
- Lead incompleto: revisar una vez al día.

## Regla de oro

Si responder mal puede costar dinero, confianza o reputación, pasa a humano.
