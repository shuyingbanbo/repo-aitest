%global ros_distro humble
%global pkg_name situational_graphs_msgs
%global ros_pkg_name situational-graphs-msgs

Name:           ros-%{ros_distro}-%{ros_pkg_name}
Version:        0.0.1
Release:        1%{?dist}
Summary:        Custom ROS 2 messages for situational graphs
License:        GPL-3.0
URL:            https://github.com/snt-arg/situational_graphs_msgs.git
Source0:        %{pkg_name}-%{version}.tar.gz

BuildRequires:  cmake gcc gcc-c++ python3
BuildRequires:  ros-%{ros_distro}-ament-cmake
BuildRequires:  ros-%{ros_distro}-rosidl-default-generators
BuildRequires:  ros-%{ros_distro}-builtin-interfaces
BuildRequires:  ros-%{ros_distro}-std-msgs
BuildRequires:  ros-%{ros_distro}-geometry-msgs
BuildRequires:  ros-%{ros_distro}-sensor-msgs
BuildRequires:  ros-%{ros_distro}-visualization-msgs

%global __requires_exclude_from ^/opt/ros/.*

Requires:       ros-%{ros_distro}-rosidl-default-runtime
Requires:       ros-%{ros_distro}-builtin-interfaces
Requires:       ros-%{ros_distro}-std-msgs
Requires:       ros-%{ros_distro}-geometry-msgs
Requires:       ros-%{ros_distro}-sensor-msgs
Requires:       ros-%{ros_distro}-visualization-msgs
Requires:       python3

%description
Custom messages used by s_graphs repo and its dependencies.
Provides ROS 2 message and service definitions for situational graphs.

%prep
%autosetup -n %{pkg_name}-%{version}

%build
source /opt/ros/%{ros_distro}/setup.sh
# Use safe flags that avoid -mbranch-protection=standard and LTO (qemu/GCC segfault workaround)
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
/opt/ros/%{ros_distro}/*

%changelog
* Thu Apr 09 2026 OpenEuler Package Import <pkg@openeuler.org> - 0.0.1-1
- Initial package
