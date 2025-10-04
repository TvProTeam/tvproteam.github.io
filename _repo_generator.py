import os
import zipfile
import hashlib

# --- CONFIGURACIÓN ---
ADDONS_DIR = "addons"   # Carpeta donde están los addons
OUTPUT_DIR = "addons"   # Donde se guardarán los ZIPs también

# --- FUNCIONES ---
def calcular_md5(ruta_archivo):
    """Calcula el hash MD5 de un archivo."""
    with open(ruta_archivo, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

def crear_zip(carpeta_addon):
    """Empaqueta un addon en un archivo ZIP con su versión."""
    ruta_addon_xml = os.path.join(ADDONS_DIR, carpeta_addon, "addon.xml")
    if not os.path.exists(ruta_addon_xml):
        print(f"⚠️  No se encontró addon.xml en {carpeta_addon}")
        return

    # Extraer la versión del addon.xml
    with open(ruta_addon_xml, "r", encoding="utf-8") as f:
        contenido = f.read()
    inicio = contenido.find('version="') + 9
    fin = contenido.find('"', inicio)
    version = contenido[inicio:fin] if inicio > 8 else "1.0.0"

    nombre_zip = f"{carpeta_addon}-{version}.zip"
    ruta_zip = os.path.join(OUTPUT_DIR, nombre_zip)

    with zipfile.ZipFile(ruta_zip, "w", zipfile.ZIP_DEFLATED) as zipf:
        for raiz, _, archivos in os.walk(os.path.join(ADDONS_DIR, carpeta_addon)):
            for archivo in archivos:
                ruta_completa = os.path.join(raiz, archivo)
                ruta_relativa = os.path.relpath(ruta_completa, ADDONS_DIR)
                zipf.write(ruta_completa, ruta_relativa)
    print(f"📦 Empaquetado: {nombre_zip}")

def generar_addons_xml():
    """Genera addons.xml y addons.xml.md5."""
    addons = []
    for carpeta in os.listdir(ADDONS_DIR):
        ruta_addon_xml = os.path.join(ADDONS_DIR, carpeta, "addon.xml")
        if os.path.isfile(ruta_addon_xml):
            with open(ruta_addon_xml, "r", encoding="utf-8") as f:
                addons.append(f.read().strip())
                print(f"✅ Detectado addon: {carpeta}")
                crear_zip(carpeta)

    contenido_final = '<?xml version="1.0" encoding="UTF-8"?>\n<addons>\n' + "\n".join(addons) + '\n</addons>'
    with open("addons.xml", "w", encoding="utf-8") as f:
        f.write(contenido_final)
    print("📄 addons.xml generado.")

    md5_hash = calcular_md5("addons.xml")
    with open("addons.xml.md5", "w") as f:
        f.write(md5_hash)
    print("🔐 addons.xml.md5 generado.")

# --- EJECUCIÓN ---
if __name__ == "__main__":
    generar_addons_xml()
    print("\n✅ Repositorio Kodi listo para subir al hosting.")
