# AppMonedas
# 💱 CurrencySwap App – Microservicios con FastAPI + React Native (Expo)

Una aplicación básica de cambio de monedas con arquitectura de microservicios. Permite registrar usuarios, depositar fondos, cambiar divisas y hacer transferencias entre cuentas.

---

Docs de pruebas en postman y frontend:
[https://docs.google.com/document/d/1sLtyN1aeh2TNv6MxIIFEVNfF5DJ1JxrNqfUy5YDwZf4/edit?usp=sharing](https://docs.google.com/document/d/1sLtyN1aeh2TNv6MxIIFEVNfF5DJ1JxrNqfUy5YDwZf4/edit?usp=sharing)

frontend:
https://github.com/jordinnreyes/AppMonedasFrontend.git

## 🧱 Arquitectura General

```plaintext
 ┌──────────────┐       ┌──────────────┐       ┌──────────────┐
 │ UsuarioSvc   │──────▶│ CambistaSvc  │──────▶│ BancoSvc     │
 └──────────────┘       └──────────────┘       └──────────────┘
        ▲                                           ▲
        │                                           │
   React Native                               Base de Datos
       (Expo)                                      (PGSQL)


