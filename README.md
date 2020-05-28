# pdsen-corral
umbrella project to manage the build cycle (continuous integration and stable release) for the PDS EN tools.

# Develop and Test

    pip install -e 
    export GITHUB_TOKEN=<token value>
    python setup.py test


# Use

Update configuration in master branch, file: `.gitmodule`

Repostory generates page on gh-pages branch through githun actions.

Go to `http://nasa-pds.github.io/pdsen-corral/<build version>`

For example [http://nasa-pds.github.io/pdsen-corral/10.0](http://nasa-pds.github.io/pdsen-corral/10.0)

