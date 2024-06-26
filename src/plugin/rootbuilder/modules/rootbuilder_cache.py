import mobase, os, threading
from pathlib import Path
from .rootbuilder_strings import RootBuilderStrings
from .rootbuilder_paths import RootBuilderPaths
from ..core.rootbuilder_settings import RootBuilderSettings
from ....common.common_utilities import *
from ..models.rootbuilder_cacheitem import *
from ....common.common_log import CommonLog
from typing import List, Dict

class RootBuilderCache:
    """Root Builder cache module, handles the hashing and recording of game files."""

    def __init__(self, organiser: mobase.IOrganizer, strings: RootBuilderStrings, paths: RootBuilderPaths, settings: RootBuilderSettings, log: CommonLog) -> None:
        self._organiser = organiser
        self._strings = strings
        self._paths = paths
        self._settings = settings
        self._log = log

    def cacheFileExists(self) -> bool:
        """Returns true if there is a current build data file."""
        filePath = self._strings.rbCachePath
        return Path(filePath).exists()

    _cache = None
    def loadCacheFile(self) -> Dict[str, CacheItem]:
        """Loads and returns the current cache file, or an empty object if none exists."""
        if self._cache is not None:
            return self._cache
        filePath = self._strings.rbCachePath
        self._cache = loadJson(filePath)
        if self._cache is not None:
            return self._cache
        return {}
    
    def saveCacheFile(self, data:dict) -> bool:
        """Saves new data to the current cache file."""
        self._cache = data
        filePath = self._strings.rbCachePath
        return saveJson(filePath, self._cache)
    
    def deleteCacheFile(self) -> bool:
        """Deletes the current cache file."""
        self._cache = None
        filePath = self._strings.rbCachePath
        return deleteFile(filePath)
    
    def cachedValidRootGameFiles(self) -> List[str]:
        """Gets the list of game files from cache, or from the raw files if none exists."""
        if self.cacheFileExists():
            gamePath = self._strings.gamePath
            cacheFiles = self.loadCacheFile()
            gameFiles = []
            for cacheFile in cacheFiles:
                relativePath = cacheFiles[cacheFile][RELATIVE]
                finalPath = Path(gamePath, relativePath)
                gameFiles.append(str(finalPath.absolute()))
            return gameFiles
        else:
            return self._paths.validGameRootFiles()
    
    _currentCache = {}
    def updateCache(self) -> Dict[str, CacheItem]:
        """Loads the current cache file and then updates it with any changes."""
        self._currentCache = self.loadCacheFile()
        cacheFiles = self.cachedValidRootGameFiles()
        gamePath = self._strings.gamePath
        useHash = self._settings.hash()
        tasks = []
        for file in cacheFiles:
            nt = threading.Thread(target=self._updateCache, args=[file, useHash, gamePath])
            nt.start()
            tasks.append(nt)
        for t in tasks:
            t.join()
        return self._currentCache
    
    def _updateCache(self, filePath:str, useHash:bool, gamePath:str):
        relativePath = self._paths.relativePath(gamePath, filePath)
        relativeLower = relativePath.lower()
        if (useHash and (relativeLower not in self._currentCache or self._currentCache[relativeLower][HASH] == "")) and Path(filePath).exists():
            self._currentCache[relativeLower] = CacheItem({
                RELATIVE: relativePath,
                HASH: hashFile(filePath),
                MODIFIED: os.path.getmtime(filePath),
                SIZE: os.path.getsize(filePath)
            })
        elif (not useHash and relativeLower not in self._currentCache):
            self._currentCache[relativeLower] = CacheItem({
                RELATIVE: relativePath,
                HASH: "",
                MODIFIED: os.path.getmtime(filePath),
                SIZE: os.path.getsize(filePath)
            })
