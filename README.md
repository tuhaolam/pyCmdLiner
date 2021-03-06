pycmdliner
==========

A scaffolding for developing python command line non interactive tools.

This package may be useful when developing command line tools in that it provides the logic that parses
and validates input commands and options and then invokes the user provided application logic.

The user of this module provides:
* an object implementing the application logic of the tool
* some basic configuration

then pycmdliner takes care of the rest

Usage
-----

First element when using this module is installing it. A packaged distribution is present on 
[http://pypi.python.org/pypi/pycmdliner]. Just download it and install through easy_install:

    easy_install -U pycmdliner-0.1.0-py2.7.egg

Second step is importing it in your python script:

    from pycmdliner import Pycmdliner

Third step is preparing the configuration. 
Configuration is provided as a dictionary to the module. This is an example:

    config = {'commandMapping':
    		{'command1': 'method1', 
    	 	'command2': 'method2'},
    	      'appHeader': 'My useless command line tool version 0.0.0.0.1',
              'usageString': "Read the manual!!"}

Up to now the configuration may contain 3 elements: mapping between commands and application logic methods,
content to be displayed in case of bad input, application header. See following Configuration section
for additional explanations.

Fourth step consists in instantiating a Pycmdliner object providing the object implementing application 
logic:

    cmdliner = Pycmdliner(config, applicationObject)
    
Fifth step: invoke process method passing input parameters (if no parameters are passed, command line arguments
are used by default.

    cmdliner.process()

Let's say our python script was called myTool, upon process method call, "My useless command line tool version 0.0.0.0.1"
will appear as header, then the first input parameter wil be matched with one of the elements of commandMapping
dictionary to find the proper method to be called on the passed object.

If the user called the script with three parameters: command1 a b, method method1 will be invoked on applicationObject
passing a and b as parameters of the method. The signature of the method is checked to ensure the number of 
input parameters is acceptable. If this is not true the usageString is printed out.

Configuration
-------------

The first element of the configuration dictionary states the mapping between input command and method to be called.
There are two ways to provide this mapping: 

* if the same application method has to be always executed (let's say there are no specific input commands to choose
  among, the mapping has to be stated with 'defaultCommand' entry in the dictionary. In this case no matter on 
  user input, the method provided as 'defaultCommand' is always called.

* if the tool serves multiple functionalities according to the command provided by the user, we assume the command
  is chosen through the first input argument (like for example: git commit. commit is the command). In this case
  the mapping is provided through 'commandMapping' dictionary, which states the method to be called for each command.

A header string can be provided through 'appHeader' key in configuration dictionary.

If the user of the tool provides an invalid command, no command at all, or an invalid number of parameters for 
the chosen command, the usage string is printed out. This can be configured in three ways:

* 'usageString' : The string rpesent in the config is printed out
* 'usageMethod' : In this case the method specified in 'usageMethod' key is invoked and supposed to return something
                  printable. The result is printed out.
* 'usageFile' : if we have to print a lot of stuff, this configuraiton key can be used and the content of the file
                is printed out.

License
-------
This module is Copyright 2012 Filippo Pacifici and is available under the [Apache License, Version 2.0][1].

[1]: http://www.apache.org/licenses/LICENSE-2.0