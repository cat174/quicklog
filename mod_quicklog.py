import os
import json
import time
import re
import codecs
import urllib2
from gui import SystemMessages
from ResMgr import openSection as _openSection
from BigWorld import wg_getProductVersion as _productVersion
from gui.Scaleform.daapi.view.lobby.LobbyView import LobbyView
from notification.actions_handlers import NotificationsActionsHandlers
from gui.shared import events, g_eventBus

class quicklog():

    def __init__(self):

        self.name = 'cat174'
        self.version_name = '0.0.7'
        self.version_code = 9
        self.forum = 'http://forum.worldoftanks.eu/index.php?/topic/705127-'
        self.date = '17.12.2020'   
        print '[QuickLog] Baslatiliyor... [Yapimci:(%s)-Surum:(%s)-Tarih:(%s)-Forum:(%s)]' % (self.name, self.version_name, self.date, self.forum)
        self.cat_ql_boot()
        self.cat_feedback()

    def cat_feedback(self):
        try:
            #urllib2.urlopen('http://##########/lmstatus.php?key=%s---%s' % (self.version_name, self.version_code))
            pass
        except:
            print '[QuickLog] Geri Besleme Hata olustu'
       
    def cat_ql_boot(self):

        self.cat_ql_boot2()
        if self.ql_status:
            self.ql_set_list()
        else:
            print '[QuickLog]: Devre Disi'

    def ql_set_list(self):
        try:
            from gui.modsListApi import g_modsListApi
            g_modsListApi.addModification(id = 'quicklog', name = 'QuickLog', description = 'Python.log Dosyasini açar', icon = 'gui/maps/icons/quicklog.png', enabled = True, login = True, lobby = True, callback = lambda : self.cat_ql_open_log())
        except:
            print '[QuickLog] ModlistApi Bulunamadi'

    def cat_ql_open_log(self):
        try:
            py_file = os.getcwd()
            os.system("start notepad %s\python.log" % (py_file))
        except:
            print '[QuickLog]: Bir Hata olustu [OPEN]'

    def cat_ql_boot2(self):
        try:
            self.ql_status = self.cat_ql_json_read_status()
        except:
            print '[QuickLog]: Bir Hata olustu [Boot_2]'

    def cat_ql_json_read_status(self):
            try:    
                _jreturn = self.cat_core_json_read('/catcore/quicklog/settings.json', 'status')
                print '[QuickLog] ( %s )' % (_jreturn)  
                return _jreturn
            except:
                print '[QuickLog]: Bir Hata Olustu [JSON_READ] (Status)' 
    
    def cat_core_json_read(self, imlec1, imlec2):
        cat_file_last = os.getcwd()
        try:
            cat_directory = os.getcwd() + '/mods/configs/'
            cat_directory += imlec1
            cat_fileLine = []
            with codecs.open(cat_directory, 'r', 'utf-8') as cat_rawFile:
                cat_rawJson = cat_rawFile.read()
                for cat_line in cat_rawJson.split('\n'):
                    cat_line = re.sub(r'(^|\s+)//.*$|/\*(.|.\s)*?\*/', '', cat_line)
                    cat_line = cat_line.strip()
                    if cat_line:
                        cat_fileLine.append(cat_line)
                    cat_fileJson = ''.join(cat_fileLine)
                cat_json_give = json.loads(cat_fileJson)
                cat_rawFile.close()
                cat_finish = cat_json_give[imlec2]
                print '[CatCore]: Okundu (%s)' % (imlec2)
                return cat_finish    
        except:    
            os.chdir(cat_file_last)
            print '[CatCore]: Bir Hata Olustu [JSON_READ]'

    def core_jus_engine(self, ek1, ek2):
        cat_file_last = os.getcwd()
        try:
            cat_directory = os.getcwd() + '/mods/configs/'
            cat_directory += ek1
            cat_fileLine = []
            with codecs.open(cat_directory, 'r', 'utf-8') as cat_rawFile:
                cat_rawJson = cat_rawFile.read()
                for cat_line in cat_rawJson.split('\n'):
                    cat_line = re.sub(r'(^|\s+)//.*$|/\*(.|.\s)*?\*/', '', cat_line)
                    cat_line = cat_line.strip()
                    if cat_line:
                        cat_fileLine.append(cat_line)
                    cat_fileJson = ''.join(cat_fileLine)
                cat_json_give = json.loads(cat_fileJson)
                cat_rawFile.close()
                cat_finish = cat_json_give[ek2]
                print '[CatCore]: Okundu (%s)' % (ek2)
                return cat_finish    
        except:    
            os.chdir(cat_file_last)
            print '[CatCore]: (JusEngine) (Error)'

    def core_ms_info(self, cat_message):
        SystemMessages.pushMessage(cat_message, SystemMessages.SM_TYPE.Information)

    def core_ms_warning(self, cat_message):
        SystemMessages.pushMessage(cat_message, SystemMessages.SM_TYPE.Warning)

    def core_ms_error(self, cat_message):
        SystemMessages.pushMessage(cat_message, SystemMessages.SM_TYPE.Error)

def _overrideMethod(handler, cls, method):
    orig = getattr(cls, method)
    new = lambda *args, **kwargs: handler(orig, *args, **kwargs)
    setattr(cls, method, new if type(orig) is not property else property(new))

def _overrideStaticMethod(handler, cls, method):
    orig = getattr(cls, method)
    new = staticmethod(lambda *args, **kwargs: handler(orig, *args, **kwargs))
    setattr(cls, method, new if type(orig) is not property else property(new))

def _hookDecorator(func):
    def _oneDecorator(*args, **kwargs):
        def _twoDecorator(handler):
            func(handler, *args, **kwargs)
        return _twoDecorator
    return _oneDecorator

def nfa_boot(self, model, typeID, entityID, actionName):
    regex = re.compile('^https?://(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\\.)+[A-Z]{2,6}\\.?|\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3})(?::\\d+)?(?:/?|[/?]\\S+)$', re.IGNORECASE)
    if regex.match(actionName) is None:
        return g_nfah(self, model, typeID, entityID, actionName)
    else:
        g_eventBus.handleEvent(events.OpenLinkEvent(events.OpenLinkEvent.SPECIFIED, actionName))
        return
    return
    
class hookUtil():
    
    VERSION = tuple(map(int, _productVersion().split('.')))
    PATH = _openSection('../paths.xml')['Paths'].values()[0].asString    
    MODS = '/'.join([PATH, 'scripts', 'client', 'mods'])
    GUI_MODS = '/'.join([PATH, 'scripts', 'client', 'gui', 'mods'])
    INJECT = staticmethod(_hookDecorator(_overrideMethod))
    OVERRIDE_STATIC = staticmethod(_hookDecorator(_overrideStaticMethod))

g_hookUtil = hookUtil()
g_nfah = NotificationsActionsHandlers.handleAction
NotificationsActionsHandlers.handleAction = nfa_boot
g_quicklog = quicklog()

