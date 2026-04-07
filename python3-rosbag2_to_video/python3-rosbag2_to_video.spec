Name:           python3-rosbag2_to_video
Version:        1.0.1
Release:        1%{?dist}
Summary:        Command line tool to create a video from a rosbag recording
License:        Apache-2.0
URL:            https://github.com/fictionlab/rosbag2_to_video
Source0:        rosbag2_to_video-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools

%description
Command line tool to create a video from a rosbag recording.

%prep
%autosetup -n rosbag2_to_video-%{version}

%build
%pyproject_build

%install
%pyproject_install

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/rosbag2_to_video/
%{python3_sitelib}/rosbag2_to_video-%{version}*.dist-info/
%{_bindir}/rosbag2_to_video
%{_datadir}/ament_index/resource_index/packages/rosbag2_to_video
%{_datadir}/rosbag2_to_video/package.xml

%changelog
* Tue Apr 07 2026 OpenEuler Package Import <pkg@openeuler.org> - 1.0.1-1
- Initial package
