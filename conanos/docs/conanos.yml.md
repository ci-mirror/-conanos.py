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

<font color=gray>\# _Build worker image(VM template), i.e. Visual Studio, GCC, CLANG _</font>  
image: Visual Studio  
<font color=gray>\# _Compiler version(CONAN_VISUAL_VERSIONS)_</font>  
compiler: 15  
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
&emsp;&emsp;array:  
&emsp;&emsp;&emsp;CONAN_BUILD_REQUIRES:  
&emsp;&emsp;&emsp;&emsp;- some/1.0@conan/stable  
&emsp;&emsp;&emsp;&emsp;- other/1.0@conan/stable  
&emsp;&emsp;list:  
&emsp;&emsp;&emsp;- CONAN_EXCLUDE_VCVARS_PRECOMMAND  
&emsp;&emsp;&emsp;- CONAN_ALLOW_GCC_MINORS  
&emsp;&emsp;&emsp;- CONAN_DOCKER_32_IMAGES  
&emsp;&emsp;&emsp;- CONAN_ALWAYS_UPDATE_CONAN_DOCKER  
&emsp;&emsp;&emsp;- CONAN_DOCKER_IMAGE_SKIP_PULL  
&emsp;&emsp;&emsp;- CONAN_USE_DOCKER  
&emsp;&emsp;map:  
&emsp;&emsp;&emsp;- CONAN_DOCKER_USE_SUDO: False  
&emsp;&emsp;&emsp;- CONAN_PIP_USE_SUDO: False  
&emsp;&emsp;&emsp;- CONAN_UPLOAD: http://172.16.65.42:8081/artifactory/api/conan/conanos_3  
&emsp;&emsp;&emsp;- CONAN_BASH_PATH: path_to_windows_cygwin_msys2_bash  
&emsp;&emsp;&emsp;- CONAN_PIP_PACKAGE: 1.13.0  
&emsp;&emsp;&emsp;- CONAN_DOCKER_IMAGE_SKIP_UPDATE: False  
&emsp;&emsp;&emsp;- CONAN_DOCKER_HOME: clone_location_in_docker  
&emsp;&emsp;&emsp;- CONAN_DOCKER_IMAGE: conanio/gcc63  
&emsp;&emsp;upload:  
&emsp;&emsp;&emsp;- CONAN_STABLE_CHANNEL: stable  
&emsp;&emsp;&emsp;- CONAN_STABLE_BRANCH_PATTERN: testing/*  
&emsp;&emsp;&emsp;- CONAN_SKIP_CHECK_CREDENTIALS: False  
&emsp;&emsp;&emsp;- CONAN_UPLOAD_ONLY_WHEN_TAG  
&emsp;&emsp;&emsp;- CONAN_UPLOAD_ONLY_WHEN_STABLE  
&emsp;&emsp;&emsp;- CONAN_UPLOAD_RETRY  
&emsp;&emsp;&emsp;- CONAN_UPLOAD: https://api.bintray.com/conan/conan-community/conan@True@other_repo_name  
&emsp;&emsp;&emsp;- CONAN_REFERENCE
&emsp;&emsp;build_configuration:  
&emsp;&emsp;&emsp;- CONAN_VISUAL_RUNTIMES: MT,MD  
&emsp;&emsp;&emsp;- CONAN_VISUAL_VERSIONS: 15  
&emsp;&emsp;&emsp;- CONAN_BUILD_TYPES: Debug  
&emsp;&emsp;&emsp;- CONAN_OPTIONS: foobar:with_bar=True,foobar:with_qux=False  
&emsp;&emsp;&emsp;- CONAN_ARCHS: x86_64  
&emsp;&emsp;&emsp;- CONAN_APPLE_CLANG_VERSIONS: 6.1,8.0  
&emsp;&emsp;&emsp;- CONAN_CLANG_VERSIONS: 3.8,3.9,4.0  
&emsp;&emsp;pre_build:  
&emsp;&emsp;&emsp;- CONAN_PIP_INSTALL: pkg-foo==0.1.0,pkg-bar  
&emsp;&emsp;&emsp;- CONAN_DOCKER_ENTRY_SCRIPT: command  
&emsp;&emsp;&emsp;- CONAN_REMOTES:url1@True@remote_name  
&emsp;&emsp;&emsp;\#Specify a password for a remote named XXX  
&emsp;&emsp;&emsp;- CONAN_PASSWORD_XXX  
&emsp;&emsp;&emsp;\#Specify a login username for a remote named XXX  
&emsp;&emsp;&emsp;- CONAN_LOGIN_USERNAME_XXX  
&emsp;&emsp;&emsp;\#Conan Password, or API key if using Bintray  
&emsp;&emsp;&emsp;- CONAN_PASSWORD: password  
&emsp;&emsp;&emsp;\#Unique login username for all remotes. Will use "CONAN_USERNAME" when not present  
&emsp;&emsp;&emsp;- CONAN_LOGIN_USERNAME  
&emsp;custom:  
&emsp;&emsp;my_var1: value1  
&emsp;&emsp;my_var1: value2  

<font color=gray>\# _Scripts that run after cloning repository_</font>  
install:  
&emsp;- python build.py

\#------------------------------------#  
\# &emsp;&emsp;&nbsp; _Build configuration_&emsp;&emsp;&emsp; #  
\#------------------------------------#  
<font color=gray>\# _Build platform, i.e. x86, x64 (CONAN_ARCHS)_</font>  
platform: x64  

<font color=gray>\# _Build platform matrix_</font>  
<font color=gray>\#platform:  
\#&emsp;- x86  
\#&emsp;- x64</font>  

<font color=gray>\# _Build configuration, i.e. Debug, Release (CONAN_BUILD_TYPES)_</font>  
configuration: Release  

<font color=gray>\# _Configuration matrix_</font>  
<font color=gray>\#configuration:  
\#&emsp;- Debug  
\#&emsp;- Release</font>  

<font color=gray>\# _Compiler runtime for visual studio, i.e. MTd,MDd (CONAN_VISUAL_RUNTIMES)_</font>  
runtime: MTd  
<font color=gray>\# _Runtime matrix_</font>  
<font color=gray>\#runtime:  
\#&emsp;- MTd  
\#&emsp;- MDd</font>  

<font color=gray>\# _Conan-package-tools variables related to build_</font>  
conan:  
&emsp;<font color=gray>\# _conan package user space(CONAN_USERNAME)_</font>  
&emsp;- username: conanos  
&emsp;<font color=gray>\# _conan package user space(CONAN_CHANNEL)_</font>  
&emsp;- channel: stable  

\#------------------------------------#  
\# &emsp;&emsp;&ensp; _tests configuration_&emsp;&emsp;&emsp; #  
\#------------------------------------#

\#------------------------------------#  
\# &emsp;&emsp; _artifacts configuration_&emsp;&emsp; #  
\#------------------------------------#

\#------------------------------------#  
\# &emsp;&emsp;&emsp;&ensp; _global handlers_ &emsp;&emsp;&emsp; #  
\#------------------------------------#