%global debug_package %{nil}

Name:           magic_enum
Version:        0.9.8
Release:        1%{?dist}
Summary:        Static reflection for enums for modern C++

License:        MIT
URL:            https://github.com/Neargye/magic_enum
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildArch:      noarch

%description
magic_enum is a header-only C++ library that provides static reflection
for enums. It supports enum to string, string to enum, enum iteration,
and more, without any macro or boilerplate code.

%package devel
Summary:        Development files for %{name}
BuildArch:      noarch

%description devel
Header files and CMake integration files for %{name}.

%prep
%autosetup

%build
%cmake \
    -DMAGIC_ENUM_OPT_INSTALL=ON \
    -DMAGIC_ENUM_OPT_BUILD_TESTS=OFF \
    -DMAGIC_ENUM_OPT_BUILD_EXAMPLES=OFF

%install
%cmake_install

%files devel
%license LICENSE
%doc README.md
%{_includedir}/magic_enum/
%{_datadir}/cmake/magic_enum/
%{_datadir}/magic_enum/
%{_datadir}/pkgconfig/magic_enum.pc

%changelog
* Thu May 14 2026 openEuler Builder <builder@openeuler.org> - 0.9.8-1
- Initial package for magic_enum 0.9.8
