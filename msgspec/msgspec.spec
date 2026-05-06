Name:           python-msgspec
Version:        0.19.0
Release:        1%{?dist}
Summary:        A fast serialization and validation library, with builtin support for JSON, MessagePack, YAML, and TOML

License:        BSD-3-Clause
URL:            https://github.com/jcrist/msgspec
Source0:        msgspec-0.19.0.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  gcc

Provides:       python3-msgspec = %{version}-%{release}

%description
A fast serialization and validation library, with builtin support for JSON,
MessagePack, YAML, and TOML.

%prep
%autosetup -n msgspec-%{version}

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.md
%{python3_sitearch}/msgspec/
%{python3_sitearch}/msgspec-%{version}*.egg-info/

%changelog
* Wed May 06 2026 Claude - 0.19.0-1
- Initial package
