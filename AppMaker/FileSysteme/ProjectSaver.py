import json
import os
from AppMaker.FileSysteme.ProjectSavingEncoder import ProjectSavingEncoder


def ProjectSaver(ProjectName, UdFunc, UdVar, Udsrc, WindowConfig, GameSettings, ToImport, Items, Path,
                 SaveOnlyIfProjectAlreayExists=False):
    Items = list(Items)

    if not os.path.exists(f"{Path}/{ProjectName}") and not SaveOnlyIfProjectAlreayExists:
        os.makedirs(f"{Path}/{ProjectName}")

    elif not os.path.exists(f"{Path}/{ProjectName}") and SaveOnlyIfProjectAlreayExists:
        return False

    with open(f"{Path}/{ProjectName}/Code.py", "w") as WorldItemsFile:
        json.dump(Items, WorldItemsFile, cls=ProjectSavingEncoder)

    with open(f"{Path}/{ProjectName}/Window Config.txt", "w") as WindowConfigFile:
        json.dump(WindowConfig, WindowConfigFile, cls=ProjectSavingEncoder)

    with open(f"{Path}/{ProjectName}/Project Settings.txt", "w") as GameSettingsFile:
        json.dump(GameSettings, GameSettingsFile, cls=ProjectSavingEncoder)


def SceneStateSaver(ProjectName, Path, SceneState):
    if not os.path.exists(f"{Path}/{ProjectName}"):
        return False

    with open(f"{Path}//{ProjectName}//Scene state.txt", "w") as SceneStateFile:
        json.dump(SceneState, SceneStateFile, cls=ProjectSavingEncoder)

    return True
