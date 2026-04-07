Name:           ruyi
Version:        0.48.0
Release:        0.alpha.20260317%{?dist}
Summary:        Package manager for RuyiSDK
License:        Apache-2.0
URL:            https://github.com/ruyisdk/ruyi
Source0:        ruyi-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-poetry-core

Requires:       python3-argcomplete >= 2.0.0
Requires:       python3-arpy
Requires:       python3-babel >= 2.8.0
Requires:       python3-fastjsonschema >= 2.15.1
Requires:       python3-jinja2 >= 3
Requires:       python3-pygit2 >= 1.6
Requires:       python3-pyyaml >= 5.4
Requires:       python3-requests >= 2
Requires:       python3-rich >= 11.2.0
Requires:       python3-semver >= 2.10
Requires:       python3-tomlkit >= 0.9

%description
Ruyi is the package manager for RuyiSDK, a comprehensive toolchain and
SDK distribution for RISC-V development. It provides easy installation and
management of cross-compilation toolchains, emulators, board support packages,
and other development tools for RISC-V platforms.

%prep
%autosetup -n ruyi-%{version}

%build
%pyproject_build

%install
%pyproject_install

%files
%license LICENSE-Apache.txt
%doc README.md
%{_bindir}/ruyi
%{python3_sitelib}/ruyi/
%{python3_sitelib}/ruyi-0.48.0a20260317*.dist-info/

%changelog
* Fri Apr 03 2026 OpenEuler Package Import <pkg@openeuler.org> - 0.48.0-0.alpha.20260317
- Initial package
