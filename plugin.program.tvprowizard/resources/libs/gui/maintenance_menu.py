################################################################################
#      Copyright (C) 2019 drinfernoo                                           #
#                                                                              #
#  This Program is free software; you can redistribute it and/or modify        #
#  it under the terms of the GNU General Public License as published by        #
#  the Free Software Foundation; either version 2, or (at your option)         #
#  any later version.                                                          #
#                                                                              #
#  This Program is distributed in the hope that it will be useful,             #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of              #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the                #
#  GNU General Public License for more details.                                #
#                                                                              #
#  You should have received a copy of the GNU General Public License           #
#  along with XBMC; see the file COPYING.  If not, write to                    #
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.       #
#  http://www.gnu.org/copyleft/gpl.html                                        #
################################################################################

import xbmc

import os

from resources.libs.common import directory
from resources.libs.common import logging
from resources.libs.common import tools
from resources.libs.common.config import CONFIG


class MaintenanceMenu:

    def get_listing(self):
        directory.add_dir('Herramientas de Limpieza', {'mode': 'maint', 'name': 'clean'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME1)
        directory.add_dir('Herramientas de Addons', {'mode': 'maint', 'name': 'addon'}, icon=CONFIG.ICONADDONS, themeit=CONFIG.THEME1)
        directory.add_dir('Herramientas de Log', {'mode': 'maint', 'name': 'logging'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME1)
        directory.add_dir('Mantenimiento General', {'mode': 'maint', 'name': 'misc'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME1)
        directory.add_dir('Backup y Restauración', {'mode': 'maint', 'name': 'backup'}, icon=CONFIG.ICONSAVE, themeit=CONFIG.THEME1)
        directory.add_dir('Ajustes y Arreglos del Sistema', {'mode': 'maint', 'name': 'tweaks'}, icon=CONFIG.ICONSETTINGS, themeit=CONFIG.THEME1)

    def clean_menu(self):
        from resources.libs import clear
        from resources.libs.common import tools

        on = '[B][COLOR springgreen]Activado[/COLOR][/B]'
        off = '[B][COLOR blue]Desactivado[/COLOR][/B]'

        autoclean = 'true' if CONFIG.AUTOCLEANUP == 'true' else 'false'
        cache = 'true' if CONFIG.AUTOCACHE == 'true' else 'false'
        packages = 'true' if CONFIG.AUTOPACKAGES == 'true' else 'false'
        thumbs = 'true' if CONFIG.AUTOTHUMBS == 'true' else 'false'
        includevid = 'true' if CONFIG.INCLUDEVIDEO == 'true' else 'false'
        includeall = 'true' if CONFIG.INCLUDEALL == 'true' else 'false'

        sizepack = tools.get_size(CONFIG.PACKAGES)
        sizethumb = tools.get_size(CONFIG.THUMBNAILS)
        archive = tools.get_size(CONFIG.ARCHIVE_CACHE)
        sizecache = (clear.get_cache_size()) - archive
        totalsize = sizepack + sizethumb + sizecache

        directory.add_file(
            '[B]Limpieza Total del Sistema[/B]: [COLOR springgreen]{0}[/COLOR]'.format(tools.convert_size(totalsize)), {'mode': 'fullclean'},
            icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_file('[B]Borrar Caché[/B]: [COLOR springgreen]{0}[/COLOR]'.format(tools.convert_size(sizecache)),
                           {'mode': 'clearcache'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        if xbmc.getCondVisibility('System.HasAddon(script.module.urlresolver)') or xbmc.getCondVisibility(
                'System.HasAddon(script.module.resolveurl)'):
            directory.add_file('[B]Borrar Caché de Resolvers[/B]', {'mode': 'clearfunctioncache'}, icon=CONFIG.ICONMAINT,
                               themeit=CONFIG.THEME3)
        directory.add_file('[B]Borrar Paquetes[/B]: [COLOR springgreen]{0}[/COLOR]'.format(tools.convert_size(sizepack)),
                           {'mode': 'clearpackages'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_file(
            '[B]Borrar Thumbnails[/B]: [COLOR springgreen]{0}[/COLOR]'.format(tools.convert_size(sizethumb)),
            {'mode': 'clearthumb'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        if os.path.exists(CONFIG.ARCHIVE_CACHE):
            directory.add_file('[B]Borrar Caché de Archivos[/B]: [COLOR springgreen]{0}[/COLOR]'.format(
                tools.convert_size(archive)), {'mode': 'cleararchive'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_file('[B]Borrar Thumbnails Antiguos[/B]', {'mode': 'oldThumbs'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_file('[B]Borrar Logs de Cierres Inesperados[/B]', {'mode': 'clearcrash'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_file('[B]Purgar Bases de Datos[/B]', {'mode': 'purgedb'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_file('[B]Restaurar Kodi de Fábrica[/B]', {'mode': 'freshstart'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        directory.add_separator('Limpieza Automática', icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME1)
        directory.add_file('Limpieza Automática al Iniciar: {0}'.format(autoclean.replace('true', on).replace('false', off)),
                           {'mode': 'togglesetting', 'name': 'autoclean'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        if autoclean == 'true':
            directory.add_file(
                '--- Frecuencia de Limpieza: [B][COLOR springgreen]{0}[/COLOR][/B]'.format(
                    CONFIG.CLEANFREQ[CONFIG.AUTOFREQ]),
                {'mode': 'changefreq'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
            directory.add_file(
                '--- Borrar Caché al Iniciar: {0}'.format(cache.replace('true', on).replace('false', off)),
                {'mode': 'togglesetting', 'name': 'clearcache'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
            directory.add_file(
                '--- Borrar Paquetes al Iniciar: {0}'.format(packages.replace('true', on).replace('false', off)),
                {'mode': 'togglesetting', 'name': 'clearpackages'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
            directory.add_file(
                '--- Borrar Thumbnails Antiguos al Iniciar: {0}'.format(thumbs.replace('true', on).replace('false', off)),
                {'mode': 'togglesetting', 'name': 'clearthumbs'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_separator('Caché de Video Addons', icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME1)
        directory.add_file(
            'Incluir Caché de Video en la Limpieza: {0}'.format(includevid.replace('true', on).replace('false', off)),
            {'mode': 'togglecache', 'name': 'includevideo'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        if includeall == 'true':
            includegaia = 'true'
            includeexodusredux = 'true'
            includethecrew = 'true'
            includeyoda = 'true'
            includevenom = 'true'
            includenumbers = 'true'
            includescrubs = 'true'
            includeseren = 'true'
        else:
            includeexodusredux = 'true' if CONFIG.INCLUDEEXODUSREDUX == 'true' else 'false'
            includegaia = 'true' if CONFIG.INCLUDEGAIA == 'true' else 'false'
            includethecrew = 'true' if CONFIG.INCLUDETHECREW == 'true' else 'false'
            includeyoda = 'true' if CONFIG.INCLUDEYODA == 'true' else 'false'
            includevenom = 'true' if CONFIG.INCLUDEVENOM == 'true' else 'false'
            includenumbers = 'true' if CONFIG.INCLUDENUMBERS == 'true' else 'false'
            includescrubs = 'true' if CONFIG.INCLUDESCRUBS == 'true' else 'false'
            includeseren = 'true' if CONFIG.INCLUDESEREN == 'true' else 'false'

        if includevid == 'true':
            directory.add_file(
                '--- Incluir [B]TODOS[/B] los Addons de Video: {0}'.format(includeall.replace('true', on).replace('false', off)),
                {'mode': 'togglecache', 'name': 'includeall'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
            if xbmc.getCondVisibility('System.HasAddon(plugin.video.exodusredux)'):
                directory.add_file(
                    '--- Incluir Exodus Redux: {0}'.format(
                        includeexodusredux.replace('true', on).replace('false', off)),
                    {'mode': 'togglecache', 'name': 'includeexodusredux'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
            if xbmc.getCondVisibility('System.HasAddon(plugin.video.gaia)'):
                directory.add_file(
                    '--- Incluir Gaia: {0}'.format(includegaia.replace('true', on).replace('false', off)),
                    {'mode': 'togglecache', 'name': 'includegaia'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
            if xbmc.getCondVisibility('System.HasAddon(plugin.video.numbersbynumbers)'):
                directory.add_file(
                    '--- Incluir NuMb3r5: {0}'.format(includenumbers.replace('true', on).replace('false', off)),
                    {'mode': 'togglecache', 'name': 'includenumbers'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
            if xbmc.getCondVisibility('System.HasAddon(plugin.video.scrubsv2)'):
                directory.add_file(
                    '--- Incluir Scrubs v2: {0}'.format(includescrubs.replace('true', on).replace('false', off)),
                    {'mode': 'togglecache', 'name': 'includescrubs'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
            if xbmc.getCondVisibility('System.HasAddon(plugin.video.seren)'):
                directory.add_file(
                    '--- Incluir Seren: {0}'.format(includeseren.replace('true', on).replace('false', off)),
                    {'mode': 'togglecache', 'name': 'includeseren'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
            if xbmc.getCondVisibility('System.HasAddon(plugin.video.thecrew)'):
                directory.add_file(
                    '--- Incluir THE CREW: {0}'.format(includethecrew.replace('true', on).replace('false', off)),
                    {'mode': 'togglecache', 'name': 'includethecrew'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
            if xbmc.getCondVisibility('System.HasAddon(plugin.video.venom)'):
                directory.add_file(
                    '--- Incluir Venom: {0}'.format(includevenom.replace('true', on).replace('false', off)),
                    {'mode': 'togglecache', 'name': 'includevenom'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
            if xbmc.getCondVisibility('System.HasAddon(plugin.video.yoda)'):
                directory.add_file(
                    '--- Incluir Yoda: {0}'.format(includeyoda.replace('true', on).replace('false', off)),
                    {'mode': 'togglecache', 'name': 'includeyoda'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
            directory.add_file('--- [B]Activar Todos[/B] los Addons de Video', {'mode': 'togglecache', 'name': 'true'}, icon=CONFIG.ICONMAINT,
                               themeit=CONFIG.THEME3)
            directory.add_file('--- [B]Desactivar Todos[/B] los Addons de Video', {'mode': 'togglecache', 'name': 'false'}, icon=CONFIG.ICONMAINT,
                               themeit=CONFIG.THEME3)

    def addon_menu(self):
        directory.add_file('[B]Desinstalar Addons[/B]', {'mode': 'removeaddons'}, icon=CONFIG.ICONADDONS, themeit=CONFIG.THEME3)
        directory.add_dir('[B]Eliminar Datos de Addons[/B]', {'mode': 'removeaddondata'}, icon=CONFIG.ICONADDONS, themeit=CONFIG.THEME3)
        directory.add_dir('[B]Activar/Desactivar Addons[/B]', {'mode': 'enableaddons'}, icon=CONFIG.ICONADDONS, themeit=CONFIG.THEME3)
        directory.add_file('[B]Forzar Actualización de Repositorios[/B]', {'mode': 'forceupdate'}, icon=CONFIG.ICONADDONS, themeit=CONFIG.THEME3)
        directory.add_file('[B]Forzar Actualización de Addons[/B]', {'mode': 'forceupdateaddons', 'action': 'auto'}, icon=CONFIG.ICONADDONS, themeit=CONFIG.THEME3)
   
    def logging_menu(self):
        errors = int(logging.error_checking(count=True))
        errorsfound = '[COLOR blue]{0} Error(es) Encontrado(s)[/COLOR]'.format(errors) if errors > 0 else '[COLOR springgreen]No se encontraron errores[/COLOR]'
        wizlogsize = '[COLOR blue]No Encontrado[/COLOR]' if not os.path.exists(
            CONFIG.WIZLOG) else "[COLOR springgreen]{0}[/COLOR]".format(
            tools.convert_size(os.path.getsize(CONFIG.WIZLOG)))
            
        directory.add_file('[B]Activar/Desactivar Log de Depuración[/B]', {'mode': 'enabledebug'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_file('[B]Subir Archivo de Log[/B]', {'mode': 'uploadlog'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_file('Ver Errores del Log: {0}'.format(errorsfound), {'mode': 'viewerrorlog'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        if errors > 0:
            directory.add_file('[B]Ver Último Error del Log[/B]', {'mode': 'viewerrorlast'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_file('[B]Ver Archivo de Log de Kodi[/B]', {'mode': 'viewlog'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_file('[B]Ver Archivo de Log del Wizard[/B]', {'mode': 'viewwizlog'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_file('[B]Borrar Log del Wizard[/B] (Tamaño: {0})'.format(wizlogsize), {'mode': 'clearwizlog'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
   
    def misc_menu(self):
        directory.add_file('[B]Reparar Kodi 17[/B]', {'mode': 'kodi17fix'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_dir('[B]Herramientas de Red[/B]', {'mode': 'nettools'}, icon=CONFIG.ICONSPEED, themeit=CONFIG.THEME3)
        directory.add_file('[B]Activar Fuentes Desconocidas[/B]', {'mode': 'unknownsources'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_file('[B]Activar/Desactivar Actualizaciones de Addons[/B]', {'mode': 'toggleupdates'}, icon=CONFIG.ICONSETTINGS, themeit=CONFIG.THEME3)
        directory.add_file('[B]Recargar Skin[/B]', {'mode': 'forceskin'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_file('[B]Recargar Perfil[/B]', {'mode': 'forceprofile'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_file('[B]Forzar Cierre de Kodi[/B]', {'mode': 'forceclose'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

    def backup_menu(self):
        directory.add_file('Limpiar Carpeta de Backups', {'mode': 'clearbackup'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_file('Ubicación de Backup: [COLOR {0}]{1}[/COLOR]'.format(CONFIG.COLOR2, CONFIG.MYBUILDS), {'mode': 'settings', 'name': 'Maintenance'}, icon=CONFIG.ICONSETTINGS, themeit=CONFIG.THEME3)
        directory.add_separator('Crear Backup', icon=CONFIG.ICONSAVE)
        directory.add_file('[B]Backup de la Build Completa[/B]', {'mode': 'backup', 'action': 'build'}, icon=CONFIG.ICONSAVE, themeit=CONFIG.THEME3)
        directory.add_file('[B]Backup del GuiFix[/B]', {'mode': 'backup', 'action': 'gui'}, icon=CONFIG.ICONSAVE, themeit=CONFIG.THEME3)
        directory.add_file('[B]Backup del Tema[/B]', {'mode': 'backup', 'action': 'theme'}, icon=CONFIG.ICONSAVE, themeit=CONFIG.THEME3)
        directory.add_file('[B]Backup de un Pack de Addons[/B]', {'mode': 'backup', 'action': 'addonpack'}, icon=CONFIG.ICONSAVE, themeit=CONFIG.THEME3)
        directory.add_file('[B]Backup de Addon Data[/B]', {'mode': 'backup', 'action': 'addondata'}, icon=CONFIG.ICONSAVE, themeit=CONFIG.THEME3)
        directory.add_separator('Restaurar Backup Local', icon=CONFIG.ICONSAVE)
        directory.add_file('[B]Restaurar Build Local[/B]', {'mode': 'restore', 'action': 'build'}, icon=CONFIG.ICONSAVE, themeit=CONFIG.THEME3)
        directory.add_file('[B]Restaurar GuiFix Local[/B]', {'mode': 'restore', 'action': 'gui'}, icon=CONFIG.ICONSAVE, themeit=CONFIG.THEME3)
        directory.add_file('[B]Restaurar Tema Local[/B]', {'mode': 'restore', 'action': 'theme'}, icon=CONFIG.ICONSAVE, themeit=CONFIG.THEME3)
        directory.add_file('[B]Restaurar Pack de Addons Local[/B]', {'mode': 'restore', 'action': 'addonpack'}, icon=CONFIG.ICONSAVE, themeit=CONFIG.THEME3)
        directory.add_file('[B]Restaurar Addon Data Local[/B]', {'mode': 'restore', 'action': 'addondata'}, icon=CONFIG.ICONSAVE, themeit=CONFIG.THEME3)
        directory.add_separator('Restaurar Backup Externo (URL)', icon=CONFIG.ICONSAVE)
        directory.add_file('[B]Restaurar Build Externa[/B]', {'mode': 'restore', 'action': 'build', 'name': 'external'}, icon=CONFIG.ICONSAVE, themeit=CONFIG.THEME3)
        directory.add_file('[B]Restaurar GuiFix Externo[/B]', {'mode': 'restore', 'action': 'gui', 'name': 'external'}, icon=CONFIG.ICONSAVE, themeit=CONFIG.THEME3)
        directory.add_file('[B]Restaurar Tema Externo[/B]', {'mode': 'restore', 'action': 'theme', 'name': 'external'}, icon=CONFIG.ICONSAVE, themeit=CONFIG.THEME3)
        directory.add_file('[B]Restaurar Pack de Addons Externo[/B]', {'mode': 'restore', 'action': 'addonpack', 'name': 'external'}, icon=CONFIG.ICONSAVE, themeit=CONFIG.THEME3)
        directory.add_file('[B]Restaurar Addon Data Externo[/B]', {'mode': 'restore', 'action': 'addondata', 'name': 'external'}, icon=CONFIG.ICONSAVE, themeit=CONFIG.THEME3)

    def tweaks_menu(self):
        directory.add_dir('[B]Configuración Avanzada (Buffer)[/B]', {'mode': 'advanced_settings'}, icon=CONFIG.ICONSETTINGS, themeit=CONFIG.THEME3)
        directory.add_file('[B]Escanear Fuentes en Busca de Enlaces Rotos[/B]', {'mode': 'checksources'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_file('[B]Buscar Repositorios Rotos[/B]', {'mode': 'checkrepos'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_dir('[B]Información del Sistema[/B]', {'mode': 'systeminfo'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)


#########################################################
#         PARTE DE ESTE CÓDIGO FUE TOMADO DE CHIKIRY    #
#                A QUIEN DAMOS LAS GRACIAS              #
#########################################################