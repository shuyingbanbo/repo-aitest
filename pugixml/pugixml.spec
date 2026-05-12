Name:           pugixml
Version:        1.15
Release:        1%{?dist}
Summary:        Light-weight, simple and fast XML parser for C++

License:        MIT
URL:            https://github.com/zeux/pugixml
Source0:        %{name}-%{version}.tar.gz

Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
pugixml is a light-weight C++ XML processing library. It features a DOM-like
interface with rich traversal and modification capabilities, an extremely fast
XML parser, and XPath 1.0 support.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files, CMake integration files, and pkgconfig files for %{name}.

%prep
%autosetup

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--build-id" \
    -DBUILD_SHARED_LIBS=ON \
    -DPUGIXML_BUILD_TESTS=OFF
%cmake_build

%install
%cmake_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/libpugixml.so.1
%{_libdir}/libpugixml.so.1.15

%files devel
%license LICENSE.md
%doc README.md
%{_includedir}/pugiconfig.hpp
%{_includedir}/pugixml.hpp
%{_libdir}/libpugixml.so
%{_libdir}/cmake/pugixml/
%{_libdir}/pkgconfig/pugixml.pc

%changelog
* Tue May 12 2026 openEuler Builder <builder@openeuler.org> - 1.15-1
- Initial package for pugixml 1.15
