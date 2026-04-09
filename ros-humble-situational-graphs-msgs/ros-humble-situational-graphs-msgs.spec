%global ros_distro humble
%global pkg_name situational_graphs_msgs
%global ros_pkg_name situational-graphs-msgs

Name:           ros-%{ros_distro}-%{ros_pkg_name}
Version:        0.0.1
Release:        1%{?dist}
Summary:        Custom messages for s_graphs
License:        GPL-3.0
URL:            https://github.com/snt-arg/situational_graphs_msgs.git
Source0:        %{pkg_name}-%{version}.tar.gz

BuildRequires:  ros-%{ros_distro}-ament-cmake
BuildRequires:  ros-%{ros_distro}-builtin-interfaces
BuildRequires:  ros-%{ros_distro}-rosidl-default-generators
BuildRequires:  ros-%{ros_distro}-std-msgs
BuildRequires:  ros-%{ros_distro}-geometry-msgs
BuildRequires:  ros-%{ros_distro}-sensor-msgs
BuildRequires:  ros-%{ros_distro}-visualization-msgs
BuildRequires:  cmake gcc gcc-c++ python3

# ROS libs live under /opt/ros/humble/lib/ (non-standard ldconfig path).
# The ros-humble-* RPMs don't declare Provides: lib*.so() in metadata,
# so suppress auto-dependency scanning for files installed to /opt/ros/.
# Explicit package-name Requires: below cover the runtime dependencies.
%global __requires_exclude_from ^/opt/ros/.*

Requires:       ros-%{ros_distro}-fastcdr
Requires:       ros-%{ros_distro}-geometry-msgs
Requires:       ros-%{ros_distro}-sensor-msgs
Requires:       ros-%{ros_distro}-std-msgs
Requires:       ros-%{ros_distro}-visualization-msgs
Requires:       ros-%{ros_distro}-rcutils
Requires:       ros-%{ros_distro}-rosidl-runtime-c
Requires:       ros-%{ros_distro}-rosidl-typesupport-c
Requires:       ros-%{ros_distro}-rosidl-typesupport-cpp
Requires:       ros-%{ros_distro}-rmw-fastrtps-cpp
Requires:       ros-%{ros_distro}-rosidl-typesupport-introspection-c
Requires:       ros-%{ros_distro}-rosidl-typesupport-introspection-cpp
Requires:       python3

%description
Custom messages used by s_graphs repo and its dependencies.

%prep
%autosetup -n %{pkg_name}-%{version}

%build
# Disable LTO and AArch64 BTI hardening flags to prevent GCC segfaults
# with ROS2 generated C/C++17 typesupport code
%define _lto_cflags %{nil}
export CFLAGS="${CFLAGS//-flto=auto/}"
export CFLAGS="${CFLAGS//-ffat-lto-objects/}"
export CFLAGS="${CFLAGS//-mbranch-protection=standard/}"
export CFLAGS="$(echo "$CFLAGS" | sed 's|-specs=[^ ]*generic-hardened-cc1||g')"
export CXXFLAGS="${CXXFLAGS//-flto=auto/}"
export CXXFLAGS="${CXXFLAGS//-ffat-lto-objects/}"
export CXXFLAGS="${CXXFLAGS//-mbranch-protection=standard/}"
export CXXFLAGS="$(echo "$CXXFLAGS" | sed 's|-specs=[^ ]*generic-hardened-cc1||g')"
export LDFLAGS="${LDFLAGS//-flto=auto/}"
source /opt/ros/%{ros_distro}/setup.sh
%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_INSTALL_PREFIX=/opt/ros/%{ros_distro} \
  -DBUILD_TESTING=OFF
%cmake_build -- -j2

%install
source /opt/ros/%{ros_distro}/setup.sh
%cmake_install

%files
/opt/ros/%{ros_distro}/*

%changelog
* Wed Apr 08 2026 OpenEuler Package Import <pkg@openeuler.org> - 0.0.1-1
- Initial package
