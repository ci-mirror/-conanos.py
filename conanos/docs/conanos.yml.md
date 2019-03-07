# conanos.yml reference

<font color=gray>\#  _Notes:_  
\#  - _Minimal conanos.yml file is an empty file. All sections are optional._  
\#  - _Indent each level of configuration with 2 spaces. Do not use tabs!_  
\#  - _All section names are case-sensitive_  
\#  - _Section names should be unique on each level_</font>

\#------------------------------------#  
\# &emsp;&emsp;&nbsp; _General configuration_&emsp;&emsp; #  
\#------------------------------------#  

<font color=gray>\# _Version format_</font>  
version: 0.0.1

<font color=gray>\# _Url of recipe repository_</font>  
recipe_repository: http://172.16.65.44/conanos

<font color=gray>\# _Branch pattern_</font>  
branch: testing/*

<font color=gray>\# _The name of the taget sdk_</font>  
scheme: webstreamer

<font color=gray>\# _Libraries that the target sdk contains_</font>  
packages:  
&emsp;- libffi  
&emsp;- zlib  
&emsp;- glib  
&emsp;- gtk-doc-lite  
&emsp;- gstreamer

<font color=gray>\# _Libraries that the target sdk contains_  
\# _, outside the default repository_</font>  
scattered:  
&emsp;- package: lib_a  
&emsp;&ensp;&nbsp;url: http://host_a/path_a  
&emsp;&ensp;&nbsp;branch: testing/x.x.x  
&emsp;- package: lib_b  
&emsp;&ensp;&nbsp;url: http://host_b/path_b  
&emsp;&ensp;&nbsp;branch: testing/x.x.y  

\#------------------------------------#  
\# &emsp; _Environment configuration_&emsp; #  
\#------------------------------------#  

<font color=gray>\# _Build worker image(VM template)_</font>  
image: Visual Studio  
<font color=gray>\# _Directory mapping_</font>  
volume:  
&emsp;- from: host_dir  
&emsp;- to: vm_dir  
<font color=gray>\# _Scripts that are called at very beginning, before repo cloning_</font>  
init:  
&emsp;- pip install conan --upgrade  
&emsp;- pip install conan_package_tools --upgrade  
&emsp;- pip install conanos

<font color=gray>\# _Environment variables_</font>  
environment:  
&emsp;\# Environment variables from conan-package-tools  
&emsp;cpt:  
&emsp;&emsp;CONAN_VISUAL_VERSIONS: 15  
&emsp;&emsp;CONAN_USERNAME: conanos  
&emsp;&emsp;CONAN_STABLE_BRANCH_PATTERN: testing/*  
&emsp;&emsp;CONAN_UPLOAD: http://172.16.65.42:8081/artifactory/api/conan/conanos_3  
&emsp;custom:  
&emsp;&emsp;my_var1: value1  
&emsp;&emsp;my_var1: value2  

\#------------------------------------#  
\# &emsp;&emsp;&nbsp; _build configuration_&emsp;&emsp;&emsp; #  
\#------------------------------------#

\#------------------------------------#  
\# &emsp;&emsp;&ensp; _tests configuration_&emsp;&emsp;&emsp; #  
\#------------------------------------#

\#------------------------------------#  
\# &emsp;&emsp; _artifacts configuration_&emsp;&emsp; #  
\#------------------------------------#

\#------------------------------------#  
\# &emsp;&emsp;&emsp;&ensp; _global handlers_ &emsp;&emsp;&emsp; #  
\#------------------------------------#