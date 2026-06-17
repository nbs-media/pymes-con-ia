# PYMEs con IA — QA compra → entrega

Fecha: 2026-06-17
Dominio: https://pymesconia.com
Stripe checkout: https://buy.stripe.com/dRm3cub7nbGj0oq3BX2ZO01

## Resultado corto

PASS con una sola verificación diferida: envío/recepción live por WhatsApp usando Meta, porque el token actual está expirado.

El funnel crítico está listo para revisión:
YouTube → WhatsApp demo pendiente de token → checkout Stripe $100 → página de entrega → descarga ZIP del paquete.

## Evidencia

| Área | Estado | Evidencia |
|---|---:|---|
| Fuente canónica | PASS | Dashboard Notion `3816341467be80eabef4d444c67b0d50` leído vía `NOTION_PGF_API_KEY`; apunta a dominio, repo y checklist MVP. |
| Página principal | PASS | `https://pymesconia.com` devolvió 200; contiene PYMES con IA, CTA Stripe, YouTube → WhatsApp y nota de Meta pendiente. |
| Legal | PASS | `/privacidad` y `/terminos` devolvieron 200. |
| Checkout | PASS | Stripe payment link devolvió 200; API Stripe encontró `plink_1Tj7zGA81aFjWNd31Zqnm06T`, activo, $100 USD, producto “Agente IA para WhatsApp en n8n”. |
| Post-compra | PASS | Stripe `after_completion` redirige a `https://pymesconia.com/entrega?session_id={CHECKOUT_SESSION_ID}`. |
| Entrega | PASS | `/entrega` devolvió 200 y contiene link de descarga del paquete ZIP. |
| Descarga | PASS | `/descargas/pymes-con-ia-agente-whatsapp-n8n-v1.zip` devolvió 200 `application/zip`, 24,764 bytes, SHA256 `7bb6776e7023cd3adf982565a9b10d9f6b3595ab2a08a6eb090ab1bd6ff259a9`. |
| Buyer package | PASS | 9 archivos base presentes: guía, checklist, FAQ, lead log, handoff, troubleshooting, YouTube→WhatsApp y CSV. |
| n8n JSON local | PASS | `validate_workflow.py` devolvió `VALID`; 17 nodos, 12 fuentes de conexión, env vars requeridas presentes. |
| n8n import/API | PASS | PGFormula n8n `/healthz` 200; workflow de validación `xt4vC2fSJ3ot4by0` existe inactivo, no archivado, 17 nodos, 12 conexiones, nombres de nodos coinciden con el JSON local. |
| Links locales críticos | PASS | No faltan assets locales referenciados por `index.html`, `entrega.html`, `privacidad.html`, `terminos.html`. |
| WhatsApp live Meta | DEFERRED | Graph `/me` con token configurado devolvió OAuthException 190: sesión expirada. No bloquea venta/importación; bloquea demo live hasta refrescar token. |

## Fix aplicado durante QA

La página `/entrega` dependía de pedir el paquete por email. Eso era débil para “purchase-to-delivery”. Se corrigió agregando descarga directa del ZIP del paquete comprador:

- `descargas/pymes-con-ia-agente-whatsapp-n8n-v1.zip`
- Link visible en `/entrega`

## Veredicto

Listo para revisión de Dr E.

No hay blocker de compra/entrega. El único pendiente real es activar y probar el WhatsApp demo cuando Dr E refresque el token Meta.
