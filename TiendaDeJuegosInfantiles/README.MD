# Tienda de Juegos Infantiles

Este proyecto es una aplicación web de una tienda de juegos infantiles desarrollada con Django. Implementa el patrón MVT (Modelo-Vista-Template) y está diseñada para gestionar usuarios, juegos y pedidos.

## Funcionalidades

1. **Página Principal**:
   - URL: `http://127.0.0.1:8000/`
   - Descripción: Página de bienvenida de la tienda de juegos.

2. **Crear Juego**:
   - URL: `http://127.0.0.1:8000/crear_juego/`
   - Descripción: Formulario para crear un nuevo juego con campos de nombre, edad recomendada y descripción.

3. **Buscar Juego**:
   - URL: `http://127.0.0.1:8000/buscar_juego/`
   - Descripción: Formulario para buscar juegos por nombre, ID o rango de edades.

4. **Crear Pedido**:
   - URL: `http://127.0.0.1:8000/pedir_juego/`
   - Descripción: Formulario para realizar un pedido de un juego específico.

5. **Registro Usuario**:
   - URL: `http://127.0.0.1:8000/registro_usuario/`
   - Descripción: Formulario para registrarse como ususario de la tienda.


## Orden de Prueba de Funcionalidades

1. **Página Principal**: Visitar la URL `http://127.0.0.1:8000/` para ver la página de bienvenida.
2. **Crear Juego**: Visitar la URL `http://127.0.0.1:8000/crear_juego/`, completar el formulario y enviar para crear un nuevo juego.
3. **Buscar Juego**: Visitar la URL `http://127.0.0.1:8000/buscar_juego/`, utilizar los campos de búsqueda y enviar para buscar juegos.
4. **Crear Pedido**: Visitar la URL `http://127.0.0.1:8000/pedir_juego/`, seleccionar un juego y completar el formulario de pedido.
5. **Registro Usuario**: Visitar la URL `http://127.0.0.1:8000/registro_usuario/`, registrate como usuario de la tienda.

## Ubicación de las Funcionalidades

- **Modelos**:
  - `models.py`: Contiene las definiciones de los modelos `Usuario`, `Juego` y `Pedido`.
- **Vistas**:
  - `views.py`: Contiene las vistas `index`, `crear_juego`, `buscar_juego`, `crear_pedido` y `registro_usuario`.
- **Formularios**:
  - `forms.py`: Contiene los formularios `UsuarioForm`, `JuegoForm` y `PedidoForm`.
- **Plantillas**:
  - `templates/base.html`: Plantilla base para la herencia.
  - `templates/index.html`: Plantilla para la página principal.
  - `templates/crear_juego.html`: Plantilla para el formulario de creación de juegos.
  - `templates/buscar_juego.html`: Plantilla para el formulario de búsqueda de juegos.
  - `templates/crear_pedido.html`: Plantilla para el formulario de pedido de juegos.
  - `templates/registro_usuario.html`: Plantilla para el formulario de registro de usuario.
