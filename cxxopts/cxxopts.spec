%global debug_package %{nil}

Name:           cxxopts
Version:        3.3.1
Release:        1%{?dist}
Summary:        Lightweight C++ command line option parser

License:        MIT
URL:            https://github.com/jarro2783/cxxopts
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
cxxopts is a lightweight, header-only C++ library for parsing command line
options. It supports positional arguments, optional and required options,
default values, and help text generation.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>

%description devel
Header files and CMake integration files for %{name}.

%prep
%autosetup

%build
%cmake \
    -DCXXOPTS_BUILD_EXAMPLES=OFF \
    -DCXXOPTS_BUILD_TESTS=OFF \
    -DCXXOPTS_ENABLE_INSTALL=ON
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE
%doc README.md
%{_includedir}/cxxopts.hpp
%{_datadir}/cmake/cxxopts/
%{_datadir}/pkgconfig/cxxopts.pc

%changelog
* Tue May 12 2026 openEuler Builder <builder@openeuler.org> - 3.3.1-1
- Initial package for cxxopts 3.3.1
