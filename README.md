# pdsen-corral
umbrella project to manage the build cycle (continuous integration and stable release) for the PDS EN tools.

## Develop and Test

    pip install -e 
    export GITHUB_TOKEN=<token value>
    python setup.py test


## Use

Update configuration in master branch, file: `.gitmodule`

## Development release

    git pull

.gitmodule file must have a version containing 'dev' or 'SNAPSHOT', for example:

    [submodule "."]
        version = 10.0-SNAPSHOT

Then commit and push the modification:
  
    
    git commit -a -m "new development build"
    git push        
        

Repository generates page on gh-pages branch through githun actions.

Go to `http://nasa-pds.github.io/pdsen-corral/<build version>`

For example [http://nasa-pds.github.io/pdsen-corral/10.0-SNAPSHOT](http://nasa-pds.github.io/pdsen-corral/10.0SNAPSHOT)

## Tag release

    git pull

.gitmodule file must have a stable (not containing 'dev' or 'SNAPSHOT'), for example:

    [submodule "."]
        version = 10.0

Then commit, create tag and push the modification:
  

    git commit -a -m "new stable build"
    git tag '10.0'
    git push --tags    
        
Repository generates page on gh-pages branch through githun actions.

Go to `http://nasa-pds.github.io/pdsen-corral/<build version>`

For example [http://nasa-pds.github.io/pdsen-corral/10.0-SNAPSHOT](http://nasa-pds.github.io/pdsen-corral/10.0SNAPSHOT)

