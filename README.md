# TvPro
# Repositorio de Kodi TVPROTEAM
Repositorio personalizado para Kodi alojado en GitHub.

## Instalación

### Método 1: Instalar desde ZIP
1. Descarga el último release desde [Releases](https://github.com/tvpro/kodi-repository/releases)
2. En Kodi: Sistema → Add-ons → Instalar desde archivo ZIP
3. Selecciona el archivo `repository.tvproteam-9.0.zip`

### Método 2: Instalar desde URL
1. En Kodi: Sistema → Archivos → Agregar fuente
2. URL: `https://raw.githubusercontent.com/TvProTean/kodi-repository/main/repository/`
3. Nombre: "Mi Repo GitHub"
4. Ve a Instalar desde repositorio → Mi Repositorio GitHub

## Addons incluidos

- Plugin de Ejemplo: Un plugin de demostración
- Script de Ejemplo: Un script de demostración

## Desarrollo

Para agregar nuevos addons:

1. Coloca el addon en la carpeta `src/`
2. El script automáticamente lo incluirá en el repositorio
3. Los cambios se construyen automáticamente con GitHub Actions
