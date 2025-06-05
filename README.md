# AppMonedas
# 💱 CurrencySwap App – Microservicios con FastAPI + React Native (Expo)

Una aplicación básica de cambio de monedas con arquitectura de microservicios. Permite registrar usuarios, depositar fondos, cambiar divisas y hacer transferencias entre cuentas.

---

## 🧱 Arquitectura General

```plaintext
 ┌──────────────┐       ┌──────────────┐       ┌──────────────┐
 │ UsuarioSvc   │──────▶│ CambistaSvc  │──────▶│ BancoSvc     │
 └──────────────┘       └──────────────┘       └──────────────┘
        ▲                                           ▲
        │                                           │
   React Native                               Base de Datos
       (Expo)                                      (PGSQL)
