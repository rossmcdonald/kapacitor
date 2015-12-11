Kapacitor
=========

An Ansible role to install, configure, and manage [Kapacitor](https://github.com/influxdb/kapacitor) (an open source framework for processing, monitoring, and alerting on time series data).

Requirements
------------

Prior knowledge/experience with [InfluxDB](https://github.com/influxdb/influxdb) and Kapacitor is highly recommended. Full documentation is available [here](https://docs.influxdata.com/kapacitor/v0.2/introduction/getting_started/).

Installation
------------

Either clone this repository, or install through Ansible Galaxy directly using the command:

```
ansible-galaxy install rossmcdonald.kapacitor
```

Role Variables
--------------

The high-level variables are stored in the `defaults/main.yml` file. The most important ones being:

```
# Channel of Kapacitor to install (stable, unstable, nightly)
kapacitor_install_version: stable
```

More advanced configuration options are stored in the `vars/main.yml` file, which includes all of the necessary bells and whistles to tweak your configuration.

Dependencies
------------

No other Ansible dependencies are required. This role was tested and developed with Ansible 1.9.4.

Example Playbook
----------------

An example playbook is included in the `test.yml` file. There is also a `Vagrantfile`, which can be used for quick local testing leveraging [Vagrant](https://www.vagrantup.com/).

Contributions and Feedback
--------------------------

Any contributions are welcome. For any bugs or feature requests, please open an issue through Github.

License
-------

MIT

Author
------

Created by [Ross McDonald](https://github.com/rossmcdonald).

