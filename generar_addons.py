import os
import hashlib

# --- CONFIGURACIÓN ---
# Carpeta donde están los addons
ADDONS_DIR = "addons"

# --- FUNCIONES ---
def calcular_md5(ruta_archivo):
    """Devuelve el hash MD5 de un archivo."""
    with open(ruta_archivo, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

def generar_addons_xml():
    """Genera el archivo addons.xml y su checksum addons.xml.md5."""
    addons = []

    # Recorremos cada carpeta dentro de 'addons/'
    for carpeta in os.listdir(ADDONS_DIR):
        ruta_addon = os.path.join(ADDONS_DIR, carpeta, "addon.xml")
        if os.path.isfile(ruta_addon):
            with open(ruta_addon, "r", encoding="utf-8") as f:
                contenido = f.read().strip()
                addons.append(contenido)
                print(f"✅ Añadido: {carpeta}")

    # Creamos addons.xml
    contenido_final = '<?xml version="1.0" encoding="UTF-8"?>\n<addons>\n' + "\n".join(addons) + '\n</addons>'
    with open("addons.xml", "w", encoding="utf-8") as f:
        f.write(contenido_final)
    print("📄 Archivo 'addons.xml' generado.")

    # Creamos addons.xml.md5
    md5_hash = calcular_md5("addons.xml")
    with open("addons.xml.md5", "w") as f:
        f.write(md5_hash)
    print("🔐 Archivo 'addons.xml.md5' generado con el hash:", md5_hash)

# --- EJECUCIÓN ---
if __name__ == "__main__":
    generar_addons_xml()
