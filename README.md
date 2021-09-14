# PDS Engineering Node Corral

This umbrella project manages the build cycle for the toosl of the Engineering Node (EN) of the Planetary Data System (PDS). As such it aggregates status of the PDS EN components stable and development releases. It relies standardized continuous integration implemented by these components.

The provided service are web pages describing as automatically as possible the builds:

http://nasa-pds.github.io/pdsen-corral/

The content is intended for:
- PDS software users, to know what the latest and history of available software
- PDS EN test team, to know the scope of the up coming releases

The details on how these pages are generated is given after. It requires:
- to have continuous integration implemented on **components** of the build.
- to reference the components in the **psden-corral** repository


## In the pdsen-corral Repository

This section describes the composition of the `pdsen-corral` repository.


### Development build

Current development build (ie until beginning of UIT phase) is described on the **main** branch.

The `.gitmodule` file must have a version containing 'SNAPSHOT', for example:

    [submodule "."]
        version = 10.0-SNAPSHOT

The modules are describes in submodule sections as follow:

    [submodule "pds-doi-service"]
        url = https://github.com/NASA-PDS/pds-doi-service/

The latest dev or snapshot version of the components are integrated to the current snapshot build.


### Stable release

Stable releases are described in branch named after the build number (e.g. 10.1, 11.0, ...). The stable release process starts at the beginning of the UIT phase.

In `.gitmodule`, the current build version is described as follow:

    [submodule "."]
        version = 10.1
        
The components are described as follow:

    [submodule "pds-doi-service"]
        url = https://github.com/NASA-PDS/pds-doi-service/
        version = 1.0
        
The module's version are described with 2 digits only. The last digit (patch version) is automatically updated to the latest whenever an update is done in the components.


## Component Repositories (e.g. validate, pds-deep-archive)

To enable the integration of a component in the build, each repository needs to follow some rules.


### Continuous Integration with GitHub Actions

The approach of using [GitHub Actions](https://github.com/features/actions) is described in this section.


#### Principles

The continuous integration process has implement these mandary steps:
- create a **tag** (can be a -dev or snapshot tag)
- release package at least as github **release**, the package could also be deployed on pypi or maven artifactory but github release is the minimum requirements for publication.
- generate **changelog and requirements** files in gh-pages, directory pdsen-corral
- **ping pdsen-corral** by doing an empty commit

Most of these steps are implemented by the [pds-github-util](https://github.com/NASA-PDS/pds-github-util) library in [GitHub Actions](https://github.com/features/actions).

The component needs a secret `ADMIN_GITHUB_TOKEN` which value is a GitHub personal access token allowed to push to `pdsen-corral`.


#### Examples

See examples of continuous integration implementation. Use them to initiate new repository:

For the **development** releases:
- Python project: https://github.com/NASA-PDS/pds-doi-service/blob/main/.github/workflows/release-latest.yml
- Java project: https://github.com/NASA-PDS/validate/blob/main/.github/workflows/snapshot-maven.yml

For **stable** release:
- java project: https://github.com/tloubrieu-jpl/harvest/blob/main/.github/workflows/release.yml
- python project: To Be Provided


### Everyday updates

Common updates are described in this section.


#### Development or Snapshot

The development or snapshot work is committed and pushed in the *main* branch of the repositories.

The GitHub Actions will publish the release files and update the local reports (changelog, requirements). The GitHub Action will also trigger the generation of the `gh-pages` on `pdsen-corral` to reflect the latest updates.


#### Stable Release

Create a stable release by creating and pushing a tag:

    git tag 2.3.0
    git push --tags

When a patch is developed to correct bugs in a stable release, create it with incremented last digit, here 2.3.1.

When a new tag is created the github action creates the local changelog and requirement reports. The GitHub Action also triggers the generation of `gh-pages` on `pdsen-corral` to reference the latest patched stable versions. 
