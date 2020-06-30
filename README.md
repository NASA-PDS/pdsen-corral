# pdsen-corral

Umbrella project to manage the build cycle (continuous integration and stable release) for the PDS EN tools.

The master branch describes the current development version.

The releases description are in branch named after the build version (e.g. 10.0, 10.1).



## Use

### in components repostory (e.g. validate, pds-deep-archive)

Update the developement or snapshot versions in the master branch. The github actions will update the local reports (changelog, requirements).
The github action will also trigger the generation of the gh-pages on pdsen-corral to reflect the latest updates.

Create a stable release by creating a tag:

    git tag 2.3.0
    git push --tags

When a patch is developed to debug a stable release, a new tag is created with incremented last digit, here 2.3.1.

When a new tag is created a github action creates the local changelog and requirement reports.
The github action also triggers the generation of gh-pages on pdsen-corral to reference the latest patched stable versions. 



### in pdsen-corral repository

Update configuration in master or stable release branch, file: `.gitmodule`

.gitmodule file must have a version containing 'dev' or 'SNAPSHOT', for example:

    [submodule "."]
        version = 10.0-SNAPSHOT

Then commit and push the modification:
  
    
    git commit -a -m "new development build"
    git push        
        

Repository generates page on gh-pages branch through githun actions.

Go to `http://nasa-pds.github.io/pdsen-corral/



