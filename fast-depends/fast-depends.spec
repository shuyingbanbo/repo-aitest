%global pypi_name fast-depends
%global module_name fast_depends

Name:           python-%{pypi_name}
Version:        3.0.8
Release:        1%{?dist}
Summary:        FastAPI Dependency Injection System extracted and cleared from HTTP domain logic
License:        MIT
URL:            https://github.com/Lancetnik/FastDepends
Source0:        fast-depends-3.0.8.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  python3-anyio
BuildRequires:  python3-typing-extensions

Requires:       python3-anyio >= 4.0.0
Requires:       python3-typing-extensions

%description
FastDepends - extracted and cleared from HTTP domain logic FastAPI Dependency
Injection System. Async and sync are both supported.

%package -n python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Provides:       python3dist(fast-depends[pydantic]) = 3.0.8
Provides:       python3.11dist(fast-depends[pydantic]) = 3.0.8
Requires:       python3-anyio >= 4.0.0
Requires:       python3-typing-extensions

%description -n python3-%{pypi_name}
FastDepends - extracted and cleared from HTTP domain logic FastAPI Dependency
Injection System. Async and sync are both supported.

%prep
%setup -q -n fast-depends-3.0.8

%build
# Install uv to provide uv_build backend, then build wheel
pip3 install uv
python3 -m pip wheel --no-deps -w dist .

%install
pip3 install --no-deps --ignore-installed \
    --prefix=%{_prefix} --root=%{buildroot} dist/*.whl

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{module_name}/
%{python3_sitelib}/fast_depends*.dist-info/

%changelog
* Wed Apr 22 2026 Builder <builder@openeuler.org> - 3.0.8-1
- Initial package for fast-depends 3.0.8
