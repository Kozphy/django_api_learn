  # -*- mode: ruby -*-
  # vi: set ft=ruby :

  # All Vagrant configuration is done below. The "2" in Vagrant.configure
  # configures the configuration version (we support older styles for
  # backwards compatibility). Please don't change it unless you know what
  # you're doing.
  Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  # setting os virtual enviornment 
  config.vm.box = "ubuntu/bionic64"
  # setting box version 
  config.vm.box_version = "~> 20200304.0.0"
    # setting port
  config.vm.network "forwarded_port", guest: 8000, host: 8000
  # how you can run script when you first create your server
  config.vm.provision "shell", inline: <<-SHELL
    # disable the auto update which conflicts with sudo apt-get update when it first run it on Ubuntu
    systemctl disable apt-daily.service
    systemctl disable apt-daily.timer
    
    sudo apt-get update
    # install python 3 virtual environment 
    sudo apt-get install -y python3-venv zip
    # create a bash aliases file setting python 3 to the default python version for our vagrant 
    touch /home/vagrant/.bash_aliases
    if ! grep -q PYTHON_ALIAS_ADDED /home/vagrant/.bash_aliases; then
      echo "# PYTHON_ALIAS_ADDED" >> /home/vagrant/.bash_aliases
      echo "alias python='python3'" >> /home/vagrant/.bash_aliases
    fi
  SHELL
  end