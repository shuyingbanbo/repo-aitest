%global ros_distro humble
%global pkg_name naoqi_bridge_msgs2
%global ros_pkg_name naoqi-bridge-msgs2
%global _lto_cflags %{nil}
%undefine _package_note_flags
%global __requires_exclude_from ^/opt/ros/.*

Name:           ros-%{ros_distro}-%{ros_pkg_name}
Version:        2.1.0
Release:        1%{?dist}
Summary:        Common ROS 2 messages and services used by ros-naoqi
License:        Apache-2.0
URL:            https://github.com/ros-naoqi/naoqi_bridge_msgs2
Source0:        %{pkg_name}-%{version}.tar.gz

BuildRequires:  cmake gcc gcc-c++ python3
BuildRequires:  ros-%{ros_distro}-ros-workspace
BuildRequires:  ros-%{ros_distro}-ament-cmake
BuildRequires:  ros-%{ros_distro}-rosidl-default-generators
BuildRequires:  ros-%{ros_distro}-action-msgs
BuildRequires:  ros-%{ros_distro}-sensor-msgs
BuildRequires:  ros-%{ros_distro}-nav-msgs
BuildRequires:  ros-%{ros_distro}-trajectory-msgs
BuildRequires:  ros-%{ros_distro}-std-msgs
BuildRequires:  ros-%{ros_distro}-geometry-msgs

Requires:       ros-%{ros_distro}-ros-workspace
Requires:       ros-%{ros_distro}-rosidl-default-runtime
Requires:       ros-%{ros_distro}-action-msgs
Requires:       ros-%{ros_distro}-sensor-msgs
Requires:       ros-%{ros_distro}-nav-msgs
Requires:       ros-%{ros_distro}-trajectory-msgs
Requires:       ros-%{ros_distro}-std-msgs
Requires:       ros-%{ros_distro}-geometry-msgs
Requires:       python3

%description
Commonly used ROS 2 messages and services inside ros-naoqi.

%prep
%autosetup -n %{pkg_name}-%{version}

%build
source /opt/ros/%{ros_distro}/setup.sh
SAFE_C="-O2 -g -pipe -fstack-protector-strong -Wall -Werror=format-security -Wp,-U_FORTIFY_SOURCE,-D_FORTIFY_SOURCE=2 -Wp,-D_GLIBCXX_ASSERTIONS -fasynchronous-unwind-tables -fstack-clash-protection"
SAFE_CXX="${SAFE_C} -fexceptions"
mkdir -p %{_vpath_builddir}
cd %{_vpath_builddir}
cmake .. \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_INSTALL_PREFIX=/opt/ros/%{ros_distro} \
  -DCMAKE_C_FLAGS="${SAFE_C}" \
  -DCMAKE_CXX_FLAGS="${SAFE_CXX}" \
  -DCMAKE_SHARED_LINKER_FLAGS="-Wl,-z,relro -Wl,--as-needed -Wl,-z,now" \
  -DBUILD_SHARED_LIBS=ON \
  -DBUILD_TESTING=OFF
cmake --build . -j1

%install
source /opt/ros/%{ros_distro}/setup.sh
cd %{_vpath_builddir}
DESTDIR=%{buildroot} cmake --install .

%files
%license LICENSE
/opt/ros/%{ros_distro}/*

%changelog
* Mon Apr 13 2026 OpenEuler Package Import <pkg@openeuler.org> - 2.1.0-1
- Initial package
