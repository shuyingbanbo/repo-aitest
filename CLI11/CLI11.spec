%global debug_package %{nil}

Name:           CLI11
Version:        2.6.2
Release:        1%{?dist}
Summary:        Command line parser for C++11 and beyond

License:        BSD-3-Clause
URL:            https://github.com/CLIUtils/CLI11
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
CLI11 is a header-only command line parser for C++11 and beyond. It supports
subcommands, options, flags, positional arguments, validators, and help text
generation. It has no external dependencies.

%package devel
Summary:        Development files for %{name}
BuildArch:      noarch
Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>

%description devel
Header files and CMake integration files for %{name}.

%prep
%autosetup

%build
%cmake \
    -DCLI11_BUILD_TESTS=OFF \
    -DCLI11_BUILD_EXAMPLES=OFF \
    -DCLI11_SINGLE_FILE=OFF \
    -DCLI11_INSTALL=ON
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE
%doc README.md
%{_includedir}/CLI/
%{_datadir}/cmake/CLI11/
%{_datadir}/pkgconfig/CLI11.pc

%changelog
* Tue May 12 2026 openEuler Builder <builder@openeuler.org> - 2.6.2-1
- Initial package for CLI11 2.6.2
