Name:           robin-map
Version:        1.4.1
Release:        1%{?dist}
Summary:        Fast C++ robin hood hash map and hash set library
License:        MIT
URL:            https://github.com/Tessil/robin-map
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
robin-map is a header-only C++ library providing fast hash map and hash set
containers based on robin hood hashing. It also installs CMake package files
for integrating the library with CMake-based projects.

%prep
%autosetup

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DTSL_ROBIN_MAP_ENABLE_INSTALL=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_includedir}/tsl/
%{_datadir}/cmake/tsl-robin-map/

%changelog
* Mon Apr 13 2026 OpenEuler Package Import <pkg@openeuler.org> - 1.4.1-1
- Initial package
