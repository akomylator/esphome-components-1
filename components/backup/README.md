# Backup

Save your ESPHome device configuration in firmware and and recover it if you lost source files. Just download it from `http://yourdevice.local/config.yaml`.

> WARNING: stored configuration is the same as shown by `esphome config` command. It fully worked but not the same as your original sources.

> WARNING: command line substitutions are not supported!

The configuration is very simple. Look at a sample below:
```yaml
# Full example of configuration entry
...
external_components:
  - source: github://dentra/esphome-components
...
backup:
  auth:
    username: !secret web_username
    password: !secret web_password
  force_update: false
```

##  Configuration variables:
* **auth** (*Optional*): Enables basic authentication with username and password.
 * **username** (**Required**, string): The username to use for authentication.
 * **password** (**Required**, string): The password to check for authentication.
* **force_update** (*Optional*, boolean): Unnecessary but might be needed when you changes in separated files are not detected properly. Default is False.