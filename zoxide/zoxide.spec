%global debug_package %{nil}

Name:           zoxide
Version:        0.9.9
Release:        1%{?dist}
Summary:        A smarter cd command for your terminal

License:        MIT
URL:            https://github.com/ajeetdsouza/zoxide
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

ExclusiveArch:  x86_64 aarch64

BuildRequires:  rust >= 1.88
BuildRequires:  cargo
BuildRequires:  gcc

%description
zoxide is a smarter cd command, inspired by z and autojump.
It remembers which directories you use most frequently, so you can
"jump" to them in just a few keystrokes.

%prep
%autosetup -n %{name}-%{version}

%build
%define _lto_cflags %{nil}
export CARGO_PROFILE_RELEASE_LTO=false
cargo build --release

%install
install -Dm755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/%{name}

%changelog
* Mon May 19 2026 OpenEuler Packaging <packaging@openeuler.org> - 0.9.9-1
- Initial package
