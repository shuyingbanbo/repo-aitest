Name:           rosx_introspection
Version:        2.3.0
Release:        1%{?dist}
Summary:        C++ library for ROS message introspection without ROS dependency
License:        GPL-2.0-only
URL:            https://github.com/facontidavide/rosx_introspection
Source0:        rosx_introspection-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  rapidjson-devel

%description
ROS X Introspection is a C++ library that allows parsing any ROS message
at runtime without requiring a full ROS installation. It supports ROS1,
ROS2, and vanilla cmake builds. The library provides runtime type
introspection for ROS1 and ROS2 message types.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development headers and libraries for rosx_introspection.

%prep
%autosetup -n rosx_introspection-%{version}

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_SHARED_LIBS=ON \
    -DROSX_HAS_JSON=ON \
    -DROSX_PYTHON_BINDINGS=OFF \
    -DBUILD_TESTING=OFF \
    -DBUILD_BENCHMARKS=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_libdir}/librosx_introspection.so

%files devel
%{_includedir}/rosx_introspection/

%changelog
* Thu Apr 09 2026 OpenEuler Package Import <pkg@openeuler.org> - 2.3.0-1
- Initial package
