%global debug_package %{nil}

Name:           git-delta
Version:        0.19.2
Release:        1%{?dist}
Summary:        A syntax-highlighting pager for git and diff output

License:        MIT
URL:            https://github.com/dandavison/delta
Source0:        %{url}/archive/%{version}/delta-%{version}.tar.gz

ExclusiveArch:  x86_64 aarch64

BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  gcc

%description
A syntax-highlighting pager for git, diff, and grep output.

%prep
%autosetup -n delta-%{version}

%build
%define _lto_cflags %{nil}
export CARGO_PROFILE_RELEASE_LTO=false
cargo build --release

%install
install -Dm755 target/release/delta %{buildroot}%{_bindir}/delta

%files
%license LICENSE
%doc README.md
%{_bindir}/delta

%changelog
* Mon May 19 2026 OpenEuler Packaging <packaging@openeuler.org> - 0.19.2-1
- Initial package
