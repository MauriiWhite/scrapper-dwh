# Scrapper Data Warehouse Project

## 📜 Descripción

**Scrapper** es un **Data Warehouse** diseñado para gestionar datos de productos de computación extraídos de una URL específica. Este proyecto utiliza un modelo dimensional con un esquema en estrella y ha sido implementado mediante ingeniería inversa para realizar web scraping de los datos de productos.

El proyecto incluye las siguientes tablas predeterminadas:

- **Product**: Información detallada sobre los productos.
- **Customer**: Datos de los clientes.
- **Branch**: Información sobre las sucursales.
- **Sales**: Tabla principal para el análisis de datos.

> [!NOTE]
> La extracción de datos de productos se ha realizado mediante técnicas de web scraping y un proceso de ingeniería inversa para adaptar la estructura de los datos a las necesidades del Data Warehouse.

## 📁 Estructura del Proyecto

El proyecto está organizado en las siguientes carpetas y archivos:

- **`data/`**: Carpeta que contiene varios archivos en diferentes formatos para fines demostrativos.
- **`requirements.txt`**: Archivo que lista las dependencias necesarias para el proyecto. Asegúrate de instalar estas dependencias antes de ejecutar el proyecto.
- **`scrapper/`**: Contiene el código principal para realizar el scraping de datos a partir de la URL especificada.

> [!WARNING]
> Debido a restricciones de propiedad intelectual, la URL para el scrapper no está disponible públicamente. Como resultado, el scrapper no puede ser ejecutado sin la URL válida.

- **`src/`**: Carpeta con los archivos de ejecución principal del proyecto. Incluye los scripts y módulos esenciales que forman el núcleo del sistema.
- **`test/`**: Carpeta destinada a las pruebas. Contiene scripts para transformar archivos y validar los datos en los formatos adecuados para pruebas.
- **`config.toml`**: Archivo de configuración utilizado para ajustar las peticiones HTTP del scrapper. Permite personalizar la conexión y la forma en que se envían las solicitudes.
- **`packages.ps1`**: Script de PowerShell para actualizar las dependencias del proyecto en sistemas **Windows**.

## 🛠️ Requisitos

Antes de comenzar con el proyecto, asegúrate de tener instalados los siguientes componentes:

- **Python**: Versión 3.10 o superior. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).
- **XAMPP**: Para crear y gestionar la base de datos. Descárgalo e instálalo desde [apachefriends.org](https://www.apachefriends.org/).

## 🚀 Instrucciones de Configuración

Sigue estos pasos para configurar el entorno de desarrollo y preparar el proyecto para su uso:

1. **Configura la Base de Datos**:
   - Abre XAMPP y inicia los servicios de **Apache** y **MySQL**.
   - Accede a **phpMyAdmin** desde tu navegador en `http://localhost/phpmyadmin/`.
   - Crea una nueva base de datos llamada **store**.

2. **Configura el Entorno de Python**:
   - **Crear un Entorno Virtual**:
     Se recomienda crear un entorno virtual para gestionar las dependencias del proyecto de manera aislada. Ejecuta el siguiente comando en tu terminal:

     ```bash
     python -m venv venv
     ```

   - **Activar el Entorno Virtual**:
     - En **Windows**:

       ```bash
       venv\Scripts\activate
       ```

     - En **macOS** o **Linux**:

       ```bash
       source venv/bin/activate
       ```

   - **Instalar las Dependencias**:
     Con el entorno virtual activado, instala las dependencias necesarias utilizando el archivo `requirements.txt`:

     ```bash
     pip install -r requirements.txt
     ```

   **Nota**: Asegúrate de tener `pip` actualizado para evitar problemas de instalación.

Siguiendo estos pasos, tendrás tu entorno de desarrollo configurado y listo para utilizar **Scrapper Data Warehouse**.

## 📝 Uso

Sigue estos pasos para ejecutar el scrapper y verificar que los datos se hayan gestionado correctamente:

1. **Configura la Base de Datos**:
   - Asegúrate de que la base de datos **store** esté correctamente configurada y en funcionamiento en XAMPP.

2. **Ejecuta el Scrapper**:
   - **En Windows**:

     Abre la terminal (cmd o PowerShell) y navega al directorio del proyecto. Ejecuta el siguiente comando para iniciar el scrapper:

     ```bash
     python src\main.py
     ```

   - **En macOS o Linux**:

     Abre la terminal y navega al directorio del proyecto. Ejecuta el siguiente comando para iniciar el scrapper:

     ```bash
     python3 src/main.py
     ```

3. **Verifica los Datos**:
   - Revisa los datos extraídos en la base de datos **store** para asegurarte de que el proceso se completó correctamente. Puedes usar **phpMyAdmin** para inspeccionar las tablas y validar la información.

Si encuentras algún problema durante la ejecución o en la verificación de los datos, revisa los mensajes de error en la terminal y asegúrate de que todas las configuraciones sean correctas.

## 😊 Agradecimientos

Gracias por usar **Scrapper Data Warehouse**. Espero que este proyecto te sea de utilidad.

> Atte. ***Maurii White***
