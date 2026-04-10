%global ros_distro humble
%global pkg_name clearpath_ros2_socketcan_interface
%global ros_pkg_name clearpath-ros2-socketcan-interface
%global _lto_cflags %{nil}
%undefine _package_note_flags
%global __requires_exclude_from ^/opt/ros/.*

Name:           ros-%{ros_distro}-%{ros_pkg_name}
Version:        2.1.4
Release:        1%{?dist}
Summary:        ROS 2 SocketCAN interface library and launch helpers for Clearpath robots
License:        BSD-3-Clause
URL:            https://github.com/clearpathrobotics/clearpath_ros2_socketcan_interface.git
Source0:        %{pkg_name}-%{version}.tar.gz

BuildRequires:  cmake gcc gcc-c++ python3
BuildRequires:  ros-%{ros_distro}-ros-workspace
BuildRequires:  ros-%{ros_distro}-ament-cmake
BuildRequires:  ros-%{ros_distro}-ament-cmake-ros
BuildRequires:  ros-%{ros_distro}-can-msgs
BuildRequires:  ros-%{ros_distro}-rclcpp

Requires:       ros-%{ros_distro}-ros-workspace
Requires:       ros-%{ros_distro}-ros2-socketcan
Requires:       ros-%{ros_distro}-can-msgs
Requires:       ros-%{ros_distro}-rclcpp
Requires:       ros-%{ros_distro}-launch
Requires:       ros-%{ros_distro}-launch-ros
Requires:       ros-%{ros_distro}-rclpy
Requires:       ros-%{ros_distro}-lifecycle-msgs
Requires:       iproute
Requires:       python3

%description
A ROS 2 package that provides a SocketCAN interface library, launch files, and
lifecycle activation helpers for Clearpath Robotics CAN bus integrations.

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
* Fri Apr 10 2026 OpenEuler Package Import <pkg@openeuler.org> - 2.1.4-1
- Initial package
