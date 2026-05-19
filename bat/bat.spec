%global crate_name bat
%global debug_package %{nil}

Name:           bat
Version:        0.26.1
Release:        1%{?dist}
Summary:        A cat(1) clone with wings

License:        MIT OR Apache-2.0
URL:            https://github.com/sharkdp/bat
Source0:        %{url}/archive/v%{version}/%{crate_name}-%{version}.tar.gz

ExclusiveArch:  x86_64 aarch64

BuildRequires:  rust >= 1.88
BuildRequires:  cargo
BuildRequires:  gcc
BuildRequires:  make

%description
bat is a cat(1) clone with syntax highlighting and Git integration.
It supports automatic paging, line numbers, Git modifications display,
and syntax highlighting for a large number of programming languages.

%prep
%autosetup -n %{crate_name}-%{version}

%build
%define _lto_cflags %{nil}
export CARGO_PROFILE_RELEASE_LTO=false
cargo build --release --no-default-features --features application

%install
install -Dm755 target/release/%{crate_name} %{buildroot}%{_bindir}/%{crate_name}

%files
%license LICENSE-MIT LICENSE-APACHE
%doc README.md CHANGELOG.md
%{_bindir}/%{crate_name}

%changelog
* Mon May 19 2026 OpenEuler Packaging <packaging@openeuler.org> - 0.26.1-1
- Initial package
