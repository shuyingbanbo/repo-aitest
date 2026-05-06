Name:           python-litestar
Version:        3.0.0~b0
Release:        1%{?dist}
Summary:        Litestar - A production-ready, highly performant, extensible ASGI API Framework
License:        MIT
URL:            https://github.com/litestar-org/litestar
Source0:        litestar-3.0.0~b0.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-hatchling
BuildRequires:  python3-anyio
BuildRequires:  python3-httpx
BuildRequires:  python3-msgspec
BuildRequires:  python3-multidict
BuildRequires:  python3-sniffio
BuildRequires:  python3-click
BuildRequires:  python3-rich
BuildRequires:  python3-typing-extensions

Requires:       python3-anyio >= 3
Requires:       python3-httpx >= 0.22
Requires:       python3-msgspec >= 0.19.0
Requires:       python3-multidict >= 6.0.2
Requires:       python3-typing-extensions
Requires:       python3-click
Requires:       python3-rich >= 13.0.0
Requires:       python3-rich-click < 1.9
Requires:       python3-multipart >= 1.3.1
Requires:       python3-sniffio >= 1.3.1

%description
Litestar is a powerful, flexible yet opinionated ASGI framework, focused on
building APIs. It offers high-performance data validation, dependency injection,
first-class ORM integration, authorization primitives, a rich plugin API,
middleware, and much more.

%prep
%autosetup -n litestar-3.0.0~b0

%build
%pyproject_build

%install
%pyproject_install

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/litestar/
%{python3_sitelib}/litestar-*.dist-info/
%{_bindir}/litestar

%changelog
* Wed May 06 2026 Claude - 3.0.0~b0-1
- Initial package
