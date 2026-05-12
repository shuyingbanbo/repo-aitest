%global debug_package %{nil}

Name:           xtl
Version:        0.8.2
Release:        1%{?dist}
Summary:        Basic tools for the xtensor ecosystem

License:        BSD-3-Clause
URL:            https://github.com/xtensor-stack/xtl
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
xtl provides basic tools used by the xtensor ecosystem, including meta-programming
utilities, type traits, and optional/variant-like types. It is a header-only library
with no external dependencies.

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
    -DBUILD_TESTS=OFF
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE
%doc README.md
%{_includedir}/xtl/
%{_datadir}/cmake/xtl/
%{_datadir}/pkgconfig/xtl.pc

%changelog
* Tue May 12 2026 openEuler Builder <builder@openeuler.org> - 0.8.2-1
- Initial package for xtl 0.8.2
