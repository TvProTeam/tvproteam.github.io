import xbmcaddon
import os

#########################################################
#         Global Variables - DON'T EDIT!!!              #
#########################################################
ADDON_ID = xbmcaddon.Addon().getAddonInfo('id')
PATH = xbmcaddon.Addon().getAddonInfo('path')
ART = os.path.join(PATH, 'resources', 'media')
#########################################################

#########################################################
#        User Edit Variables                            #
#########################################################
ADDONTITLE = '[COLOR blue]TvProTeam Wizard[/COLOR]'
BUILDERNAME = 'TvPro'
EXCLUDES = [ADDON_ID, '']
# Text File with build info in it.
BUILDFILE = 'https://tvproteam.github.io/repo/wizard/build.txt'
# How often you would like it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK = 0
# Text File with apk info in it.  Leave as 'http://' to ignore
APKFILE = ''
# Text File with Youtube Videos urls.  Leave as 'http://' to ignore
YOUTUBETITLE = 'Youtube Video'
YOUTUBEFILE = 'http://'
# Text File for addon installer.  Leave as 'http://' to ignore
ADDONFILE = 'http://'
# Text File for advanced settings.  Leave as 'http://' to ignore
ADVANCEDFILE = 'http://'
#########################################################

#########################################################
#        Theming Menu Items                             #
#########################################################
ICONBUILDS = os.path.join(ART, 'builds.png')
ICONMAINT = os.path.join(ART, 'maintenance.png')
ICONSPEED = os.path.join(ART, 'speed.png')
ICONAPK = os.path.join(ART, 'apkinstaller.png')
ICONADDONS = os.path.join(ART, 'addoninstaller.png')
ICONYOUTUBE = os.path.join(ART, 'youtube.png')
ICONSAVE = os.path.join(ART, 'savedata.png')
ICONTRAKT = os.path.join(ART, 'keeptrakt.png')
ICONREAL = os.path.join(ART, 'keepdebrid.png')
ICONLOGIN = os.path.join(ART, 'keeplogin.png')
ICONCONTACT = os.path.join(ART, 'information.png')
ICONSETTINGS = os.path.join(ART, 'settings.png')
HIDESPACERS = 'No'
SPACER = '='

# uservar.py - New Lines
from resources.libs.common.colors import colors

COLOR1 = colors.color1
COLOR2 = colors.color2
COLOR3 = colors.color3
THEME1 = u'[COLOR {color3}][B]{{}}[/B][/COLOR]'.format(color3=COLOR3)
THEME2 = u'[COLOR {color1}][B]{{}}[/B][/COLOR]'.format(color1=COLOR1)
THEME3 = u'[COLOR {color1}]» {{}}[/COLOR]'.format(color1=COLOR1)
THEME4 = u'[COLOR {color1}]Build Actual: [/COLOR][COLOR {color3}][B]{{}}[/B][/COLOR]'.format(color1=COLOR1, color3=COLOR3)
THEME5 = u'[COLOR {color1}]Tema Actual: [/COLOR][COLOR {color3}][B]{{}}[/B][/COLOR]'.format(color1=COLOR1, color3=COLOR3)

HIDECONTACT = 'Yes'
CONTACT = 'Gracias TvProTeam.'
CONTACTICON = 'http://'
CONTACTFANART = 'http://_'
#########################################################

#########################################################
#        Auto Update For Those With No Repo             #
#########################################################
AUTOUPDATE = 'Yes'
#########################################################

#########################################################
#        Auto Install Repo If Not Installed             #
#########################################################
AUTOINSTALL = 'No'
REPOID = ''
REPOADDONXML = 'https://'
REPOZIPURL = 'https://'
#########################################################

#########################################################
#        Notification Window                            #
#########################################################
ENABLE = 'No'
NOTIFICATION = 'https://tvproteam.github.io/wizard/notificacion.txt'
HEADERTYPE = 'Text'
FONTHEADER = 'Font24'
HEADERMESSAGE = '[COLOR RED][B]LEE BIEN[/B][/COLOR]'
HEADERIMAGE = 'http://'
FONTSETTINGS = 'Font20'
BACKGROUND = 'https://tvproteam.github.io/wizard/tvpro.jpg'
#########################################################

#########################################################
#         PARTE DE ESTE CÓDIGO FUE TOMADO DE CHIKIRY    #
#                A QUIEN DAMOS LAS GRACIAS              #
#########################################################