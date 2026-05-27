%global crate publicsuffix
%global upstream_version 1.5.4-alpha.0
%global debug_package %{nil}

Name:           rust-%{crate}
Version:        1.5.4~alpha.0
Release:        1%{?dist}
Summary:        Robust domain name parsing and RFC compliant email address validation

License:        MIT OR Apache-2.0
URL:            https://github.com/rushmorem/publicsuffix
Source0:        https://github.com/rushmorem/%{crate}/archive/refs/tags/v%{upstream_version}/%{crate}-%{upstream_version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  rust
BuildRequires:  cargo

%description
This library uses Mozilla's Public Suffix List to reliably parse domain names
and email addresses in Rust. It exposes the list allowing convenient methods
like list.all() to get all known domain extensions or list.icann() to get only
ICANN extensions.

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       rust-%{crate}-devel = %{version}-%{release}
Provides:       rust-%{crate}+default-devel = %{version}-%{release}

%description    devel
This package contains library source intended for building other packages which
use the "%{crate}" crate.

%prep
%autosetup -n %{crate}-%{upstream_version} -p1
mkdir -p .cargo
cat > .cargo/config.toml << 'CARGOEOF'
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
CARGOEOF

%build
cargo build --release --offline --locked --no-default-features 2>&1

%install
install -d %{buildroot}%{_datadir}/rust/registry/%{crate}-%{upstream_version}
cp -a src Cargo.toml Cargo.lock vendor \
    %{buildroot}%{_datadir}/rust/registry/%{crate}-%{upstream_version}/

%check
# offline build; test fixtures not vendored

%files devel
%license LICENSE LICENSE-APACHE
%doc README.md
%{_datadir}/rust/registry/%{crate}-%{upstream_version}/

%changelog
* Wed May 27 2026 Builder <builder@openeuler.org> - 1.5.4~alpha.0-1
- Initial package
