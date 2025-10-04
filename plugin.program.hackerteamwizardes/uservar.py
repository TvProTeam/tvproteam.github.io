import os, xbmc, xbmcaddon

#########################################################
### User Edit Variables #################################
#########################################################
ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = '[B][LOWERCASE][CAPITALIZE][COLOR blue]Wizard HackerTeam[/CAPITALIZE][/LOWERCASE][/B][/COLOR]'
EXCLUDES       = [ADDON_ID]
# Text File with build info in it.
BUILDFILE      = 'http://tvbox.uiwap.com/kodi/hacker.txt'
# How often you would list it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK    = 0
# Text File with apk info in it.
APKFILE        = 'http://tvbox.uiwap.com/kodi/apk.txt'
# Text File with Youtube Videos urls.  Leave as 'http://' to ignore
YOUTUBETITLE   = '[COLOR black]Videos Kodi[/COLOR]'
YOUTUBEFILE    = 'https://'
# Text File for addon installer.  Leave as 'http://' to ignore
ADDONFILE      = 'http://tvbox.uiwap.com/kodi/addons.txt'
# Text File for advanced settings.  Leave as 'http://' to ignore
ADVANCEDFILE   = 'http://tvbox.uiwap.com/kodi/advancedsettingslist.txt'
#########################################################

# Dont need to edit just here for icons stored locally
PATH           = xbmcaddon.Addon().getAddonInfo('path')
ART            = os.path.join(PATH, 'resources', 'art')

#########################################################
### THEMING MENU ITEMS ##################################
#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'http://aftermathwizard.net/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS     = 'http://tvbox.uiwap.com/kodi/icon/builds.png'
ICONMAINT      = 'http://tvbox.uiwap.com/kodi/icon/Maintenance.png'
ICONAPK        = 'http://tvbox.uiwap.com/kodi/icon/apkinstaller.png'
ICONADDONS     = 'http://tvbox.uiwap.com/kodi/icon/addoninstaller.png'
ICONYOUTUBE    = 'http://tvbox.uiwap.com/kodi/icon/youtube.png'
ICONSAVE       = 'http://tvbox.uiwap.com/kodi/icon/savedata.png'
ICONTRAKT      = 'http://'
ICONREAL       = 'http://'
ICONLOGIN      = 'http://'
ICONCONTACT    = 'http://tvbox.uiwap.com/kodi/icon/wizard.png'
ICONSETTINGS   = 'http://tvbox.uiwap.com/kodi/icon/settings.png'
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'No'
# Character used in seperator
SPACER         = '='

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'white'
COLOR2         = 'blue'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR1+'][B][I][COLOR '+COLOR2+']HackerTeam[/COLOR][/B][/COLOR] [COLOR '+COLOR2+']%s[/COLOR][/I]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR1+']Version Actual:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Current Theme Header / %s is the menu item and is required
THEME5         = '[COLOR '+COLOR1+']Tema Actual:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'No'
# You can add \n to do line breaks
CONTACT        = 'Gracias por elegir Wizard HackerTeam\r\n\r\nGracias al echipo HackerTeam.\r\n Gupo telegram:@kodihackerteam\r\n'
#Images used for the contact window.  http:// for default icon and fanart
CONTACTICON    = 'http://tvbox.uiwap.com/kodi/icon/wizard.png'
CONTACTFANART  = 'http://'
#########################################################

#########################################################
### AUTO UPDATE #########################################
########## FOR THOSE WITH NO REPO #######################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'Yes'
# Url to wizard version
WIZARDFILE     = 'http://tvbox.uiwap.com/kodi/hacker.txt'
#########################################################

#########################################################
### AUTO INSTALL ########################################
########## REPO IF NOT INSTALLED ########################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'No'
# Addon ID for the repository
REPOID         = ''
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = ''
# Url to folder zip is located in
REPOZIPURL     = ''
#########################################################

#########################################################
### NOTIFICATION WINDOW##################################
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'Yes'
# Url to notification file
NOTIFICATION   = 'http://tvbox.uiwap.com/kodi/norification.txt'
# Use either 'Text' or 'Image'
HEADERTYPE     = 'Text'
HEADERMESSAGE  = 'HackerTeam'
# url to image if using Image 500x50(Width can vary but height of image needs to be 50px)
HEADERIMAGE    = ''
# Background for Notification Window
BACKGROUND     = ''
#########################################################