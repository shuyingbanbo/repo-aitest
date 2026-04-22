%global pypi_name faststream

Name:           python-%{pypi_name}
Version:        0.7.0~rc1
Release:        1%{?dist}
Summary:        FastStream: the simplest way to work with a messaging queues
License:        Apache-2.0
URL:            https://github.com/airtai/faststream
Source0:        faststream-0.7.0rc1.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  python3-anyio
BuildRequires:  python3-typing-extensions
BuildRequires:  python3-fast-depends

%description
FastStream simplifies the process of writing producers and consumers for
message queues, handling all the parsing, networking and documentation
generation automatically.

%package -n python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-anyio >= 4.0
Requires:       python3-typing-extensions >= 4.12.0
Requires:       python3-fast-depends >= 3.0.0

%description -n python3-%{pypi_name}
FastStream simplifies the process of writing producers and consumers for
message queues, handling all the parsing, networking and documentation
generation automatically.

%prep
%setup -q -n faststream-0.7.0rc1

%build
pip3 install uv
python3 -m pip wheel --no-deps -w dist .

%install
pip3 install --no-deps --ignore-installed \
    --prefix=%{_prefix} --root=%{buildroot} dist/%{pypi_name}*.whl

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}*.dist-info/
%{_bindir}/faststream

%changelog
* Wed Apr 22 2026 Builder <builder@openeuler.org> - 0.7.0~rc1-1
- Initial package for faststream 0.7.0rc1
