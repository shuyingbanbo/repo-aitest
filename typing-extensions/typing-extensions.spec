Name:           python-typing-extensions-4.13
Version:        4.13.2
Release:        1%{?dist}
Summary:        Backported and Experimental Type Hints for Python 3.8+ (v4.13)
License:        PSF-2.0
URL:            https://github.com/python/typing_extensions
Source0:        https://files.pythonhosted.org/packages/source/t/typing_extensions/typing_extensions-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-flit-core >= 3.11

%description
Backported and Experimental Type Hints for Python 3.8+ (version 4.13.x).
This compat package coexists with the official python3-typing-extensions package.


%package -n python3-typing-extensions-4.13
Summary:        Backported and Experimental Type Hints for Python 3.8+ (v4.13)
Provides:       python3-typing-extensions = %{version}-%{release}
Provides:       python3dist(typing-extensions) = %{version}

%description -n python3-typing-extensions-4.13
Backported and Experimental Type Hints for Python 3.8+ (version 4.13.x).
This compat package coexists with the official python3-typing-extensions package.


%package help
Summary:        Documentation for python-typing-extensions (v4.13)
Requires:       python3-typing-extensions-4.13
Provides:       python3-typing-extensions-4.13-doc

%description help
Documentation and examples for python-typing-extensions version 4.13.x.


%prep
%autosetup -n typing_extensions-%{version} -p1


%build
%pyproject_build


%install
%pyproject_install


%files -n python3-typing-extensions-4.13
%license LICENSE
%{python3_sitelib}/typing_extensions.py
%{python3_sitelib}/__pycache__/typing_extensions*.pyc
%{python3_sitelib}/typing_extensions-%{version}*.dist-info/


%files help
%license LICENSE
%doc README.md CHANGELOG.md


%changelog
* Thu May 28 2026 Python_Bot <Python_Bot@openeuler.org> - 4.13.2-1
- Initial compat package for typing-extensions 4.13.2
