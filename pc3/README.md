# <font color="#7F000E" size=5>3era Práctica Calificada</font>

<br>
<div style="text-align: right">
<font color="#7F000E" size=3>Curso: Desarrollo de Software</font><br>
<font color="#7F000E" size=3>Semestre: 2024-II</font><br>
<font color="#7F000E" size=3>Ciencias de la Computación - UNI</font><br>
</div>

<br>

<div style="display: flex; justify-content: space-between;">
    <div>
        <strong>Apellidos y Nombres:</strong> <span style="border-bottom: 1.5px dotted black;">Pacheco Taboada André Joaquín</span>
    </div>
    <div>
        <strong>Código:</strong> <span style="border-bottom: 1.5px dotted black;">20222189G</span>
    </div>
</div>

## Estrategia de Desarrollo

### Fase 1: Análisis Inicial y Estructura del Proyecto

Al analizar los requisitos de la práctica, noté que tanto la Parte 1 (Implementación RSA) como la Parte 2 (Sistema de cifrado de base de datos) comparten varios componentes y patrones de diseño similares. Por esta razón, decidí desarrollar ambas partes simultáneamente, aprovechando la reutilización de código y manteniendo una arquitectura coherente.

#### Estructura del Proyecto

He diseñado una estructura de directorios que soporta ambos ejercicios:
```bash
src/
├── core/
│   ├── __init__.py
│   └── interfaces/
│       ├── __init__.py
│       ├── crypto_generator.py     
│       ├── crypto_strategy.py       
│       ├── database.py              
│       └── key_manager.py          
│
├── crypto/
│   ├── __init__.py
│   ├── generators/
│   │   ├── __init__.py
│   │   └── rsa_generator.py       
│   └── strategies/
│       ├── __init__.py
│       ├── aes_strategy.py        
│       └── rsa_strategy.py        
│
├── database/
│   ├── __init__.py
│   ├── repositories/
│   │   ├── __init__.py
│   │   └── encrypted_data_repository.py
│   └── implementations/
│       ├── __init__.py
│       └── memory_database.py     
│
├── models/
│   ├── __init__.py
│   ├── encrypted_data.py
│   └── key_pair.py
│
├── services/
│   ├── __init__.py
│   ├── encryption_service.py      
│   └── key_management_service.py   
│
└── utils/
    ├── __init__.py
    └── exceptions.py               

tests/
├── __init__.py
├── integration/
│   ├── __init__.py
│   └── test_encryption_flow.py
│
├── unit/
│   ├── __init__.py
│   ├── crypto/
│   │   ├── test_aes_strategy.py
│   │   └── test_rsa_strategy.py
│   ├── database/
│   │   └── test_memory_database.py
│   └── services/
│       ├── test_encryption_service.py
│       └── test_key_management.py
│
└── conftest.py                     
```

Esta estructura fue diseñada considerando:

1. **Separación de Interfaces**: Para facilitar la implementación del Principio de Inversión de Dependencias (DIP).

2. **Organización Modular**: Cada componente (crypto, database, services) tiene su propio espacio y está organizado según su responsabilidad.

3. **Testing**: De momento solo se contemplan las pruebas unitarias, pero se ha dejado espacio para futuras pruebas de integración.

