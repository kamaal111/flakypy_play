set export

DEFAULT_VIRTUAL_ENVIRONMENT := ".venv"

test virtual-environment=DEFAULT_VIRTUAL_ENVIRONMENT:
    #!/bin/zsh

    VIRTUAL_ENVIRONMENT="{{ virtual-environment }}"

    . $VIRTUAL_ENVIRONMENT/bin/activate
    pytest


setup-virtual-environment virtual-environment=DEFAULT_VIRTUAL_ENVIRONMENT:
    #!/bin/zsh

    VIRTUAL_ENVIRONMENT="{{ virtual-environment }}"

    if [ ! -d $VIRTUAL_ENVIRONMENT ]
    then
        python -m venv $VIRTUAL_ENVIRONMENT
    fi
    . $VIRTUAL_ENVIRONMENT/bin/activate
    pip install poetry
    poetry install
    just install-python-modules $VIRTUAL_ENVIRONMENT

[private]
install-python-modules virtual-environment:
    #!/bin/zsh

    VIRTUAL_ENVIRONMENT="{{ virtual-environment }}"

    . $VIRTUAL_ENVIRONMENT/bin/activate
    poetry install
