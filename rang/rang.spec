%global debug_package %{nil}

Name:           rang
Version:        3.2
Release:        1%{?dist}
Summary:        Header-only C++ library for terminal color and style output

License:        Unlicense
URL:            https://github.com/agauniyal/rang
Source0:        %{name}-%{version}.tar.gz

Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
rang is a header-only C++11 library for adding color and style to terminal
output. It uses ANSI escape codes on Linux and macOS, and Windows console
APIs on Windows. It has no external dependencies.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>

%description devel
Header files, CMake integration files, and pkgconfig files for %{name}.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE
%doc README.md
%{_includedir}/rang.hpp
%{_libdir}/cmake/rang/
%{_libdir}/pkgconfig/rang.pc

%changelog
* Tue May 12 2026 openEuler Builder <builder@openeuler.org> - 3.2-1
- Initial package for rang 3.2
