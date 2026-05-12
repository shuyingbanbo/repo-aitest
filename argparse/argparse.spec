%global debug_package %{nil}

Name:           argparse
Version:        3.2
Release:        1%{?dist}
Summary:        Single-header argument parser library for C++17

License:        MIT
URL:            https://github.com/p-ranav/argparse
Source0:        %{name}-%{version}.tar.gz

Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
argparse is a single-header argument parser library for C++17. It is
inspired by Python's argparse module and supports positional arguments,
optional arguments, sub-commands, and compound arguments.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>

%description devel
Header files, CMake integration files, and pkgconfig files for %{name}.

%prep
%autosetup

%build
%cmake \
    -DARGPARSE_BUILD_TESTS=OFF \
    -DARGPARSE_BUILD_SAMPLES=OFF \
    -DARGPARSE_INSTALL=ON
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE
%doc README.md
%{_includedir}/argparse/
%{_libdir}/cmake/argparse/
%{_libdir}/pkgconfig/argparse.pc

%changelog
* Tue May 12 2026 openEuler Builder <builder@openeuler.org> - 3.2-1
- Initial package for argparse 3.2
