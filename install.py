import pathlib
import sys
import time


vsc_config = pathlib.Path(__file__).parent.joinpath('config')
system_config = pathlib.Path.home().joinpath('.config', 'i3', 'config')

if system_config.exists():
    if system_config.is_symlink():
        if (x := pathlib.Path.readlink(system_config)) == vsc_config:
            sys.exit(0)
        else:
            print(f'Link already exists (target= {x})', file=sys.stderr)
            sys.exit(1)

        breakpoint()
    else:
        system_config.rename(system_config.parent.joinpath(f'config.bak.{time.time()}'))
        system_config.symlink_to(vsc_config)
else:
    system_config.parent.mkdir(parents=True, exists_ok=True)
    system_config.symlink_to(vsc_config)

sys.exit(os.system('i3-msg reload'))
