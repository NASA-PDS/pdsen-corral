# pdsen-corral

Umbrella project to manage the build cycle for the PDS EN tools (continuous integration for development and stable releases).

The repository provides web pages to describe as automatically as possible the builds.

http://nasa-pds.github.io/pdsen-corral/

The details on how these pages can be generated is given after:



## Component's repository (e.g. validate, pds-deep-archive)

To enable the integration of a component in the build, its repository need to follow some rules.

### Set the continuous integration components with github actions

#### Principles

The continuous integration process has implement these mandary steps:
- create a **tag** (can be a -dev or snapshot tag)
- release package at least as github **release**, the package could also be deployed on pypi or maven artifactory but github release is the minimum requirements for publication.
- generate **changelog and requirements** files in gh-pages, directory pdsen-corral
- **ping pdsen-corral** by doing an empty commit

Most of these steps are implemented by the [pds-github-util](https://github.com/NASA-PDS/pds-github-util) library in [github actions](https://github.com/features/actions).
#### Examples

See examples of continuous integration implementation. Use them to initiate new repository:

For the **development** releases:
- python project: https://github.com/NASA-PDS/pds-doi-service/blob/master/.github/workflows/release-latest.yml
- java project: https://github.com/NASA-PDS/validate/blob/master/.github/workflows/snapshot-maven.yml

For **stable** release:
- java project: https://github.com/tloubrieu-jpl/harvest/blob/gh-pages/.github/workflows/maven-snapshot.yml
- python project: To Be Provided

### Everyday updates

#### Development or snapshot

The development or snapshot work is commited and pushed in the *master* branch of the repositories.

The github actions will publish the release files and update the local reports (changelog, requirements).
The github action will also trigger the generation of the gh-pages on pdsen-corral to reflect the latest updates.

#### Stable release

Create a stable release by creating and pushing a tag:

    git tag 2.3.0
    git push --tags

When a patch is developed to correct bugs in a stable release, create it with incremented last digit, here 2.3.1.

When a new tag is created the github action creates the local changelog and requirement reports.
The github action also triggers the generation of gh-pages on pdsen-corral to reference the latest patched stable versions. 


## in pdsen-corral repository

### Development build

Current development build (ie until beginning of UIT phase) is described on the **master** branch.

`.gitmodule` file must have a version containing 'dev' or 'SNAPSHOT', for example:

    [submodule "."]
        version = 10.0-SNAPSHOT

The modules are describes in submodule sections as follow:

    [submodule "pds-doi-service"]
        url = https://github.com/NASA-PDS/pds-doi-service/
        description = Manage DOIs


The latest dev or snapshot version of the components are integrated to the current snapshot build.

### Stable release

Stable releases are described in branch named after the build number (e.g. 10.1, 11.0, ...). The stable release process starts at the beginning of the UIT phase.

In .gitmodule, the current build version is described as follow:

    [submodule "."]
        version = 10.1
        
The components are described as follow:

    [submodule "pds-doi-service"]
        url = https://github.com/NASA-PDS/pds-doi-service/
        description = Manage DOIs       
        version = 1.0
        
The module's version are described with 2 digits only.
The last digit (patch version) is automatically updated to the latest whenever an update is done in the components.    

 

