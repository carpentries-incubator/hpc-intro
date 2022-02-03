help([==[

Description
===========
An illustration program for Amdahls Law that does fake work.


More information
================
 - Homepage: http://XXX
]==])

whatis([==[Description: 
 An illustration program for Amdahls Law that does fake work. ]==])
whatis([==[Homepage: http://XXX]==])
whatis([==[URL: http://XXX]==])

local root = "/project/def-sponsor00/easybuild/software/amdahl/1.0-foss-2021a"

conflict("amdahl")

if not ( isloaded("foss/2021a") ) then
    load("foss/2021a")
end

if not ( isloaded("SciPy-bundle/2021.05-foss-2021a") ) then
    load("SciPy-bundle/2021.05-foss-2021a")
end

prepend_path("CMAKE_PREFIX_PATH", root)
prepend_path("PATH", pathJoin(root, "bin"))
setenv("EBROOTAMDAHL", root)
setenv("EBVERSIONAMDAHL", "1.0")
setenv("EBDEVELAMDAHL", pathJoin(root, "easybuild/amdahl-1.0-foss-2021a-easybuild-devel"))

-- Built with EasyBuild version 4.5.1
