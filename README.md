This repo provides RPM packaging for
[facebook/watchman](https://github.com/facebook/watchman). This repo is used to
build the
[lehrenfried/watchman](https://copr.fedorainfracloud.org/coprs/lehrenfried/watchman/)
Fedora COPR repository, which you can use to get pre-built RPMs.

To install watchman using my COPR repository:

```bash
# Enable the lehrenfried/watchman copr repository.
$ sudo dnf copr enable lehrenfried/watchman

# Install the watchman RPM.
$ sudo dnf install watchman
```
