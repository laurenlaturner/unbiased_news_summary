# This file will be configured to contain variables for CPack. These variables
# should be set in the CMake list file of the project before CPack module is
# included. The list of available CPACK_xxx variables and their associated
# documentation may be obtained using
#  cpack --help-variable-list
#
# Some variables are common to all generators (e.g. CPACK_PACKAGE_NAME)
# and some are specific to a generator
# (e.g. CPACK_NSIS_EXTRA_INSTALL_COMMANDS). The generator specific variables
# usually begin with CPACK_<GENNAME>_xxxx.


set(CPACK_BUILD_SOURCE_DIRS "C:/Users/laure/Desktop/sentencepiece-master;C:/Users/laure/Desktop/llm, api, ai, nlp projects/unbiased_news_summary/build")
set(CPACK_CMAKE_GENERATOR "Visual Studio 17 2022")
set(CPACK_COMPONENT_UNSPECIFIED_HIDDEN "TRUE")
set(CPACK_COMPONENT_UNSPECIFIED_REQUIRED "TRUE")
set(CPACK_DEBIAN_PACKAGE_MAINTAINER "Taku Kudo")
set(CPACK_DEFAULT_PACKAGE_DESCRIPTION_FILE "C:/Users/laure/AppData/Local/Programs/Python/Python313/Lib/site-packages/cmake/data/share/cmake-4.0/Templates/CPack.GenericDescription.txt")
set(CPACK_DEFAULT_PACKAGE_DESCRIPTION_SUMMARY "sentencepiece built using CMake")
set(CPACK_DMG_SLA_USE_RESOURCE_FILE_LICENSE "ON")
set(CPACK_GENERATOR "7Z")
set(CPACK_INNOSETUP_ARCHITECTURE "x64")
set(CPACK_INSTALL_CMAKE_PROJECTS "C:/Users/laure/Desktop/llm, api, ai, nlp projects/unbiased_news_summary/build;sentencepiece;ALL;/")
set(CPACK_INSTALL_PREFIX "C:/Users/laure/Desktop/llm, api, ai, nlp projects/unbiased_news_summary/buildroot")
set(CPACK_MODULE_PATH "")
set(CPACK_NSIS_DISPLAY_NAME "sentencepiece 0.2.1")
set(CPACK_NSIS_INSTALLER_ICON_CODE "")
set(CPACK_NSIS_INSTALLER_MUI_ICON_CODE "")
set(CPACK_NSIS_INSTALL_ROOT "$PROGRAMFILES64")
set(CPACK_NSIS_PACKAGE_NAME "sentencepiece 0.2.1")
set(CPACK_NSIS_UNINSTALL_NAME "Uninstall")
set(CPACK_OUTPUT_CONFIG_FILE "C:/Users/laure/Desktop/llm, api, ai, nlp projects/unbiased_news_summary/build/CPackConfig.cmake")
set(CPACK_PACKAGE_CONTACT "taku@google.com")
set(CPACK_PACKAGE_DEFAULT_LOCATION "/")
set(CPACK_PACKAGE_DESCRIPTION_FILE "C:/Users/laure/AppData/Local/Programs/Python/Python313/Lib/site-packages/cmake/data/share/cmake-4.0/Templates/CPack.GenericDescription.txt")
set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "sentencepiece built using CMake")
set(CPACK_PACKAGE_FILE_NAME "sentencepiece-0.2.1-win64")
set(CPACK_PACKAGE_INSTALL_DIRECTORY "sentencepiece 0.2.1")
set(CPACK_PACKAGE_INSTALL_REGISTRY_KEY "sentencepiece 0.2.1")
set(CPACK_PACKAGE_NAME "sentencepiece")
set(CPACK_PACKAGE_RELOCATABLE "true")
set(CPACK_PACKAGE_VENDOR "Humanity")
set(CPACK_PACKAGE_VERSION "0.2.1")
set(CPACK_PACKAGE_VERSION_MAJOR "0")
set(CPACK_PACKAGE_VERSION_MINOR "2")
set(CPACK_PACKAGE_VERSION_PATCH "1")
set(CPACK_RESOURCE_FILE_LICENSE "C:/Users/laure/Desktop/sentencepiece-master/LICENSE")
set(CPACK_RESOURCE_FILE_README "C:/Users/laure/Desktop/sentencepiece-master/README.md")
set(CPACK_RESOURCE_FILE_WELCOME "C:/Users/laure/AppData/Local/Programs/Python/Python313/Lib/site-packages/cmake/data/share/cmake-4.0/Templates/CPack.GenericWelcome.txt")
set(CPACK_SET_DESTDIR "OFF")
set(CPACK_SOURCE_GENERATOR "TXZ")
set(CPACK_SOURCE_IGNORE_FILES "/build/;/.git/;/dist/;/sdist/;~$;")
set(CPACK_SOURCE_OUTPUT_CONFIG_FILE "C:/Users/laure/Desktop/llm, api, ai, nlp projects/unbiased_news_summary/build/CPackSourceConfig.cmake")
set(CPACK_STRIP_FILES "TRUE")
set(CPACK_SYSTEM_NAME "win64")
set(CPACK_THREADS "1")
set(CPACK_TOPLEVEL_TAG "win64")
set(CPACK_WIX_SIZEOF_VOID_P "8")

if(NOT CPACK_PROPERTIES_FILE)
  set(CPACK_PROPERTIES_FILE "C:/Users/laure/Desktop/llm, api, ai, nlp projects/unbiased_news_summary/build/CPackProperties.cmake")
endif()

if(EXISTS ${CPACK_PROPERTIES_FILE})
  include(${CPACK_PROPERTIES_FILE})
endif()
