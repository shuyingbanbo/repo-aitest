%global debug_package %{nil}

Name:           toml11
Version:        4.4.0
Release:        1%{?dist}
Summary:        TOML for Modern C++

License:        MIT
URL:            https://github.com/ToruNiina/toml11
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
toml11 is a C++11/14/17/20 header-only TOML library. It provides
full support for TOML v1.0.0 with a clean, modern C++ API.

%package devel
Summary:        Development files for %{name}
Requires:       cmake

%description devel
Header files and CMake integration files for %{name}.

%prep
%autosetup

%build
%cmake \
    -DTOML11_INSTALL=ON \
    -DTOML11_BUILD_TESTS=OFF \
    -DTOML11_BUILD_EXAMPLES=OFF

%install
%cmake_install

%files devel
%license LICENSE
%doc README.md
%{_includedir}/toml.hpp
%{_includedir}/toml11/
%{_libdir}/cmake/toml11/

%changelog
* Thu May 14 2026 openEuler Builder <builder@openeuler.org> - 4.4.0-1
- Initial package for toml11 4.4.0
