Name:           python-markdownify
Version:        1.2.2
Release:        1%{?dist}
Summary:        Convert HTML to markdown
License:        MIT
URL:            https://github.com/matthewwithanm/python-markdownify
Source0:        %{pypi_source markdownify}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools >= 61.2
BuildRequires:  python3-setuptools_scm >= 3.4.3
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-beautifulsoup4 >= 4.9
BuildRequires:  python3-six >= 1.15

%description
Convert HTML to markdown using Python.


%package -n python3-markdownify
Summary:        Convert HTML to markdown
Requires:       python3-beautifulsoup4 >= 4.9
Requires:       python3-six >= 1.15
Provides:       python-markdownify
Provides:       python3dist(markdownify) = %{version}

%description -n python3-markdownify
Convert HTML to markdown using Python.


%package help
Summary:        Documentation for markdownify
Requires:       python3-markdownify = %{version}-%{release}

%description help
Documentation for markdownify.


%prep
%autosetup -n markdownify-%{version} -p1

%build
%pyproject_build

%install
%pyproject_install

%files -n python3-markdownify
%license LICENSE
%{python3_sitelib}/markdownify/
%{python3_sitelib}/markdownify-%{version}*.dist-info/
%{_bindir}/markdownify

%files help
%license LICENSE
%doc README.rst

%changelog
* Wed May 27 2026 Python_Bot <Python_Bot@openeuler.org> - 1.2.2-1
- Initial package
