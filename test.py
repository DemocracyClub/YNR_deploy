import sys

from ansibleci.config import Config
from ansibleci.runner import Runner
from ansibleci.defaults import ENABLED_TESTS

def main(config=False):

    # Create config instance.
    config = Config(load_defaults=True)

    # Load user-defined settings into config instance.
    try:
        import settings
        config.add_module(settings)
    except ImportError:
        pass

    ENABLED_TESTS.remove('ansibleci.tests.readme.Readme')
    ENABLED_TESTS.remove('ansibleci.tests.tag.Tag')

    # Start runner.
    success = Runner(config).run()

    # Exit with correct exit code.
    sys.exit(int(not success))

if __name__ == '__main__':
    main()
